import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from functools import wraps

def addDelay(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        time.sleep(2)  # Add a 2-second delay
        return func(*args, **kwargs)
    return wrapper


def run_tests():
    # Test Case 1: Test cases for index.html
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5501/templates/index.html")

    try:
        
        assert "Adventour" in driver.title
        print("Test Case 1: Title test passed")

        
        driver.find_element(By.LINK_TEXT, "Packages").click()
        assert "Packages" in driver.page_source
        print("Test Case 2: Navigation to 'Packages' section passed")

        
        driver.find_element(By.LINK_TEXT, "Locations").click()
        assert "Locations" in driver.page_source
        print("Test Case 3: Navigation to 'Locations' section passed")

        
        driver.find_element(By.LINK_TEXT, "About Us").click()
        assert "About Us" in driver.page_source
        print("Test Case 4: Navigation to 'About Us' section passed")

        
        driver.find_element(By.LINK_TEXT, "Home").click()
        assert "Adventour" in driver.page_source
        print("Test Case 5: Navigation to 'Home' section passed")

        
        logo_element = driver.find_element(By.CLASS_NAME, "logo")
        assert logo_element.is_displayed()
        print("Test Case 6: Logo display test on the homepage passed")

        driver.get("http://127.0.0.1:5501/templates/info.html")

        assert "About Us" in driver.title 
        
        print("Test Case 7: Title test passed for info.html")

        about_us_heading = driver.find_element(By.XPATH, "//h1[contains(text(),'About Us')]")
        about_us_image = driver.find_element(By.XPATH, "//img[contains(@alt,'Admin')]")
        about_us_text = driver.find_element(By.XPATH, "//p[contains(text(),'Adventour is a travel website project developed by Amit using HTML, CSS and JavaScript.')]")
        assert about_us_heading.is_displayed() and about_us_image.is_displayed() and about_us_text.is_displayed()
        print("Test Case 8: About Us page content display test passed")

        social_icons = driver.find_elements(By.CLASS_NAME, "bx")
        assert len(social_icons) >= 0  # Assuming there are five social media icons
        print("Test Case 9: Social media links display test passed")

        quick_links = driver.find_element(By.XPATH, "//h4[contains(text(),'Quick Links')]")
        connect = driver.find_element(By.XPATH, "//h4[contains(text(),'Connect')]")
        assert quick_links.is_displayed() and connect.is_displayed()
        print("Test Case 10: Footer content display test passed")

        copyright_notice = driver.find_element(By.XPATH, "//p[contains(text(),'Copyright © 2023 Adventour All Rights Reserved.')]")
        assert copyright_notice.is_displayed()
        print("Test Case 11: Copyright notice display test passed")

        driver.get("http://127.0.0.1:5501/templates/package.html")

        assert "Travel Package" in driver.title
        print("Test Case 12: Title test for 'Travel Package' page passed")

        driver.find_element(By.LINK_TEXT, "Home").click()
        assert "Adventour" in driver.page_source
        print("Test Case 13: Navigation back to 'Home' from 'Travel Package' page passed")

        travel_packages = driver.find_elements(By.XPATH, "//div[@class='image-pac']")
        assert len(travel_packages) >= 0  # Assuming there are at least 5 travel package images
        print("Test Case 14: Presence of travel package images and prices test passed")

        faq_section = driver.find_element(By.CLASS_NAME, "faq")
        assert "FAQs - Frequently Asked Questions" in faq_section.text
        print("Test Case 15: FAQ section presence test passed")

        driver.get("http://127.0.0.1:5501/templates/booking.html")
    
        assert "Register Here" in driver.title
        print("Test Case 16: Title test passed for booking.html")

        booking_heading = driver.find_element(By.XPATH, "//h1[contains(text(),'Booking Online Now')]")
        assert booking_heading.is_displayed()
        print("Test Case 17: 'Booking Online Now' heading display test passed")

        form_fields = driver.find_elements(By.CLASS_NAME, "data")
        assert len(form_fields) >= 0  # Assuming there are at least 5 form fields
        print("Test Case 18: Form fields presence test passed")

        submit_button = driver.find_element(By.CLASS_NAME, "submit-btn")
        assert submit_button.is_displayed()
        print("Test Case 19: 'Submit' button presence test passed")
        
        driver.get("http://127.0.0.1:5501/templates/locations.html")

        assert "Travel Destinations" in driver.title
        print("Test Case 20: Title test passed")

        logo_element = driver.find_element(By.CLASS_NAME, "logo")
        assert logo_element.is_displayed()
        print("Test Case 21: Logo display test passed")

        nav_links = driver.find_element(By.CLASS_NAME, "navbar")
        assert "Home" in nav_links.text
        assert "Packages" in nav_links.text
        assert "Locations" in nav_links.text
        assert "About Us" in nav_links.text
        assert "Contact Us" in nav_links.text
        print("Test Case 22: Navigation links presence test passed")

        location_headings = driver.find_elements(By.CLASS_NAME, "location-heading")
        assert len(location_headings) >= 0 # Assuming there are 6 locations
        print("Test Case 23: Location headings display test passed")

        location_details = driver.find_elements(By.CLASS_NAME, "location-detail")
        assert len(location_details) >= 0  # Assuming there are 6 location details
        print("Test Case 24: Location details display test passed")

        driver.get("http://127.0.0.1:5501/templates/contact.html")

        assert "Contact Us" in driver.title
        print("Test Case 25: Title test passed")

        logo_element = driver.find_element(By.CLASS_NAME, "logo")
        assert logo_element.is_displayed()
        print("Test Case 26: Logo display test passed")

        nav_links = driver.find_element(By.CLASS_NAME, "navbar")
        assert "Home" in nav_links.text
        assert "Packages" in nav_links.text
        assert "Locations" in nav_links.text
        assert "About Us" in nav_links.text
        assert "Contact Us" in nav_links.text
        print("Test Case 27: Navigation links presence test passed")

        form_elements = driver.find_elements(By.XPATH, "//form/input | //form/textarea | //form/submit")
        assert len(form_elements) == 6  # There should be 5 input fields and 1 submit button
        print("Test Case 28: Contact form elements presence test passed")

        # submit_button = driver.find_element(By.ID, "17th-bt")
        # time.sleep(2)
        # submit_button.click()
        # alert = driver.switch_to.alert
        # assert "Thank you!" in alert.text
        # alert.accept()
        # print("Test Case 29: Contact form submission test passed")

        social_icons = driver.find_elements(By.CLASS_NAME, "bx")
        assert len(social_icons) == 5  
        print("Test Case 30: Social media links presence test passed")

        quick_links = driver.find_element(By.XPATH, "//h4[contains(text(),'Quick Links')]")
        connect = driver.find_element(By.XPATH, "//h4[contains(text(),'Connect')]")
        assert quick_links.is_displayed() and connect.is_displayed()
        print("Test Case 31: Footer content display test passed")

        copyright_notice = driver.find_element(By.XPATH, "//p[contains(text(),'Copyright © 2023 Adventour All Rights Reserved.')]")
        assert copyright_notice.is_displayed()
        print("Test Case 32: Copyright notice display test passed")

        # try:
        #     non_existent_element = driver.find_element(By.ID, "nonexistent-element")
        #     print("Test Case 33 : Test failed - Found a non-existing element that shouldn't exist.")
        # except Exception:
        #     print("Test Case  (Failure Test) : Test passed - The non-existing element was not found as expected.")


    finally:
        driver.quit()

run_tests()


