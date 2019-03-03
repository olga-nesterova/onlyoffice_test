from selenium import webdriver
import defs

driver = webdriver.Chrome(executable_path="path_to_chromedriver")

#создать компанию
defs.correct_authorization(driver)
defs.create_company(driver)
driver.quit()
