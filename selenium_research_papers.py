from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://scholar.google.com/")

# Option to login if not already logged into google account/gscholar email
driver.find_element(By.XPATH, value="/html/body/div/div[7]/div[2]/a").click()
email_login = driver.find_element(By.ID, "identifierId")
email_login.send_keys("<EMAIL>", Keys.ENTER)
email_pass = driver.find_element(By.NAME, "Passwd")
email_pass.send_keys("<PASSWORD>", Keys.ENTER)

search = driver.find_element(By.NAME, value="q")
search.send_keys("Network engineering", Keys.ENTER)

#searches for the newest publications for 2024
driver.find_element(By.XPATH, "/html/body/div/div[10]/div[1]/div/div[1]/ul/li[2]/a").click()

#Adds the newest publication to your saved list to read later
entries = driver.find_elements(By.CLASS_NAME, "gs_r")
if entries:
    newest = entries[0]
    save = driver.find_element(By.CSS_SELECTOR, "svg.gs_or_svg").click()
