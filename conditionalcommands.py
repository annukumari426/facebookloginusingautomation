# login to facebook using automation

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.get("https://www.facebook.com/")
user_ele= driver.find_element_by_name("email")
print(user_ele.is_displayed())   #returns true/false based on element status
print(user_ele.is_enabled())     #returns true/false



pass_ele =  driver.find_element_by_name("pass")
print(pass_ele.is_displayed())   #returns true/false based on element status
print(pass_ele.is_enabled())     #returns true/flse

user_ele.send_keys("your user name")
pass_ele.send_keys("Your password")
driver.find_element_by_name("login").click()