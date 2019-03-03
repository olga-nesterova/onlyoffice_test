from selenium import webdriver
import defs

driver = webdriver.Chrome(executable_path="path_to_chromedriver")

# авторизация без пароля
defs.authorization_without_password(driver)

# авторизация без пароля
defs.authorization_without_login(driver)
driver.quit()
