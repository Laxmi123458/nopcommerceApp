import time

import driver
import self
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium import webdriver

class AddnewProduct:
    lnkcatalog_menu_xpath = "//body/div[@class='wrapper']/aside[@class='main-sidebar sidebar-dark-primary elevation-4']/div[@class='sidebar']/nav[@class='mt-2']/ul[@role='menu']/li[2]/a[1]"
    lnkcatalog_menuitems_xpath = "//a[@href='/Admin/Product/List']"
    btnAddnew_xpath = "//a[normalize-space()='Add new']"

    txtProductname_xpath = "//input[@id='Name']"
    txtShortdescription_xpath = "//textarea[@id='ShortDescription']"
    txtFulldescription = "//textarea[@id='FullDescription']"
    txtSku_xpath = "//input[@id='Sku']"
    txtCategorices_xpath = "//span[@class='select2 select2-container select2-container--default select2-container--focus select2-container--below']//input[@role='searchbox']"


    drpPrice_xpath = "//input[@id='Price']"
    chkTaxexempt_xpath = "//input[@id='IsTaxExempt']"
    drpTaxcategory_xpath = "//select[@id='TaxCategoryId']"

    chkShippingenabled_xpath = "//input[@id='IsShipEnabled']"
    drpWeight_xpath = "//input[@id='Weight']"
    drpLength_xpath = "//input[@id='Length']"
    drpWidth_xpath = "//input[@id='Width']"
    drpHeight_xpath = "//input[@id='Height']"

    btnSave_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver= driver

    def clickOnCatalogMenu(self):
        self.driver.find_element(By.XPATH, self.lnkcatalog_menu_xpath).click()

    def clickOnCatalogMenuItems(self):
        self.driver.find_element(By.XPATH, self.lnkcatalog_menuitems_xpath).click()

    def clickOnAddNewButton(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()


    def setProductName(self, prdname):
        self.driver.find_element(By.XPATH, self.txtProductname_xpath).send_keys(prdname)

    def setShortDescription(self, shrtdescr):
        self.driver.find_element(By.XPATH, self.txtShortdescription_xpath).send_keys(shrtdescr)

    def setFullDescription(self, fulldescr):
        iframe = self.driver.find_element(By.CSS_SELECTOR, "iframe.tox-edit-area__iframe")
        self.driver.switch_to.frame(iframe)
        # Wait for the FullDescription text area to be available inside the iframe
        full_description_element = self.driver.find_element(By.XPATH, '//*[@id="tinymce"]/p')

        # Interact with the text area
        full_description_element.click()
        full_description_element.clear()
        full_description_element.send_keys(fulldescr)
        self.driver.switch_to.default_content()

        # Click an element outside the editor (e.g., label or container div)
        outside_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//body/div[@class='wrapper']/div[@class='content-wrapper']/form[@id='product-form']/section[@class='content']/div[@class='container-fluid']/div[@class='form-horizontal']/nop-cards[@id='product-cards']/nop-card/div[@id='product-info']/div[@class='card-body']/div[@id='product-details-area']/div[@class='form-group row']/div[1]"))  # Adjust as needed
        )
        outside_element.click()
        time.sleep(5)

    def settxtSku(self, txtsku):
        sku = self.driver.find_element(By.XPATH, self.txtSku_xpath)
        sku.send_keys(txtsku)

    #def setCategories(self, value):
        #search_field = self.driver.find_element(By.XPATH, self.txtCategorices_xpath)
        #search_field.send_keys(value)

        #wait for the specific category to appear
        #WebDriverWait(self.driver, 10).until(
            #EC.presence_of_element_located((By.XPATH, "//li[@title='Computers']"))
        #)
        #catg= Select(self.driver.find_element(By.XPATH, "//li[@title='Computers']" ))
        #catg.click()

    def setPrice(self, pno):
        self.driver.find_element(By.XPATH, self.drpPrice_xpath).clear()
        self.driver.find_element(By.XPATH, self.drpPrice_xpath).send_keys(pno)

    def setTaxExempt(self):
        self.driver.find_element(By.XPATH, self.chkTaxexempt_xpath).click()

    def setShipping(self):
        checkbox=self.driver.find_element(By.XPATH, self.chkShippingenabled_xpath)
        if not checkbox.is_selected():
            checkbox.click()

    def setDimensions(self, weight, length, width, height):
        self.driver.find_element(By.XPATH, self.drpWeight_xpath).clear()
        self.driver.find_element(By.XPATH, self.drpWeight_xpath).send_keys(weight)
        self.driver.find_element(By.XPATH, self.drpLength_xpath).clear()
        self.driver.find_element(By.XPATH, self.drpLength_xpath).send_keys(length)
        self.driver.find_element(By.XPATH, self.drpWidth_xpath).clear()
        self.driver.find_element(By.XPATH, self.drpWidth_xpath).send_keys(width)
        self.driver.find_element(By.XPATH, self.drpHeight_xpath).clear()
        self.driver.find_element(By.XPATH, self.drpHeight_xpath).send_keys(height)

    def setSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()
















