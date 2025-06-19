import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# ✅ Read credentials from GitHub Secrets
EMAIL = os.environ.get("NAUKRI_EMAIL")
PASSWORD = os.environ.get("NAUKRI_PASSWORD")

# ✅ Path to resume file (must be in root of repo)
RESUME_PATH = os.path.join(os.getcwd(), "resume.pdf")

# ✅ Set up headless Chrome with correct binary path
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.binary_location = "/usr/bin/google-chrome"

# ✅ Launch Chrome browser
driver = webdriver.Chrome(options=options)

try:
    # ✅ Open Naukri login page
    driver.get("https://www.naukri.com/nlogin/login")
    time.sleep(3)

    # ✅ Enter email and password
    driver.find_element(By.ID, "usernameField").send_keys(EMAIL)
    driver.find_element(By.ID, "passwordField").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)

    # ✅ Go to profile page
    driver.get("https://www.naukri.com/mnjuser/profile")
    time.sleep(5)

    # ✅ Upload resume
    upload = driver.find_element(By.XPATH, "//input[@type='file']")
    upload.send_keys(RESUME_PATH)
    time.sleep(5)

    print("✅ Resume uploaded successfully.")

except Exception as e:
    print("❌ Error occurred:", e)

finally:
    driver.quit()
