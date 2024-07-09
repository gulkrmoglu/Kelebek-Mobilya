from selenium import webdriver
import pytest
from KelebekMobilya.pages.homepage import HomePage


@pytest.mark.usefixtures("setup")
class TestHomePage:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.homepage= HomePage(self.driver)

    def test_homepage(self):
        self.homepage.homepage_scroll()
        self.homepage.view_top_menus()
        self.homepage.scrolling_pages_left_and_right()
       
       