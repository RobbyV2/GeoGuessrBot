import time

from selenium.webdriver.common.by import By

import utils.driver as driver


def switchMode(mode):
    # Party Navigation
    driver.driver.get("https://geoguessr.com/party")
    time.sleep(3)

    # Game Mode Menu
    invite_button = driver.driver.find_element(
        By.CSS_SELECTOR, ".footer-controls_gameModeButton__RJRJm"
    )
    invite_button.click()
    time.sleep(1)

    if mode == "Team Duels":
        team_image = driver.driver.find_element(By.XPATH, "//img[@alt='Team Duels']")
        team_image.click()
        time.sleep(1)

    if mode == "Duels":
        team_image = driver.driver.find_element(By.XPATH, "//img[@alt='Duels']")
        team_image.click()
        time.sleep(1)

    if mode == "Battle Royale Distance":
        team_image = driver.driver.find_element(
            By.XPATH, "//img[@alt='Battle Royale Distance']"
        )
        team_image.click()
        time.sleep(1)

    return
