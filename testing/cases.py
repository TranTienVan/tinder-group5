from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import random

def register_case(driver: webdriver.Chrome):
    driver.get("http://localhost:5173/register")
    time.sleep(0.5)
    
    full_name = f"trantienvan-{random.randint(1, 10000000)}"
    email = full_name + "@gmail.com"
    password = "trantienvan"
    birthday = f"{random.randint(2000, 2010)}-{str(random.randint(1, 12)).zfill(2)}-{str(random.randint(1, 28)).zfill(2)}"
    gender = ["Male", "Female", "Other"]
    sexual = ["Straigt", "Gay", "Lesbian", "Bisexual"]

    tags = driver.find_elements(By.CLASS_NAME, "asterisk-left")

    tags[0].find_element(By.TAG_NAME, "input").send_keys(full_name)
    tags[1].find_element(By.TAG_NAME, 'input').send_keys(email)
    tags[2].find_element(By.TAG_NAME, "input").send_keys(password)
    tags[3].find_element(By.TAG_NAME, "input").send_keys(password)
    tags[4].find_element(By.TAG_NAME, "input").click()
    time.sleep(0.5)
    tags[4].find_element(By.TAG_NAME, "input").send_keys(birthday)
    time.sleep(0.5)
    driver.find_element(By.CLASS_NAME, "el-form-item__label").click()

    tags[5].find_element(By.TAG_NAME, "input").click()
    time.sleep(0.5)
    driver.find_elements(By.TAG_NAME, "li")[random.randint(0, len(gender) - 1)].click()

    tags[6].find_element(By.TAG_NAME, "input").click()
    time.sleep(0.5)
    driver.find_elements(By.TAG_NAME, "li")[random.randint(3, 3 + len(sexual) - 1)].click()

    time.sleep(0.5)
    driver.find_element(By.CLASS_NAME, "el-button").click()
    time.sleep(3)
    
    return driver.current_url

def login_case(driver: webdriver.Chrome, email, password):
    driver.get("http://localhost:5173/login")
    time.sleep(0.5)
    tags = driver.find_elements(By.CLASS_NAME, "asterisk-left")

    tags[1].find_element(By.TAG_NAME, "input").send_keys(email)
    tags[2].find_element(By.TAG_NAME, 'input').send_keys(password)
    
    driver.find_element(By.CLASS_NAME, "el-button").click()
    time.sleep(3)
    return driver.current_url
    
def register_fail_case(driver: webdriver.Chrome):
    driver.get("http://localhost:5173/register")
    time.sleep(0.5)
    time.sleep(0.5)
    driver.find_element(By.CLASS_NAME, "el-button").click()
    time.sleep(1)
    return driver.current_url

def logout_case(driver: webdriver.Chrome, email, password):
    login_case(driver, email, password)
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, "logout").click()
    time.sleep(0.5)
    return driver.current_url

def update_profile_case(driver: webdriver.Chrome, email, password):
    login_case(driver, email, password)

    # update profile
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "material-symbols-rounded").click()
    time.sleep(0.5)
    tags = driver.find_elements(By.CLASS_NAME, "asterisk-left")
    interest = str(random.randint(100, 99999))
    tags[6].find_element(By.TAG_NAME, "input").clear()
    time.sleep(0.5)
    tags[6].find_element(By.TAG_NAME, "input").send_keys(interest)
    time.sleep(0.5)
    driver.find_element(By.CLASS_NAME, "is-plain").click()
    time.sleep(2)
    driver.refresh()
    time.sleep(7)
    tags = driver.find_elements(By.CLASS_NAME, "asterisk-left")
    time.sleep(0.5)
    assert tags[6].find_element(By.TAG_NAME, "input").get_attribute("value") == interest
    return driver.current_url

def chat_case(driver: webdriver.Chrome, email, password):
    login_case(driver, email, password)
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "container").click()
    time.sleep(0.5)
    message = f"Hello {random.randint(1, 100000)}"
    driver.find_element(By.TAG_NAME, "input").send_keys(message)
    time.sleep(0.5)
    driver.find_element(By.CLASS_NAME, "container__input-area__send-icon").click()
    time.sleep(2)
    tags = driver.find_elements(By.CLASS_NAME, "container-right-side")
    assert tags[-1].find_element(By.CLASS_NAME, "container__message").text == message
    return driver.current_url

def like_case(driver: webdriver.Chrome, email, password):
    login_case(driver, email, password)
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "img[src='/src/assets/like.png']").click()
    time.sleep(0.5)
    return driver.current_url

def upgrade_premium(driver: webdriver.Chrome, email, password):
    login_case(driver, email, password)
    time.sleep(6)
    driver.find_element(By.CLASS_NAME, "material-symbols-rounded").click()
    time.sleep(0.5)
    tags = driver.find_elements(By.CLASS_NAME, "asterisk-left")
    tags[8].find_element(By.TAG_NAME, "button").click()
    time.sleep(2)
    return driver.current_url