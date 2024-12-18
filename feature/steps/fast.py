from selenium import webdriver
import time 
from behave import *

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@Given(U'Open Browser and Visit Website')
def open_picabo(context):
    context.driver= webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.pickaboo.com/login/")
    time.sleep(2)


# Scenario 1
@When(U'Click on Mobile Number/Email Section')
def step_number1(context):
    context.driver.find_element(By.XPATH, "//input[@placeholder='Mobile Number/Email']").click()
    time.sleep(2)
@Then(U'Input Mobile Number')
def step_number2(context):
    context.driver.find_element(By.XPATH, "//input[@placeholder='Mobile Number/Email']").send_keys('01749653931')
    time.sleep(2)
@When(U'Click on Password Section')
def step_password1(context):
    context.driver.find_element(By.XPATH, "//input[@placeholder='Password']").click()
    time.sleep(2)
@Then(U'Input Password')
def step_password2(context):
    context.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys('sadi1234')
    time.sleep(2)
@When(U'Click on Log In button')
def Log_In(context):
   context.driver.find_element(By.XPATH, "//span[@class='MuiButton-label']").click()
   time.sleep(5)
@When(U'Click on Smartphone option')
def Smart_Phone(context):
   context.driver.find_element(By.XPATH, "//div[@class='home-banner__menu']//a[@class='a-tag'][normalize-space()='Smartphones']").click()
   time.sleep(5)
@Then(U'Click on Camera Phone option')
def Camera_Phone(context):
   context.driver.find_element(By.XPATH, "//section[@class='ProductTwo__StyledProductTwo-sc-1cxokfi-0 fwGDQy product-layout-two pt-30 pb-30']//div[@class='row']//div[1]//div[1]//div[1]//img[1]").click()
   time.sleep(5)
@When(U'Click on First phone option')
def First_Phone(context):
   context.driver.find_element(By.XPATH, "(//h4[@class='product-title'])[1]").click()
   time.sleep(5)
@Then(U'Click on Color Phone option')
def Color_Phone(context):
   context.driver.find_element(By.XPATH, "//div[@class='views']//div[1]//center[1]//img[1]").click()
   time.sleep(5)
@When(U'Click on Add To Cart option')
def AddToCart(context):
   context.driver.find_element(By.XPATH, "//span[normalize-space()='ADD TO CART']").click()
   time.sleep(5)
@Then(U'Check that Product cart is successfull')
def Product_Cart(context):
   context.driver.find_element(By.XPATH, "//p[normalize-space()='cart']").click()
   time.sleep(5)


# Scenario 2
@When(U'Click on Shopping option')
def Shopping(context):
   context.driver.find_element(By.XPATH, "//p[normalize-space()='cart']").click()
   time.sleep(5)
@Then(U'Click on Proceed to Checkout option')
def Proceed_Checkout(context):
   context.driver.find_element(By.XPATH, "//span[normalize-space()='Proceed to checkout']").click()
   time.sleep(5)
@When(U'Click on Continue option')
def Continue(context):
   context.driver.find_element(By.XPATH, "//span[normalize-space()='CONTINUE']").click()
   time.sleep(5)

