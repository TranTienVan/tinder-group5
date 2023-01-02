from dotenv import load_dotenv
import pytest
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
from cases import register_case, login_case

@pytest.fixture
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    return driver

def host():
    
    return "http://localhost:5173"


def test_register_success(driver: webdriver.Chrome):
    result = register_case(driver)
    
    assert "/login" in result

def test_login_success(driver: webdriver.Chrome):
    email = 'trantienvan-8479699@gmail.com'
    password = 'trantienvan'
    
    
    result = login_case(driver, email, password)
    assert "/match" in result
    
    
