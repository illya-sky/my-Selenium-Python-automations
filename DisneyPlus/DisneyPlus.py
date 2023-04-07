from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://google.com")
driver.maximize_window()
wait = WebDriverWait(driver, 3)

# wait max 5 sec for page loading, then show "Load Error"
# implicitly_wait() is using for all other browsers
driver.implicitly_wait(5)

# cookies acceptation
try:
    driver.find_element(By.ID, 'W0wltc').click()
    time.sleep(2)
except NoSuchElementException:
    print("There is no cookie acceptance")

# this method is depreciated in Selenium4
# driver.find_element_by_name("q").send_keys("disney plus")
driver.find_element(By.NAME, "q").send_keys("disney plus")

print(driver.find_element(By.TAG_NAME, "img").get_attribute("src"))  # Google logo image
# Same code, but with XPath locator
print(driver.find_element(By.XPATH, '//*[@alt="Google"]').get_attribute("src"))  # Google logo image
# print(driver.find_element(By.XPATH, '//*[@alt="2022 World Cup"]').get_attribute("src"))  # Google logo image

print(driver.find_element(By.NAME, "btnK").get_attribute("value"))  # Google button value
print(driver.find_element(By.NAME, "btnI").get_attribute("value"))  # Google second button value

# Find element value, then store this value to variable "btnk"
btnk = driver.find_element(By.NAME, "btnK").get_attribute("value")

# Same element verification for "Google Search" button
if btnk == "Поиск в Google":
    print("Your browser's language is Russian")
elif btnk == "Szukaj w Google":
    print("Your browser's language is Polish")
else:
    print("Your browser's language is probably English")

driver.find_element(By.NAME, "btnK").click()
driver.back()
driver.find_element(By.NAME, "q").send_keys("disney plus")
# or just hit Enter on the Keyboard, code is below:
driver.find_element(By.NAME, "btnK").submit()

# Find and click on the DisneyPlus link
driver.find_element(By.PARTIAL_LINK_TEXT, "Disney Plus").click()

# cookies on the page
try:
    driver.find_element(By.ID, "onetrust-reject-all-handler").click()
except NoSuchElementException:
    print("there is no cookie")

assert "Stream Disney, Pixar, Marvel, Star Wars, Nat Geo | Disney+" in driver.title
print("Disney Plus Page Title is: ", driver.title)

# Not common use
if "Stream Disney, Pixar, Marvel, Star Wars, Nat Geo | Disney+" not in driver.title:
    raise Exception("Title for Disney Plus page is wrong!")

# wait max 5 sec for page loading, then show "Load Error"
# set_page_load_timeout() is using for Chrome and FireFox mostly
driver.set_page_load_timeout(5)
driver.find_element(By.LINK_TEXT, "LOG IN").click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@data-testid="responsive-logo"]')
driver.find_element(By.XPATH, "//span[contains(text(),'TRENDING')]").click()
time.sleep(0.5)
# Find "New on Disney" and "Coming Soon" links by yourself


# First Card Text and Price verification
driver.find_element(By.XPATH, "//p[contains(text(),'Thousands of movies and shows ')]")
driver.find_element(By.XPATH, "//span[contains(text(),'$7.99')]")

# Complete Text and Price verification for the second Card by yourself

# Third Card Text and Price verification
driver.find_element(By.XPATH, "//span[contains(text(),'Includes Hulu (No Ads)')]")
driver.find_element(By.XPATH, "//span[contains(text(),'$19.99')]")

# Button 1 click
driver.find_element(By.XPATH, "//span[contains(text(),'GET DISNEY+')]").click()
time.sleep(3)

# Basic Page verification
titleBasicPlanPage = "Sign up | Disney+"
assert titleBasicPlanPage in driver.title
driver.find_element(By.ID, "nav-logo")
driver.find_element(By.XPATH, "//button[contains(text(),'log in')]")
driver.find_element(By.XPATH, "//h3[contains(text(),'Enter your email')]")
driver.find_element(By.ID, "email")
driver.find_element(By.XPATH, '//span[@class="sc-cHGsZl gaiHCy"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//span[@class="sc-cHGsZl gaiHCy"]').click()
driver.find_element(By.XPATH, "//button[contains(text(),'AGREE & CONTINUE')]").click()
time.sleep(1)
driver.find_element(By.ID, "email__error")

# Go back
# driver.back()
# or code below
driver.find_element(By.ID, "nav-logo").click()

mainPageTitle = "Stream Disney, Pixar, Marvel, Star Wars, Nat Geo | Disney+"
if mainPageTitle == driver.title:
    print("Main Page Title is OK")
else:
    print("Main Page Title is Different")
    driver.save_screenshot("WrongTitleOnTheMainPage.png")

driver.find_element(By.XPATH, '//*[@alt="Disney, Pixar, Marvel, Star Wars, National Geographic Logo"]')
driver.find_element(By.XPATH, "//span[contains(text(),'View All Plan Options')]").click()
time.sleep(0.5)

# Button 2 click
driver.find_element(By.XPATH, '//*[@data-testid="bundle_cta"]').click()
time.sleep(5)

# Advanced Page verification
titleAdvancedPlanPage = "Sign Up | Disney+"
assert titleAdvancedPlanPage in driver.title
# driver.find_element(By.XPATH, '//*[@class="sc-clNaTc kowWZm"]')
driver.find_element(By.XPATH, "//button[contains(text(),'log in')]")
driver.find_element(By.XPATH, "//h3[contains(text(),'Enter your email')]")
driver.find_element(By.ID, "email")
driver.find_element(By.XPATH, '//span[@class="sc-cHGsZl gaiHCy"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//span[@class="sc-cHGsZl gaiHCy"]').click()
driver.find_element(By.XPATH, "//button[contains(text(),'AGREE & CONTINUE')]").click()
time.sleep(1)
driver.find_element(By.ID, "email__error")

# Go back
# driver.back()
driver.find_element(By.ID, 'logo-container').click()

if mainPageTitle == driver.title:
    print("Main Page Title is OK")
else:
    print("Main Page Title is Different")
    driver.save_screenshot("WrongTitleOnTheMainPage.png")

driver.find_element(By.XPATH, '//*[@alt="Disney, Pixar, Marvel, Star Wars, National Geographic Logo"]')
driver.find_element(By.XPATH, "//span[contains(text(),'View All Plan Options')]").click()
time.sleep(0.5)

# Button 3 click and Pro Page verification - Complete by yourself


# Find element value, then store this value to variable "DisneyPageLogo"
DisneyPageLogoURL = driver.find_element(By.XPATH,
                                        '//*[@alt="Disney, Pixar, Marvel, Star Wars, National Geographic Logo"]').get_attribute(
    "src")
baseDisneyLogoURL = "https://cnbl-cdn.bamgrid.com/assets/8349a1f652e69bf1c3685a888092435110056a55e27b4eac3289e10fcb232978/original"
# Assert (compare) stored element value with required value
assert DisneyPageLogoURL == baseDisneyLogoURL

DisneyPlusURL = "https://www.disneyplus.com/"
assert DisneyPlusURL == driver.current_url
if DisneyPlusURL != driver.current_url:
    print("Current 'Disney Plus' URL is different and it is: ", driver.current_url)
else:
    print("Current 'Disney Plus' URL is OK: ", driver.current_url)

# Same element verification for "Disney Plus Page Logo"
DisneyPageLogo = driver.find_element(By.XPATH, '//*[@alt="Disney, Pixar, Marvel, Star Wars, National Geographic Logo"]')
if DisneyPageLogo:
    print("'Disney Plus' Page Logo is OK")
else:
    print("NO 'Disney Plus' Page Logo")

# Complete "Email" field on the Main page verification by yourself, using example above for "DisneyPageLogo"


# Click on invisible on the screen element
# Better to use "ActionChains" - example below - code line 220
page = driver.find_element(By.TAG_NAME, 'html')
page.send_keys(Keys.SPACE)
page.send_keys(Keys.SPACE)
page.send_keys(Keys.SPACE)
page.send_keys(Keys.SPACE)
time.sleep(2)

# First Plus button click and text verification
firstPlusButton = driver.find_element(By.XPATH, "//span[contains(text(),'What is Disney+?')]")
if firstPlusButton:
    firstPlusButton.click()
else:
    page.send_keys(Keys.SPACE)
    firstPlusButton.click()

time.sleep(1)
ButtonOneExpectedText = "Disney+ is the streaming home of Disney, Pixar, Marvel, Star Wars, National Geographic, " \
                        "and more. From new releases to your favorite classics and exclusive Originals, " \
                        "there's something for everyone. "
driver.find_element(By.XPATH, "//p[contains(text(),'Disney+ is the streaming home of Disney, Pixar, Ma')]")
ButtonOneActualText = driver.find_element(By.XPATH, "//p[contains(text(),'Disney+ is the streaming home of Disney, "
                                                    "Pixar, Ma')]").text
if ButtonOneExpectedText == ButtonOneActualText:
    print("Button One Text is OK")
else:
    print("Button One Text is DIFFERENT")
    print(driver.find_element(By.XPATH,
                              "//p[contains(text(),'Disney+ is the streaming home of Disney, Pixar, Ma')]").text)
    driver.get_screenshot_as_file("Button One Different Text.png")
time.sleep(1)

# Second Plus button click and text verification
# Complete this assignment by yourself


secondPlusButton = driver.find_element(By.XPATH, "//span[contains(text(),'How much does Disney+ cost?')]")
if secondPlusButton:
    secondPlusButton.click()
else:
    page.send_keys(Keys.SPACE)
    secondPlusButton.click()

time.sleep(1)
driver.find_element(By.XPATH, "//p[contains(text(),'Access unlimited entertainment with Disney+ for $7')]")
time.sleep(1)

# Third Plus button click and text verification
# Complete this assignment by yourself
# Refer to "ActionChains" description: https://selenium-python.readthedocs.io/api.html
thirdPlusButton = driver.find_element(By.XPATH,
                                      "//p[contains(text(),'With Disney+, you can choose from an always-growin')]")
actions = ActionChains(driver)
actions.move_to_element(thirdPlusButton).perform()
time.sleep(1)
actions.click(thirdPlusButton).perform()

# Alternate choice for WebPage scrolling Down
page.send_keys(Keys.PAGE_DOWN)

time.sleep(1)
driver.find_element(By.XPATH, "//p[contains(text(),'With Disney+, you can choose from an always-growin')]")
thirdPlusButton_pointOne = driver.find_element(By.XPATH, "//p[contains(text(),'New releases and timeless classics')]")
time.sleep(1)

# Third Plus button - Point One text verification
# Complete this assignment by yourself for rest of the points text verification
thirdPlusButton_pointOne_ExpectedText = "New releases and timeless classics"
thirdPlusButton_pointOne_ActualText = driver.find_element(By.XPATH,
                                                          "//p[contains(text(),'New releases and timeless classics')]").text
if thirdPlusButton_pointOne_ExpectedText == thirdPlusButton_pointOne_ActualText:
    print("Button 3 Text - Point 1 is OK")
else:
    print("Button 3 Text - Point 1 is DIFFERENT")
    print(driver.find_element(By.XPATH,
                              "//p[contains(text(),'Disney+ is the streaming home of Disney, Pixar, Ma')]").text)
    driver.get_screenshot_as_file("Button 3 Text - Point 1 Different Text.png")
time.sleep(1)

# quit from browser
driver.quit()

# closing browser tab if you need to close just one Tab, but not the entire Browser
# driver.close()
