from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Step 1: Read credentials from credentials.txt
with open("credentials.txt", "r") as f:
    lines = f.readlines()
    EMAIL = lines[0].strip()
    PASSWORD = lines[1].strip()

# Step 2: Set resume path (relative to current folder)
RESUME_PATH = os.path.join(os.getcwd(), "resume.pdf")

# Step 3: Initialize Chrome driver (make sure chromedriver is in the same folder or in PATH)
driver = webdriver.Chrome()

try:
    # Step 4: Go to Naukri login page
    driver.get("https://www.naukri.com/nlogin/login")
    time.sleep(3)

    # Step 5: Fill in login credentials
    driver.find_element(By.ID, "usernameField").send_keys(EMAIL)
    driver.find_element(By.ID, "passwordField").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)

    # Step 6: Go to profile page
    driver.get("https://www.naukri.com/mnjuser/profile")
    time.sleep(5)

    # Step 7: Upload the resume
    upload = driver.find_element(By.XPATH, "//input[@type='file']")
    upload.send_keys(RESUME_PATH)

    print("✅ Resume uploaded successfully.")

except Exception as e:
    print("❌ Something went wrong:", e)

finally:
    time.sleep(5)
    driver.quit()
