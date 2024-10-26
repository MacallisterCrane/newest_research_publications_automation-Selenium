import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

try:
    # Initialize Chrome with default settings
    chrome_options = uc.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = uc.Chrome()

    driver.get("https://scholar.google.com/")

    # Option to login if not already logged into google account/gscholar email
    driver.find_element(By.XPATH, "/html/body/div/div[7]/div[2]/a").click()

    email_login = driver.find_element(By.ID, "identifierId")
    email_login.send_keys("<EMAIL>", Keys.ENTER)

    # Wait for the password field to load
    driver.implicitly_wait(10)
    email_pass = driver.find_element(By.NAME, "Passwd")
    email_pass.send_keys("<PASSWORD>", Keys.ENTER)

    search = driver.find_element(By.NAME, "q")
    search.send_keys("Network Engineering", Keys.ENTER)

    # Search for the newest publications for 2024
    driver.find_element(By.XPATH, "/html/body/div/div[10]/div[1]/div/div[1]/ul/li[2]/a").click()

    # Adds the newest publication to your saved list to read later
    entries = driver.find_elements(By.CLASS_NAME, "gs_r")
    if entries:
        newest = entries[0]
        save_buttons = newest.find_elements(By.CSS_SELECTOR, "svg.gs_or_btn")
        if save_buttons:
            save_button = save_buttons[0]
            save_text = save_button.get_attribute("aria-label")
            if "Saved" not in save_text:
                save_button.click()
                print("Added newest publication to saved list.")
            else:
                print("Publication already saved.")
        else:
            print("Save button not found.")

    #Shows current library after adding the newest addition-----this is cross-account compatible
    driver.get("https://scholar.google.com/scholar?scilib=1&scioq=Network+engineering&hl=en&as_sdt=0,45")
    while True:
        pass
finally:
    pass
