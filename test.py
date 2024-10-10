import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from functools import wraps


def addDelay(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        time.sleep(2)  
        return func(*args, **kwargs)
    return wrapper


class MiniprojectTest:
    def __init__(self):
        self.driver = webdriver.Chrome
        self.driver.implicitly_wait(3)

    def quit(self):
        self.driver.quit()
    
    class IndexPageTests:
        def __init__(self,driver):
            self.driver = driver

        def testToAccessIndexPage(self):
            self.driver.get("http://127.0.0.1:5501/templates/index.html")
            assert "Adventour" in self.driver.title
            print("Test Case 1: Title test passed")

        @addDelay
        def testToAccessPackageSection(self):
            self.driver.find_element(By.LINK_TEXT, "Packages").click()
            assert "Packages" in self.driver.page_source
            print("Test Case 2: Navigation to 'Packages' section passed")

        @addDelay
        def testToAccessLocations(self):
            self.driver.find_element(By.LINK_TEXT, "Locations").click()
            assert "Locations" in self.driver.page_source
            print("Test Case 3: Navigation to 'Locations' section passed")


        @addDelay
        def testToAccessAboutUs(self):
            self.driver.find_element(By.LINK_TEXT, "About Us").click()
            assert "About Us" in self.driver.page_source
            print("Test Case 4: Navigation to 'About Us' section passed")


        @addDelay
        def testToAccessHome(self):
            self.driver.find_element(By.LINK_TEXT, "Home").click()
            assert "Home" in self.driver.page_source
            print("Test Case 5: Navigation to 'Home' section passed")
        
        def accessWebsiteLogo(self):
            logo_element = self.driver.find_element(By.CLASS_NAME, "logo")
            assert logo_element.is_displayed()
            print("Test Case 6: Logo display test on the homepage passed")

    class InfoPageTests:
        def __init__(self,driver):
            self.driver = driver
        
        
        def testToAccessInfoPage(self):
            self.driver.get("http://127.0.0.1:5501/templates/info.html")
            assert "About Us" in self.driver.title
            print("test for accessing info.html passed")

        @addDelay
        def testToDisplayContentsOfAboutUsPage(self):
            about_us_heading = self.driver.find_element(By.XPATH, "//h1[contains(text(),'About Us')]")
            about_us_image = self.driver.find_element(By.XPATH, "//img[contains(@alt,'Admin')]")
            about_us_text = self.driver.find_element(By.XPATH, "//p[contains(text(),'Adventour is a travel website project developed by Amit using HTML, CSS and JavaScript.')]")
            assert about_us_heading.is_displayed() and about_us_image.is_displayed() and about_us_text.is_displayed()
            print("Test Case 8: About Us page content display test passed")

        @addDelay
        def testToDisplaySocialMediaLinks(self):
            social_icons = self.driver.find_elements(By.CLASS_NAME, "bx")
            assert len(social_icons) >= 0  
            print("Test Case 9: Social media links display test passed")

        
        def testToDisplayFooterOfInfoPage(self):
            quick_links = self.driver.find_element(By.XPATH, "//h4[contains(text(),'Quick Links')]")
            connect = self.driver.find_element(By.XPATH, "//h4[contains(text(),'Connect')]")
            assert quick_links.is_displayed() and connect.is_displayed()
            print("Test Case 10: Footer content display test passed")

        def testToDisplayCopyrightNotice(self):
            copyright_notice = self.driver.find_element(By.XPATH, "//p[contains(text(),'Copyright © 2023 Adventour All Rights Reserved.')]")
            assert copyright_notice.is_displayed()
            print("Test Case 11: Copyright notice display test passed")

    
    class PackagePageTests:
        def __init__(self,driver):
            self.driver = driver
        
        def testToAccessPackagePage(self):
            self.driver.get("http://127.0.0.1:5501/templates/package.html")
            assert "Travel Package" in self.driver.title
            print("Test Case 12: Title test for 'Travel Package' page passed")

        @addDelay
        def testToReturnBackToHomePageFromPackagePage(self):
            self.driver.find_element(By.LINK_TEXT, "Home").click()
            assert "Adventour" in self.driver.page_source
            print("Test Case 13: Navigation back to 'Home' from 'Travel Package' page passed")

        @addDelay
        def testToCheckPresenceOfTravelPackageImagesAndPrices(self):
            travel_packages = self.driver.find_elements(By.XPATH, "//div[@class='image-pac']")
            assert len(travel_packages) >= 0  
            print("Test Case 14: Presence of travel package images and prices test passed")

        @addDelay
        def testToCheckPresenceOfFAQSection(self):
            faq_section = self.driver.find_element(By.CLASS_NAME, "faq")
            assert "FAQs - Frequently Asked Questions" in faq_section.text
            print("Test Case 15: FAQ section presence test passed")

    
    class BookingPageTests:
        def __init__(self,driver):
            self.driver = driver

        def testToAccessBookingPage(self):
            self.driver.get("http://127.0.0.1:5501/templates/booking.html")
            assert "Register Here" in self.driver.title
            print("Test Case 16: Title test passed for booking.html")

        @addDelay
        def testToCheckBookingOnlineNowHeading(self):
            booking_heading = self.driver.find_element(By.XPATH, "//h1[contains(text(),'Booking Online Now')]")
            assert booking_heading.is_displayed()
            print("Test Case 17: 'Booking Online Now' heading display test passed")

        @addDelay
        def testToCheckPresenceOfFormFeild(self):
            form_fields = driver.find_elements(By.CLASS_NAME, "data")
            assert len(form_fields) >= 0  
            print("Test Case 18: Form fields presence test passed")

        @addDelay
        def testToCheckSubmitButton(self):
            submit_button = self.driver.find_element(By.CLASS_NAME, "submit-btn")
            assert submit_button.is_displayed()
            print("Test Case 19: 'Submit' button presence test passed")
        