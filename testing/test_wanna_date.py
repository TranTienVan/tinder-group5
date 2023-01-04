from dotenv import load_dotenv
import pytest
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
from cases import *

@pytest.fixture
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    return driver

def host():
    
    return "http://localhost:5173"


def test_register_success(driver: webdriver.Chrome):
    result = register_case(driver)
    
    assert "/login" in result

# def test_login_success(driver: webdriver.Chrome):
#     email = 'trantienvan-8479699@gmail.com'
#     password = 'trantienvan'
    
#     result = login_case(driver, email, password)
#     assert "/match" in result
    
# def test_login_fail(driver: webdriver.Chrome):
#     email = 'non-exist@gmail.com'
#     password = 'trantienvan'

#     result = login_case(driver, email, password)
#     assert "/login" in result

# def test_register_fail(driver: webdriver.Chrome):
#     result = register_fail_case(driver)
#     assert "/register" in result
    
# def test_logout(driver: webdriver.Chrome):
#     result = logout_case(driver,'abc@gmail.com', '123456')
#     assert "/login" in result

# def test_update_profile(driver: webdriver.Chrome):
#     result = update_profile_case(driver, 'abc@gmail.com', '123456')
#     assert "/setting" in result

# def test_chat_case(driver: webdriver.Chrome):
#     result = chat_case(driver, 'abc@gmail.com', '123456')
#     assert "/chat" in result