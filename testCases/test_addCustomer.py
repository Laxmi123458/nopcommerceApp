import time
import pytest
import self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username= ReadConfig.getUseremail()
    password= ReadConfig.getPassword()
    logger=LogGen.loggen() #logger

    @pytest.mark.sanity
    def test_addCustomer(self,setup):  #method
        self.logger.info("Test_003_AddCustomer")
        self.driver=setup #Launch the driver
        self.driver.get(self.baseURL) #Launchthe site
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        time.sleep(3)
        self.lp.clickLogin() #Login
        time.sleep(3)
        self.logger.info("Login is succesful")

        self.logger.info("Starting Add Customer test")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.addcust.clickOnAddnew()

        self.logger.info("Providing customer info")

        self.email= random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Test")
        self.addcust.setLastName("Pro")
        self.addcust.setGender("Male")
        self.addcust.setCompanyName("TestQA")
        self.addcust.setIsTaxExempt()
        self.addcust.setNewsletter("nopCommerce admin demo store")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setActive()
        self.addcust.setCustomerMustChangePassword()
        self.addcust.setAdminComment("This is for testing")
        self.addcust.clickOnSave()

        self.logger.info("Saving customer info")

        self.logger.info("Add customer validation started")

        self.msg=self.driver.find_element(By.TAG_NAME, "body").text #body means which will capture everything displayed on the page in the form of text

        print(self.msg)
        if 'Customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("Add customer test passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png") #screenshot
            self.logger.info("Add customer test failed")
            assert False == False

        self.driver.quit()
        self.logger.info("Ending Homepage tile test")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits): #User defined function
    return ''.join(random.choice(chars) for x in range(size)) #random is a predefined package in python



