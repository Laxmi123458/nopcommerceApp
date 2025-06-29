import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class AddCustomer:
    #Add customer page
    lnkcustomers_menu_xpath="//div[@class='content-header']"
    lnkcustomers_menuitems_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath="//a[normalize-space()='Add new']"

    txtEmail_xpath="//input[@id='Email']" #locators
    txtPassword_xpath="//input[@id='Password']"
    txtFirstName_xpath="//input[@id='FirstName']"
    txtLastName_xpath="//input[@id='LastName']"
    rdMaleGender_xpath="//input[@id='Gender_Male']"
    rdFeMaleGender_xpath="//input[@id='Gender_Female']"
    txtCompanyName_xapth="//input[@id='Company']"
    cbIsTaxExempt_xapth="//input[@id='Company']"
    txtNewsLetter_xpath="//input[@role='searchbox']"
    txtCustomerRoles_xapth="//span[@aria-expanded='true']//input[@role='searchbox']"
    lstitemAdministrators_xapth="//li[@title='Administrators']"
    lstitemForumModerators_xapth="//li[@title='Forum Moderators']"
    lstitemRegistered_xpath="//li[@title='Registered']"
    lstitemGuests_xpath="//li[@title='Guests']"
    lstitemVendors_xpath="//li[@title='Vendors']"
    drpManagerOfVendor_xpath="//select[@id='VendorId']"
    cbActive_xapth="//input[@id='Active']"
    cbCustomerMustChangePassword_xpath="//input[@id='MustChangePassword']"
    txtAdminComment_xpath="//textarea[@id='AdminComment']"
    btnSave_xpath="//button[@name='save']"

    def __init__(self,driver): #constructor - will get the driver from actual test case and intiate the local driver and now this driver belongs to class so we have to access the driver by using self keyword
        self.driver=driver

    def clickOnCustomersMenu(self): #actionmethod
        self.driver.find_element(By.XPATH, self.lnkcustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self): #actionmethod
        element = self.driver.find_element(By.XPATH, self.lnkcustomers_menuitems_xpath)
        self.driver.execute_script("arguments[0].click();", element)

    def clickOnAddnew(self): #actionmethod
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self, email): #actionmethod
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password): #actionmethod
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setFirstName(self, fname): #actionmethod
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname): #actionmethod
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def setGender(self, gender): #actionmethod
        if gender=="male":
            self.driver.find_element(By.XPATH, self.rdMaleGender_xpath).click()
        elif gender=="female":
            self.driver.find_element(By.XPATH, self.rdFeMaleGender_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rdMaleGender_xpath).click()

    def setCompanyName(self,comname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xapth).send_keys(comname)

    def setIsTaxExempt(self):
        self.driver.find_element(By.XPATH, self.cbIsTaxExempt_xapth).click()

    def setNewsletter(self, newsletter):
        self.driver.find_element(By.XPATH, self. txtNewsLetter_xpath).send_keys(newsletter)
        self.driver.find_element(By.XPATH, self. txtNewsLetter_xpath).submit()

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH,"//span[@role='presentation']").click()
        drp = self.driver.find_element(By.XPATH, "//span[@aria-expanded='true']//input[@role='searchbox']")
        drp.send_keys(role)
        time.sleep(2)
        role_xpath = f"//li[contains(text(), '{role}')]"
        self.driver.find_element(By.XPATH, role_xpath).click()
        time.sleep(1)
        drp.clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//body").click()
        time.sleep(1)

    def setManagerOfVendor(self, value):
        self.driver.find_element(By.XPATH, self.drpManagerOfVendor_xpath).click()
        time.sleep(3)
        drp=Select(self.driver.find_element(By.XPATH, "//select[@id='VendorId']"))
        drp.select_by_visible_text(value)

    def setActive(self):
        self.driver.find_element(By.XPATH, self.cbActive_xapth).click()

    def setCustomerMustChangePassword(self):
        self.driver.find_element(By.XPATH, self.cbCustomerMustChangePassword_xpath).click()

    def setAdminComment(self,content):
        self.driver.find_element(By.XPATH, self.txtAdminComment_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()
        time.sleep(5)