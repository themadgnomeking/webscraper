from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains 
import time

url = 'https://www.youtube.com/user/thandadj'
browser = webdriver.Chrome(executable_path='D:\Projects\Python\webscraper\driver\win32\chromedriver.exe')
browser.get(url)
#105.0.5195.128 (Official Build) (64-bit)
xpath_local = '//*[@id="thumbnail"]'

action = ActionChains(browser)

time.sleep(5)
link_click = browser.find_element(By.XPATH, '//*[@id="thumbnail"]')
#browser.findElement('//*[@id="thumbnail"]').sendKeys(keys.RETURN)
#browser.find_element_by_xpath('//*[@id="details"]').click()
action.click(on_element = link_click)

action.perform()