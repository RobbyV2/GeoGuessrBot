import time
import json

from selenium.webdriver.common.by import By

import utils.driver as driver

def getCode():
    # Party Navigation
    driver.driver.get("https://geoguessr.com/party")
    time.sleep(3)

    # Invite Players Button
    invite_button = driver.driver.find_element(By.CSS_SELECTOR, ".button_button__CnARx.button_variantPrimary__xc8Hp")
    invite_button.click()
    time.sleep(1)

    # Code Text
    code_divs = driver.driver.find_elements(By.CSS_SELECTOR, ".invite-modal_value__5gORi")
    for code_div in code_divs:
        if not code_div.text.startswith("geoguessr.com/join"):
            code_text = code_div.text
            break
        
    return code_text