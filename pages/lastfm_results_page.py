from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ResultsPageLastFm(BasePage):
    ARTIST_LINK = (By.CLASS_NAME, "link-block-target")
   
    def click_artist_link(self):
        self.click(self.ARTIST_LINK)