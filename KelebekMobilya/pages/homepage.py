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

    #Üst menüleri görüntüleme
    def view_top_menus(self):
        self.driver.get("https://www.kelebek.com/")
        sitting_room=self.WaitForElementVisible(SITTINGROOM)
        actions = ActionChains(self.driver)
        actions.move_to_element(sitting_room).perform()
        tv_unit=self.WaitForElementVisible(TVUNIT)
        actions = ActionChains(self.driver)
        actions.move_to_element(tv_unit).perform()
        dining_room=self.WaitForElementVisible(DININGROOM)
        actions = ActionChains(self.driver)
        actions.move_to_element(dining_room).perform()
        bedroom=self.WaitForElementVisible(BEDROOM)
        actions = ActionChains(self.driver)
        actions.move_to_element(bedroom).perform()
        kelebek_kids=self.WaitForElementVisible(KELEBEKKIDS)
        actions = ActionChains(self.driver)
        actions.move_to_element(kelebek_kids).perform()
        kelebek_decor=self.WaitForElementVisible(KELEBEKDECOR)
        actions = ActionChains(self.driver)
        actions.move_to_element(kelebek_decor).perform()
        kelebek_garden=self.WaitForElementVisible(KELEBEKGARDEN)
        actions = ActionChains(self.driver)
        actions.move_to_element(kelebek_garden).perform()
        home_office=self.WaitForElementVisible(HOMEOFFICE)
        actions = ActionChains(self.driver)
        actions.move_to_element(home_office).perform()

       #sayfaları sağa sola kaydırma 
    def scrolling_pages_left_and_right(self):
        self.driver.get("https://www.kelebek.com/")
        swipe_right=self.WaitForElementVisible(SWİPE_RİGHT)   
        # 15 kez sağa kaydırma
        for _ in range(15):
           swipe_right.send_keys(Keys.RIGHT)
           time.sleep(0.5)  # Her kaydırmadan sonra 0.5 saniye bekle
        swipe_left=self.WaitForElementVisible(SWİPE_LEFT)  
        # 15 kez sola kaydırma
        for _ in range(15):
           swipe_left.send_keys(Keys.LEFT)
           time.sleep(0.5)  # Her kaydırmadan sonra 0.5 saniye bekle 



