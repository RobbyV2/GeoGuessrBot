import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

with open("config.json") as config_file:
    config = json.load(config_file)

gg_email = config["gg_email"]
gg_pass = config["gg_pass"]

config_file.close

options = webdriver.FirefoxOptions()

options.add_argument("-headless")
driver = webdriver.Firefox(options=options)
driver.get("https://geoguessr.com")
time.sleep(3)

# Cookie Accept
button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
button.click()
time.sleep(1)

# Login Button
button = driver.find_element(
    By.CSS_SELECTOR, ".button_link__xHa3x.button_variantSecondary__lSxsR"
)
button.click()
time.sleep(3)

# Email Field
email_field = driver.find_element(
    By.CSS_SELECTOR, "input.text-input_textInput__HPC_k[type='email']"
)
email_field.send_keys(gg_email)
time.sleep(1)

# Password Field
password_field = driver.find_element(
    By.CSS_SELECTOR, "input.text-input_textInput__HPC_k[type='password']"
)
password_field.send_keys(gg_pass)
time.sleep(1)

# Login Button to Dashboard
login_button = driver.find_element(
    By.CSS_SELECTOR, ".button_button__CnARx.button_variantPrimary__xc8Hp"
)
login_button.click()
time.sleep(3)
