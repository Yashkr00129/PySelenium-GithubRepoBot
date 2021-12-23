# Libs
# Subprocess
# Selenium
# sys.argv
from selenium import webdriver
from selenium.webdriver.common.by import By

username = input("Enter your github username or email: ")
password = input("Enter your github password: ")
repo_name = input("What do you want your repository to be called: ")


class RepoNameError(Exception):
    pass


browser = webdriver.Chrome()
browser.get("https://github.com")

# Sign In
signin_link = browser.find_element(By.LINK_TEXT, "Sign in")
signin_link.click()
username_box = browser.find_element(By.ID, "login_field")
username_box.send_keys(username)
password_box = browser.find_element(By.ID, "password")
password_box.send_keys(password)
password_box.submit()

# Make Repo
browser.implicitly_wait(5)
add_link = browser.find_element(By.CLASS_NAME, "btn-primary")
add_link.click()
browser.implicitly_wait(5)
repo_name_field = browser.find_element(By.CSS_SELECTOR, ".js-repo-name")
repo_name_field.send_keys(repo_name)
repo_name_field.submit()

browser.implicitly_wait(5)
repo_help = browser.find_element(By.ID, "empty-setup-push-repo-echo")

print(repo_help.text)
