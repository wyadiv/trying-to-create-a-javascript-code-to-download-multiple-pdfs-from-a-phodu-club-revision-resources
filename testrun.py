from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os

# 📁 Download folder
download_dir = os.path.abspath("phodu_downloads")
os.makedirs(download_dir, exist_ok=True)

# 🔧 Chrome options
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# 🔥 FORCE DOWNLOAD PDFs
prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "plugins.always_open_pdf_externally": True
}
options.add_experimental_option("prefs", prefs)

# Driver
service = Service(r"C:\Users\yourusername\Downloads\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# Hide selenium
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# Open site
driver.get("https://learn.phodu.club/learn/formula-sheets")

print("👉 LOGIN manually (20 sec)")
time.sleep(20)

# 🔽 Download function
def download_tab(subject):
    buttons = driver.find_elements(By.XPATH, "//*[text()='Open PDF']")
    print(f"\n{subject}: Found {len(buttons)} PDFs")

    for i in range(len(buttons)):
        try:
            btns = driver.find_elements(By.XPATH, "//*[text()='Open PDF']")
            btns[i].click()

            print(f"{subject} → Opening {i+1}")
            time.sleep(5)

            # 🔥 Get REAL PDF URL
            iframe = driver.find_element(By.TAG_NAME, "iframe")
            pdf_url = iframe.get_attribute("src")

            print("Triggering download...")

            # 🔥 Open PDF URL directly (forces download via Chrome prefs)
            driver.get(pdf_url)

            time.sleep(4)

            driver.back()
            time.sleep(2)

        except Exception as e:
            print("Skipped:", e)

# 🔁 Tabs
tabs = ["Physics", "Chemistry", "Maths"]

for tab in tabs:
    try:
        print(f"\nSwitching to {tab}")
        driver.find_element(By.XPATH, f"//*[contains(text(), '{tab}')]").click()
        time.sleep(3)
        download_tab(tab)
    except Exception as e:
        print(f"❌ Could not open {tab}:", e)

print("\n🎉 DONE — CHECK phodu_downloads")
