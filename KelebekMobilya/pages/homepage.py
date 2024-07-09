from KelebekMobilya.pages.constants.globalConstants import *
from KelebekMobilya.pages.PageBase import PageBase
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class HomePage(PageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def homepage_scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def view_top_menus(self):
        self.driver.get("https://www.kelebek.com/")
        menu_items = [SITTINGROOM, TVUNIT, DININGROOM, BEDROOM, KELEBEKKIDS, KELEBEKDECOR, KELEBEKGARDEN, HOMEOFFICE, LOVAYATAK]
        actions = ActionChains(self.driver)
        
        for oge in menu_items:
            element = self.WaitForElementVisible(oge)
            actions.move_to_element(element).perform()
            time.sleep(0.5) 

    def scrolling_pages_left_and_right(self):
        self.driver.get("https://www.kelebek.com/")
        swipe_rigth = self.WaitForElementVisible(SWIPE_RIGHT)
        swipe_left = self.WaitForElementVisible(SWIPE_LEFT)
        
        self._scroll_page(swipe_rigth, Keys.RIGHT, 15)
        self._scroll_page(swipe_left, Keys.LEFT, 15)
    
    def _scroll_page(self, element, yon, tekrar):
        for _ in range(tekrar):
            element.send_keys(yon)
            time.sleep(0.5) 

