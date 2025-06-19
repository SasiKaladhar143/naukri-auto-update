from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

# ✅ Step 1: Read credentials from GitHub Secrets
EMAIL = os.environ.get("NAUKRI_EMAIL")
PASSWORD = os.environ.get("NAUKRI_PASSWORD")

# ✅ Step 2: Set resume path (relative to current folder)
RESUME_PATH = os.path.join(os.getcwd(), "resume.pdf")

# ✅ Step 3: Set up Chrome in headless mode (for GitHub Actions)
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    # ✅ Step 4: Go to Naukri login page
    driver.get("https://www.naukri.com/nlogin/login")
    time.sleep(3)

    # ✅ Step 5: Fill in login credentials
    driver.find_element(By.ID, "usernameField").send_keys(EMAIL)
    driver.find_element(By.ID, "passwordField").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)

    # ✅ Step 6: Go to profile page
    driver.get("https://www.naukri.com/mnjuser/profile")
    time.sleep(5)

    # ✅ Step 7: Upload the resume
    upload = driver.find_element(By.XPATH, "//input[@type='file']")
    upload.send_keys(RESUME_PATH)

    print("✅ Resume uploaded successfully.")

except Exception as e:
    print("❌ Something went wrong:", e)

finally:
    time.sleep(5)
    driver.quit()
