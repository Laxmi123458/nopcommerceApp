import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path=".//TestData/LoginData.xlsx"

    logger=LogGen.loggen()

    # def test_homePageTitle(self,setup):  #method
    #     self.logger.info("Test_001_Login")
    #     self.logger.info("Verifying Home page title")
    #     self.driver=setup #Launch the driver
    #     self.driver.get(self.baseURL) #Launchthe site
    #     act_title=self.driver.title
    #     if act_title=="nopCommerce demo store. Login":
    #         assert True
    #         print('Here')
    #         self.logger.info("Home page title is passed")
    #     else:
    #         print('else')
    #         self.driver.save_screenshot(".\\Screenshots\\test_homePageTitle.png")
    #         self.driver.close()
    #         self.logger.error("Home page title is failed")
    #         assert False

    @pytest.mark.regression
    def test_Login_ddt(self, setup):
        self.logger.info("Test_0012_DDT_Login")
        self.logger.info("Verifying Login test")
        self.driver = setup  # Launch the driver
        self.driver.get(self.baseURL)  # Launch the site

        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows in a excel", self.rows)

        lst_status = []  # empty list
        for r in range(2, self.rows + 1):
            # Read data from Excel
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            # Clear the fields before entering new data
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)

            # Click the Login button
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("Test is passed")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("Test is failed")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("failed")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("Passed")
                    lst_status.append("Pass")

        # After the loop finishes, check if there were any failures
        if "Fail" not in lst_status:
            self.logger.info("Login DDT test passed")
            assert True
        else:
            self.logger.info("Login DDT test failed")
            assert False

        self.driver.close()  # Close the driver after the whole test finishes
        self.logger.info("End of Login DDT Test")
        self.logger.info("Completed TC_LoginDDT_002")