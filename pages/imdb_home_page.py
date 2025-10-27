from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ImdbHomePage(BasePage):
    SEARCH_ICON = (By.CLASS_NAME, "searchform__inputContainer")
    SEARCH_INPUT = (By.ID, "suggestion-search")
    SEARCH_BUTTON = (By.ID, "suggestion-search-button")
    
    def search_movie(self, movie_name):
        self.click(self.SEARCH_ICON)
        self.enter_text(self.SEARCH_INPUT, movie_name)
        self.click(self.SEARCH_BUTTON) 