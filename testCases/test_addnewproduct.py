import time

from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from selenium.webdriver.common.by import By
from pageObjects.AddnewproductPage import AddnewProduct

class Test_007_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username= ReadConfig.getUseremail()
    password= ReadConfig.getPassword()

    def test_addNewProduct(self,setup):  #method
        self.driver=setup #Launch the driver
        self.driver.get(self.baseURL) #Launchthe site
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin() #Login

        self.addnew = AddnewProduct(self.driver)
        self.addnew.clickOnCatalogMenu()
        self.addnew.clickOnCatalogMenuItems()
        self.addnew.clickOnAddNewButton()

        self.addnew.setProductName("testro")
        self.addnew.setShortDescription("First example")
        self.addnew.setFullDescription("the first test successlly runned")
        time.sleep(5)
        self.addnew.settxtSku("test")
        #self.addnew.setCategories("Computers")

        self.addnew.setPrice("10")
        self.addnew.setTaxExempt()
        self.addnew.setShipping()

        self.addnew.setDimensions(10,20,1,3)
        time.sleep(5)

        self.addnew.setSave()
        time.sleep(5)





