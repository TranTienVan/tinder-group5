from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import random

def register_case(driver: webdriver.Chrome):
    driver.get("http://localhost:5173/register")
    
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
    tags = driver.find_elements(By.CLASS_NAME, "asterisk-left")

    tags[1].find_element(By.TAG_NAME, "input").send_keys(email)
    tags[2].find_element(By.TAG_NAME, 'input').send_keys(password)
    
    driver.find_element(By.CLASS_NAME, "el-button").click()
    time.sleep(3)
    return driver.current_url
    
    