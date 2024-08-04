import openpyxl.workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import openpyxl

# website used to extract the information
# https://www.saucedemo.com/

#method XPATH used for to search the directory unique field
# //input[@class='name']

username = "standard_user"
password = "secret_sauce"
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
sleep(3)
#using the usarname for login
login_name = driver.find_element(By.XPATH,"//input[@id='user-name']")
login_name.send_keys(username)
sleep(1)
#using the password for login
login_senha= driver.find_element(By.XPATH,"//input[@id='password']")
login_senha.send_keys(password)
sleep(1)
#find the button and click for to do login in website
button = driver.find_element(By.XPATH,"//input[@id='login-button']")
button.click()
sleep(3)
# getting the product names 
products = driver.find_elements(By.XPATH,"//div[@class='inventory_item_name ']")
#getting the prices of the products
prices = driver.find_elements(By.XPATH,"//div[@class='inventory_item_price']")

#Create the workbook
workbook = openpyxl.Workbook()
#create the sheet 'products'
workbook.create_sheet('products')
#select the sheet 'products'
sheet_products = workbook['products']
sheet_products['A1'].value = 'Name'
sheet_products['B1'].value = 'Price'


#acess the values in products and prices
for product,price in zip(products,prices):
    sheet_products.append([product.text,price.text])
    
workbook.save("products.xlsx")
