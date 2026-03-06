from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com")

wait = WebDriverWait(driver, 10)

username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
password = wait.until(EC.presence_of_element_located((By.NAME, "password")))

username.send_keys("Admin")
password.send_keys("admin123")

driver.find_element(By.XPATH,'//button[@type="submit"]').click()

print("Login Successful")

driver.quit()