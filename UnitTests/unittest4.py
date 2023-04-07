from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import unittest
from faker import Faker
import time

faker_class = Faker()


class ChromeForm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_chrome_1120x550(self):
        driver = self.driver
        driver.set_window_size(1120, 550)
        driver.get("https://qasvus.wordpress.com")
        wait = WebDriverWait(driver, 3)
        time.sleep(3)

        # making sure that we are on the right page
        assert "California Real Estate" in driver.title
        print("Driver title in Chrome is:", driver.title)

        # accepting cookies
        try:
            wait.until(
                EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@style, 'display: flex')]")))
            print("the iframe is found")
            driver.find_element(By.CSS_SELECTOR, ".is-primary").click()
            driver.switch_to.default_content()
        except TimeoutException:
            print("there is no iframe with cookies found")

        # closing an advert
        try:
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((
                    By.CSS_SELECTOR, ".bottom-sticky__ad-close-btn"))).click()
            print("the advert is found")
        except TimeoutException:
            print("there is no advert found")

        # finding the form
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Submit')]")))
        wait.until(EC.visibility_of_element_located((By.ID, "contact-form-comment-g2-message")))

        # completing the form
        driver.find_element(By.ID, 'g2-name')
        name = driver.find_element(By.ID, 'g2-name')
        name.clear()
        name.send_keys(faker_class.name())

        driver.find_element(By.NAME, 'g2-email')
        email = driver.find_element(By.ID, 'g2-email')
        email.clear()
        email.send_keys(faker_class.email())

        driver.find_element(By.ID, 'contact-form-comment-g2-message')
        message = driver.find_element(By.ID, 'contact-form-comment-g2-message')
        message.clear()
        message.send_keys(faker_class.text())

        driver.find_element(By.CLASS_NAME, 'pushbutton-wide').send_keys('\n')
        time.sleep(2)

        # thank you page
        # making sure that we are on the right page
        # going to the homepage
        try:
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((
                    By.XPATH, "//a[contains(text(),'Go back')]"))).click()
            print("California Real Estate Page is ready!")
            driver.get_screenshot_as_file('ScreenshotCalifornia_page.png')
        except TimeoutException:
            print(
                "Can't find Element by src='https://qasvus.wordpress.com/?contact-form-hash"
                "=870c9c4c3793ec33a9fbd94db1a03cdcd56c1036'")
            driver.get_screenshot_as_file('California_page_loading_error.png')

        # homepage
        # making sure that we are on the right page

        assert "California Real Estate" in driver.title
        print("Page has", driver.title + "as Page title")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-55 size-full"]')))
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-34 size-full"]')))
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-56 size-full"]')))
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-30 size-full"]')))
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


class EdgeForm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()

    def test_edge_1250x850(self):
        driver = self.driver
        driver.set_window_size(1250, 850)
        driver.get("https://qasvus.wordpress.com")
        wait = WebDriverWait(driver, 3)
        time.sleep(3)

        # making sure that we are on the right page
        assert "California Real Estate" in driver.title
        print("Driver title in Chrome is:", driver.title)

        # accepting cookies
        try:
            wait.until(
                EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@style, 'display: flex')]")))
            print("the iframe is found")
            driver.find_element(By.CSS_SELECTOR, ".is-primary").click()
            driver.switch_to.default_content()
        except TimeoutException:
            print("there is no iframe with cookies found")

        # closing an advert
        try:
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((
                    By.CSS_SELECTOR, ".bottom-sticky__ad-close-btn"))).click()
            print("the advert is found")
        except TimeoutException:
            print("there is no advert found")

        # finding the form
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Submit')]")))
        wait.until(EC.visibility_of_element_located((By.ID, "contact-form-comment-g2-message")))

        # completing the form
        driver.find_element(By.ID, 'g2-name')
        name = driver.find_element(By.ID, 'g2-name')
        name.clear()
        name.send_keys(faker_class.name())

        driver.find_element(By.NAME, 'g2-email')
        email = driver.find_element(By.ID, 'g2-email')
        email.clear()
        email.send_keys(faker_class.email())

        driver.find_element(By.ID, 'contact-form-comment-g2-message')
        message = driver.find_element(By.ID, 'contact-form-comment-g2-message')
        message.clear()
        message.send_keys(faker_class.text())

        driver.find_element(By.CLASS_NAME, 'pushbutton-wide').send_keys('\n')
        time.sleep(2)

        # thank you page
        # making sure that we are on the right page
        # going to the homepage
        try:
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((
                    By.XPATH, "//a[contains(text(),'Go back')]"))).click()
            print("California Real Estate Page is ready!")
            driver.get_screenshot_as_file('ScreenshotCalifornia_page.png')
        except TimeoutException:
            print(
                "Can't find Element by src='https://qasvus.wordpress.com/?contact-form-hash"
                "=870c9c4c3793ec33a9fbd94db1a03cdcd56c1036'")
            driver.get_screenshot_as_file('California_page_loading_error.png')

        # homepage
        # making sure that we are on the right page

        assert "California Real Estate" in driver.title
        print("Page has", driver.title + "as Page title")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-55 size-full"]')))
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-34 size-full"]')))
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-56 size-full"]')))
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class="wp-image-30 size-full"]')))
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()
