
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.google.com")

driver.title # => "Google"

driver.implicitly_wait(0.5)

search_box = driver.find_element(By.NAME, "q")
search_button = driver.find_element(By.NAME, "btnK")

search_box.send_keys("Selenium") #This is what you'd what in the address bar so it can be anything. 
search_button.click()

driver.find_element(By.NAME, "q").get_attribute("value") # => "Selenium"

driver.quit()
