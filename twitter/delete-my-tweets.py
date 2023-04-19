# This Python script is authored by Sergio Perea.
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

# Reemplaza con tus credenciales
email = "tu usuario"
password = "tu password"

chrome_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service)
driver.get("https://twitter.com/login")

time.sleep(2)

# Inicia sesión en Twitter
wait = WebDriverWait(driver, 10)
email_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='username']")))
email_field.send_keys(email)
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

# Espera a que se cargue la página principal de Twitter
wait.until(EC.url_contains("https://twitter.com/home"))

# Navega a la página del muro del usuario
driver.get("https://twitter.com/" + email)

wait.until(EC.url_contains("https://twitter.com/" + email))

# Bucle para eliminar todos los tweets
while True:
    try:
# Encuentra el botón de "Más opciones"
        more_options_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='caret']")))

        # Encuentra y haz clic en el botón de "Más opciones" usando JavaScript
        driver.execute_script("arguments[0].click();", more_options_button)

        # Encuentra y haz clic en la opción "Eliminar Tweet"
        delete_tweet_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Eliminar']/ancestor::div[@role='menuitem']")))
        delete_tweet_option.click()

        # Encuentra y haz clic en el botón "Eliminar" en el cuadro de diálogo de confirmación
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Eliminar']"))).click()
        # Espera un momento antes de buscar el siguiente tweet
        time.sleep(2)
    except TimeoutException:
        # Si no se encuentran más tweets, sal del bucle
        break


# Cierra el navegador
driver.quit()
