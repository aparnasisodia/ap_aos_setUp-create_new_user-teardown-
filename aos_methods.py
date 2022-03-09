import sys
from selenium import webdriver
import aos_locators as locators
from time import sleep
import datetime
from selenium.webdriver.common.by import By
from faker import Faker
fake = Faker(locale='en_CA')

# ------------------------Fake date section------------------------------
first_name  = fake.first_name()
last_name = fake.last_name()
middle_name = fake.first_name()
full_name = f'{first_name} {last_name} {fake.pyint(1111,2999)}'
new_username = f'{first_name}{fake.pyint(1,999)}'.lower()
new_password = fake.password()
email = fake.email() #f'{new_username}'
phone_number = fake.phone_number()
country = fake.current_country()[:5]
city = fake.city()[:5]
address = fake.address().replace("\n"," ")[:10] #'123 langara'
state = 'BC' #fake.state()[:5]
postal_code = 'L6Y555' #fake.postal_code()[:5]


driver = webdriver.Chrome('//Users/owner/Desktop/pythonProject/chromedriver')

def setUp():
    print(f'Launch {locators.app} home page')
    print('---------------------------****---------------------------')
    driver.maximize_window()

    driver.get(locators.aos_url)
    print(driver.current_url)
    print(driver.title)

    if driver.current_url == locators.aos_url or driver.title == '${nbsp}Advantage Shopping': # use $nbsp without space for title
        print(f'Yeh! {locators.app} home page launched Sucessfully, Move ahead!')
        print(f'current URL: {driver.current_url},Page Title: {driver.title}')

    else:
        print('Advantage DEMO home page did not launch.')
        print(driver.current_url)
        print(driver.title)
        print(f'{locators.app} homepage URL: {driver.current_url},\nHome Page Title: {driver.title}')
        sleep(0.25)

def teardown():  #
    if driver is not None:
        print('------------------**have an awesome day **------------------')
        print(f'The Test is completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()

# def create_new_user():
#     driver.find_element(By.ID, 'menuUserLink').click()
#     sleep(4)
#     driver.find_element(By.LINK_TEXT,'CREATE NEW ACCOUNT').click()
#     sleep(3)
#
#     #creating user details:
#     driver.find_element(By.NAME,'usernameRegisterPage').send_keys(locators.admin_username)
#     sleep(0.25)
#     driver.find_element(By.NAME,'emailRegisterPage').send_keys(email)
#     sleep(0.25)
#     driver.find_element(By.NAME,'passwordRegisterPage').send_keys(new_password)
#     sleep(0.25)
#     driver.find_element(By.NAME,'confirm_passwordRegisterPage').send_keys(new_password)
#     sleep(0.25)
#     driver.find_element(By.NAME,'first_nameRegisterPage').send_keys(first_name)
#     sleep(0.25)
#     driver.find_element(By.NAME,'last_nameRegisterPage').send_keys(last_name)
#     sleep(0.25)
#     driver.find_element(By.NAME,'phone_numberRegisterPage').send_keys(phone_number)
#     sleep(0.25)
#     driver.find_element(By.NAME,'countryListboxRegisterPage').send_keys(country)
#     sleep(0.25)
#     driver.find_element(By.NAME,'cityRegisterPage').send_keys(city)
#     sleep(0.25)
#     driver.find_element(By.NAME, 'addressRegisterPage').send_keys(address)
#     sleep(0.25)
#     driver.find_element(By.NAME,'state_/_province_/_regionRegisterPage').send_keys(state)
#     sleep(0.25)
#     driver.find_element(By.NAME,'postal_codeRegisterPage').send_keys(postal_code)
#     sleep(0.25)
#     driver.find_element(By.NAME, 'i_agree').is_selected()
#     sleep(0.25)
#     driver.find_element(By.NAME,'i_agree').click()
#     sleep(0.25)
#     driver.find_element(By.ID,'register_btnundefined').click()
#     sleep(0.25)
#     if driver.find_element(By.LINK_TEXT, new_username).is_displayed():
#         print(f'---------New User"{new_username}/{new_password},{email}" is added----------------')
#
#     else:
#         print(f'User is not created!')

setUp()
create_new_user()
teardown()

