from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# info
google_email = "cpqa666"
google_pw = "Cpqa123!"

# initial Chrome
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)




driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.lang.live/")

def goto_register():
    try:
        register_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[3]/div/div[4]/button/div/p[2]'))                                                       
            )
        register_button.click()
    except Exception as e:
        print(f"Error in goto_register: {e}")

def fb_login():
    try:
        fb_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[2]/img[1]'))
            )
        fb_button.click()
    except Exception as e:
        print(f"Error in fb_register: {e}")

def google_login():
    try:
        google_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div/img'))
        )
        google_button.click()
        driver.switch_to.window(driver.window_handles[1])

        # enter gmail
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="email"]'))
        )
        email_input.send_keys(google_email)
        email_input.send_keys(Keys.RETURN)
        time.sleep(10)
        # enter pw
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))
        )
        password_input.send_keys(google_pw)
        password_input.send_keys(Keys.RETURN)

        driver.switch_to.window(driver.window_handles[0])
    except Exception as e:
        print(f"Error in google_login: {e}")



goto_register()
time.sleep(1)
google_login()
time.sleep(3)

driver.close()