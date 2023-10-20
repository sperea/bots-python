import time
import os
import html
import re
from dotenv import load_dotenv
from selenium import webdriver
from mastodon import Mastodon
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException

load_dotenv()

# Credenciales de Twitter
username = os.environ.get('twitter_username')
password = os.environ.get('twitter_password')

# Configuración de Mastodon
mastodon_host = os.environ.get('mastodon_host')
mastodon_client_id = os.environ.get('mastodon_client_id')
mastodon_client_secret = os.environ.get('mastodon_client_secret')
mastodon_access_token = os.environ.get('mastodon_access_token')

# Autenticación en Mastodon
mastodon = Mastodon(
    client_id = mastodon_client_id,
    client_secret = mastodon_client_secret,
    access_token = mastodon_access_token,
    api_base_url = mastodon_host
)

toots = mastodon.account_statuses(mastodon.account_verify_credentials()['id'])

chrome_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service)
driver.get("https://twitter.com/login")

time.sleep(2)

# Inicia sesión en Twitter
wait = WebDriverWait(driver, 10)
email_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='username']")))
email_field.send_keys(username)
email_field.send_keys(Keys.RETURN)

time.sleep(2)

password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='current-password']")))
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

time.sleep(5)

# Aceptar cookies
accept_cookies_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Aceptar todas las cookies']")))
accept_cookies_button.click()

# Espera a que se cargue la página principal de Twitter
wait.until(EC.url_contains("https://twitter.com/home"))

# Navega a la página del muro del usuario
driver.get("https://twitter.com/" + username)

wait.until(EC.url_contains("https://twitter.com/" + username))

# Carga los toots ya publicados
try:
    with open('toots_publicados.txt', 'r') as f:
        toots_publicados = set(line.strip() for line in f)
except FileNotFoundError:
    toots_publicados = set()

# Publica cada toot en Twitter
for toot in toots:
    if not toot['mentions'] and str(toot['id']) not in toots_publicados:
        print(str(toot['id']) + " no está en publicados")
        print("publicado: " + str(toots_publicados))
        time.sleep(5)  # Espera un poco entre cada toot para evitar ser bloqueado por Twitter
        tweet_button = driver.find_element("xpath", "//a[@data-testid='SideNav_NewTweet_Button']")
        try:
            # Intentar hacer clic en el botón "Twittear"
            tweet_button.click()
        except ElementClickInterceptedException:
            # Si se produce una excepción de clic interceptado, imprimir un mensaje y continuar con el siguiente toot
            print(f"No se pudo hacer clic en el botón 'Twittear' para el toot {toot['id']} - {toot['content']}. Continuando con el siguiente...")
            continue
        wait = WebDriverWait(driver, 4)
        text_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='tweetTextarea_0']")))
        toot_content = html.unescape(toot['content'])
        toot_content = re.sub('<[^<]+?>', '', toot_content)
        text_field.send_keys(toot_content)
        print(toot_content)
        tweet_button = driver.find_element("xpath", "//div[@data-testid='tweetButton']")
        tweet_button.click()
        wait = WebDriverWait(driver, 6)

        # Añade el toot al conjunto de toots publicados y actualiza el archivo
        toots_publicados.add(toot['id'])
        with open('toots_publicados.txt', 'a') as f:
            f.write(str(toot['id']) + '\n')

# Cierra el navegador
driver.quit()