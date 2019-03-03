from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import time


# успешная авторизация
def correct_authorization(driver):
	#переход на страницу авторизации
	driver.get("https://olganesterova.teamlab.info/auth.aspx")
	# ввести логин и пароль
	elem1 = driver.find_element_by_name("login")
	elem1.send_keys("test@test.com")
	elem2 = driver.find_element_by_name("pwd")
	elem2.send_keys("test")
	elem2.send_keys(Keys.RETURN)
	# проперка успешного входа на сайт
	try:
		driver.find_element_by_class_name("header-base")
	except NoSuchElementException:
		return False
	return True

# авторизация без пароля
def authorization_without_password(driver):
	#переход на страницу авторизации
	driver.get("https://olganesterova.teamlab.info/auth.aspx")
	# ввести логин 
	elem1 = driver.find_element_by_name("login")
	elem1.send_keys("test@test.com")
	elem2 = driver.find_element_by_name("pwd")
	elem2.send_keys(Keys.RETURN)
	try:
		# проверка наличия ошибки на странице
		error1 = driver.find_element_by_class_name("errorBox")
		assert error1.is_displayed() is True
	except NoSuchElementException:
		return False
	return True

# создание новой компании
def create_company(driver):
	# перейти в модуль CRM
	element = driver.find_elements_by_css_selector("[class='link header']")
	element[2].click()
	# создать компанию
	create = driver.find_element_by_css_selector('[class="main-button-text"]')
	create.click()
	time.sleep(2)
	menu = driver.find_element_by_css_selector("[id='createNewButton']")
	menu_content = menu.find_element_by_css_selector("[class='dropdown-content']")
	menu_items = menu_content.find_elements_by_tag_name("li")
	item_company = menu_items[0]
	item_company.click()
	companyname = driver.find_element_by_css_selector("[class='textEdit generalField']")
	companyname.send_keys("NewCompany")
	save = driver.find_element_by_css_selector("[id='ctl00_ctl00_PageContent_BTPageContent_ctl00_saveContactButton']")
	save.click()
	print("company was created")


#cоздать событие в календаре
def new_event(driver):
	time.sleep(1)
	calendar = driver.find_element_by_css_selector("[class='top-item-box calendar']")
	calendar.click()
	time.sleep(4)
	#Выбрать день события
	week = driver.find_element_by_css_selector("[class='fc-week4']")
	day = week.find_element_by_css_selector("[class='fc-tue fc-widget-content fc-day29']")
	day.click()
	time.sleep(2)
	#задать название для события
	title = driver.find_element_by_css_selector("[class='title']")
	pole_title = title.find_element_by_xpath('//*[@id="fc_event_editor"]/div[4]/div[1]/input')
	pole_title.send_keys("New_Event")
	#сохранить событие
	save_event = driver.find_element_by_css_selector("#fc_event_editor > div.buttons.clearFix.editable > a.save-btn.button.blue.middle")
	save_event.click()
	time.sleep(1)
	print("event_created")

