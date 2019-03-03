from selenium import webdriver
import defs

driver = webdriver.Chrome(executable_path="path_to_chromedriver")

#создать компанию
defs.correct_authorization(driver)
defs.new_event(driver)
driver.quit()
