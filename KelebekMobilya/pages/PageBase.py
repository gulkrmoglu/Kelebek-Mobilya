from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class PageBase:

    def __init__(self,driver):
        self.driver=driver

    def WaitForElementVisible(self,locator,timeout=40):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator)) 
    
    def clickElementByJS(self,element):
        self.driver.execute_script("arguments[0].click();", element)  

