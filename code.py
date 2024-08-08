import random
import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#initialize webdriver
driver=webdriver.Chrome()

def highlight_element(element):
    driver.execute_script("arguments[0].setAttribute('style', 'border: 6px solid blue;');", element)
    time.sleep(2)
    driver.execute_script("arguments[0].setAttribute('style', 'border: 0px;');", element)

#Open URL and maximize window
driver.get('https://www.bewakoof.com/')
driver.maximize_window()
time.sleep(5)

#dont-allow-popup
dont_allow=driver.find_element('xpath', '//*[@id="wzrk-cancel"]')
dont_allow.click()
time.sleep(2)

#scroll home-page
for i in range(0,4):
    driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
for i in range(0,4):
    driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
    time.sleep(1)

#login details
login=driver.find_element('xpath', '//*[@id="loginLink"]')
highlight_element(login)
login.click()
time.sleep(2)

#Continue with email 
email_button=driver.find_element('xpath', '//*[@id="web_email_login"]')
highlight_element(email_button)
email_button.click()
time.sleep(2)

#enter email
email=driver.find_element('xpath', '//*[@id="email_input"]')
email.send_keys('aprameyaputtu2403.a@gmail.com')
time.sleep(2)
#driver.wait()

#password
password=driver.find_element(By.XPATH, '//*[@id="mob_password"]')
password.send_keys('Aprameyaa@2403a')
time.sleep(2)

#login-button
login_button=driver.find_element('xpath', '//*[@id="mob_login_password_submit"]')
highlight_element(login_button)
login_button.click()
time.sleep(5 )

#dont-allow-popup
dont_allow1=driver.find_element('xpath', '//*[@id="wzrk-cancel"]')
dont_allow1.click()
time.sleep(1)

#landing at home-page
#Men page
men=driver.find_element('xpath', '//*[@id="testMenuSelect-shop-men"]/span/span')
highlight_element(men)
men.click()
time.sleep(2)

#scroll men's page
for i in range(0,4):
    driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
for i in range(0,4):
    driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
    time.sleep(1)

#first_pic
first_pic=driver.find_element('xpath', '//*[@id="testProductcard_1"]/a/div/div[1]/div[1]/img')
first_pic.click()
time.sleep(2)

homepage=driver.find_element('xpath','//*[@id="app"]/div/div[2]/div[1]/header/div[2]/div/div[1]/a')
homepage.click()
time.sleep(2)

next_click=driver.find_element("xpath",'//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[3]/i')
for i in range(0,7):
    next_click.click()
    time.sleep(1)

#select size
size=driver.find_element('xpath','//*[@id="testSizes_S"]')
highlight_element(size)
size.click()
time.sleep(2)

#add-to-bag
add_to_bag=driver.find_element('xpath','//*[@id="addButtons"]/div/div[2]')
highlight_element(add_to_bag)
add_to_bag.click()
time.sleep(2)

#Men page
men=driver.find_element('xpath', '//*[@id="testMenuSelect-shop-men"]/span/span')
highlight_element(men)
men.click()
time.sleep(2)

#category
category=driver.find_element('xpath','//*[@id="app"]/div/div[2]/div[2]/div[2]/div[3]/div[1]/div/div/div[2]/div/div[1]/div[1]/div/span')
highlight_element(category)
category.click()
time.sleep(2)

#joggers
joggers=driver.find_element('xpath','//*[@id="app"]/div/div[2]/div[2]/div[2]/div[3]/div[1]/div/div/div[2]/div/div[1]/div[2]/div/ul/li[4]/div/span/a')
highlight_element(joggers)
joggers.click()
time.sleep(2)

#category
category1=driver.find_element('xpath','//*[@id="app"]/div/div[2]/div[2]/div[2]/div[3]/div[1]/div/div/div[2]/div/div[1]/div[1]/div/span')
highlight_element(category1)
category1.click()
time.sleep(2)

#scroll jogger's page
for i in range(0,3):
    driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
for i in range(0,3):
    driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
    time.sleep(1)

#j1
j1=driver.find_element('xpath','//*[@id="testProductcard_1"]/a/div/div[1]/div[1]/img')
j1.click()
time.sleep(2)

#sizej1
sizej1=driver.find_element('xpath','//*[@id="testSizes_M"]')
highlight_element(sizej1)
sizej1.click()
time.sleep(2)

#atc1
atcj1=driver.find_element('xpath','//*[@id="addButtons"]/div/div[2]')
highlight_element(atcj1)
atcj1.click()
time.sleep(2)

#go-to-bag
go_to_bag=driver.find_element('xpath','//*[@id="addButtons"]/div/div[2]')
highlight_element(go_to_bag)
go_to_bag.click()
time.sleep(2)

#add-address
add_address=driver.find_element('xpath','//*[@id="os_payNow_btn"]')
add_address.click()
time.sleep(2)

#name
name=driver.find_element('xpath','//*[@id="name_field"]')
name.send_keys("ArunKumar")
time.sleep(1)

#phone
phone=driver.find_element('xpath','//*[@id="mobile_field"]')
phone.send_keys("7624957729")
time.sleep(1)

#pincode
pincode=driver.find_element('xpath','//*[@id="pincode_field"]')
pincode.send_keys("560019")
time.sleep(1)

#city
city=driver.find_element('xpath','//*[@id="city_field"]')
city.send_keys("Bangalore")
time.sleep(1)
#State
state=driver.find_element('xpath','//*[@id="state_field"]')
state.send_keys("")
time.sleep(1)
#Flat-no
flat_no=driver.find_element('xpath','//*[@id="addrLine1_field"]')
flat_no.send_keys("457 2nd Main Road")
time.sleep(1)
#Area
area=driver.find_element('xpath','//*[@id="addrLine2_field"]')
area.send_keys("Basavanagudi")
time.sleep(1)
#Landmark
landmark=driver.find_element('xpath','//*[@id="landmark_field"]')
landmark.send_keys("KG Nagar Swimming Pool")
time.sleep(1)
#Save adddress as Home
save_address=driver.find_element('xpath','//*[@id="AddressUpdate"]/div/div/div/div[2]/form/div[1]/div[9]/div/div[1]/label')
save_address.click()
time.sleep(1)
#Save-address-button
save_address_button=driver.find_element('xpath','//*[@id="addr_save_button"]')
highlight_element(save_address)
save_address_button.click()
time.sleep(5)

#payments page
card_number=driver.find_element('xpath','//*[@id="pay_cardNumber_input"]')
card_number.send_keys("4779654123657894")
time.sleep(2)
valid=driver.find_element('xpath','//*[@id="pay_expiryDetail_input"]')
valid.send_keys("12/27")
time.sleep(2)
cvv=driver.find_element('xpath','//*[@id="pay_cvv_input"]')
cvv.send_keys("123")
time.sleep(2)
name_on_card=driver.find_element('xpath', '//*[@id="pay_cardName_input"]')
name_on_card.send_keys("Aprameya")
time.sleep(2)
pay=driver.find_element('xpath','//*[@id="pay_addCard_button"]')
highlight_element(pay)
#pay.click()
time.sleep(5)
driver.quit()
