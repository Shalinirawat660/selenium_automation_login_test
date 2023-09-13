from selenium import webdriver
from selenium.webdriver.common.keys import Keys  #to simulate key-driven events

#a Chrome WebDriver instance,path to the ChromeDriver executable
driver = webdriver.Chrome('C:\\Users\\shalini\\Downloads\\chromedriver-win64\\chromedriver')

#URL of the web application (in this case, LeetCode login)
url = "https://leetcode.com/accounts/login/?next="

#opening the URL in the Chrome browser
driver.get(url)

#locating the username and password input fields on the page
username_field = driver.find_element_by_name("login")
password_field = driver.find_element_by_name("password")

#simulating user input by entering username and password
username_field.send_keys("example@gmail.com")
password_field.send_keys("examplepassword")

#locating the login button on the web page to simulate a click event
login_button = driver.find_element_by_id("signin_btn")
login_button.click()

#closing the browser and WebDriver after completing the login process
driver.quit()
