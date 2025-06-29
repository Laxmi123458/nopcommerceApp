import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username= ReadConfig.getUseremail()
    password= ReadConfig.getPassword()

    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):  #method
        self.logger.info("Test_001_Login")
        self.logger.info("Verifying Home page title")
        self.driver=setup #Launch the driver
        self.driver.get(self.baseURL) #Launchthe site
        act_title=self.driver.title
        if act_title=="nopCommerce demo store. Login":
            assert True
            print('Here')
            self.logger.info("Home page title is passed")
        else:
            print('else')
            self.driver.save_screenshot(".\\Screenshots\\test_homePageTitle.png")
            self.driver.close()
            self.logger.error("Home page title is failed")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self,setup):  #method
        self.logger.info("Verifying Login test")
        self.driver=setup #Launch the driver
        self.driver.get(self.baseURL) #Launchthe site
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        time.sleep(3)
        self.lp.clickLogin() #Login
        time.sleep(3)
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            time.sleep(3)
            self.lp.clickLogout()
            assert True
            self.logger.info("Login test is passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_Login.png")
            self.driver.close()
            self.logger.error("Login test is failed")
            assert False




