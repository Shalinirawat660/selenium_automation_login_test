from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Import to simulate key-driven events

# Initialize a Chrome WebDriver instance, providing the path to the ChromeDriver executable
driver = webdriver.Chrome('C:\\Users\\shalini\\Downloads\\chromedriver-win64\\chromedriver')

# Define the URL of the web application you want to automate (in this case, LeetCode login)
url = "https://leetcode.com/accounts/login/?next="

# Open the specified URL in the Chrome browser
driver.get(url)

# Locate the username and password input fields on the web page
username_field = driver.find_element_by_name("login")
password_field = driver.find_element_by_name("password")

# Simulate user input by entering a username and password
username_field.send_keys("example@gmail.com")  # Replace with your actual email
password_field.send_keys("examplepassword")    # Replace with your actual password

# Locate the login button on the web page and simulate a click event
login_button = driver.find_element_by_id("signin_btn")
login_button.click()

# Close the browser and WebDriver session after completing the login process
driver.quit()