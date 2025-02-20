from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as webWait
from selenium.webdriver.support import expected_conditions as EC
import schedule
import time

# paste your email and password inside.
email = "";
password = "";

def waitURL(driver, time, link):
    webWait(driver, time).until(EC.url_to_be(
        link
    ))


def auto_attendance(day, ind):
    driver = webdriver.Chrome()

    driver.get("https://pmftci.com/college/login")

    webWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )

    emailF = driver.find_element(By.NAME, "email")
    passwordF = driver.find_element(By.NAME, "password")
    loginBtn = driver.find_element(By.ID, "login-btn")

    time.sleep(2)

    emailF.send_keys(email)
    passwordF.send_keys(password)
    loginBtn.send_keys(Keys.RETURN)

    waitURL(driver, 20, "https://pmftci.com/college")

    time.sleep(1)

    driver.get("https://pmftci.com/college/my-subjects")
    waitURL(driver, 20, "https://pmftci.com/college/my-subjects")

    time.sleep(2)
    
    match day:
        case "full":
            sub = ""

            match ind:
                case 0:
                    # ArtHum
                    sub = "https://pmftci.com/college/view-subject-lessons/125149"
                case 1:
                    # ArtApp
                    sub = "https://pmftci.com/college/view-subject-lessons/125150"
                case 2:
                    # Integrative Programming
                    sub = "https://pmftci.com/college/view-subject-lessons/125151"
                case 3:
                    # Information System
                    sub = "https://pmftci.com/college/view-subject-lessons/125152"
                case 4:
                    # QM
                    sub = "https://pmftci.com/college/view-subject-lessons/125153"
                case 5:
                    # Networking
                    sub = "https://pmftci.com/college/view-subject-lessons/125154"


            driver.get(sub)
            waitURL(driver, 20, sub)
            time.sleep(2)

            buttons = driver.find_elements(By.TAG_NAME, "button")
            
            for i, button in enumerate(buttons):
                if button.text == "Available":
                    button.click()
                    driver.execute_script("alert('Successfuly Attended.')")
                    time.sleep(3)
                    return
            
            driver.execute_script("alert('No Available Lessons.')")
            time.sleep(2)

        case "half":
            sub = ""

            match ind:
                case 0:
                    sub = "https://pmftci.com/college/view-subject-lessons/125155"

            driver.get(sub)
            waitURL(driver, 20, sub)
            time.sleep(2)

            buttons = driver.find_elements(By.TAG_NAME, "button")
            
            for i, button in enumerate(buttons):
                if button.text == "Available":
                    button.click()
                    driver.execute_script("alert('Successfuly Attended.')")
                    time.sleep(3)
                    return
            
            driver.execute_script("alert('No Available Lessons.')")
            time.sleep(2)


# auto_attendance(today);

# Monday scheds
schedule.every().monday.at("09:10").do(lambda: auto_attendance("full", 0))
schedule.every().monday.at("10:10").do(lambda: auto_attendance("full", 1))
schedule.every().monday.at("11:10").do(lambda: auto_attendance("full", 2))
schedule.every().monday.at("14:10").do(lambda: auto_attendance("full", 3))
schedule.every().monday.at("15:10").do(lambda: auto_attendance("full", 4))
schedule.every().monday.at("16:10").do(lambda: auto_attendance("full", 5))

# Tuesday scheds
schedule.every().tuesday.at("10:10").do(lambda: auto_attendance("half", 0))

# Wednesday scheds
schedule.every().wednesday.at("09:00").do(lambda: auto_attendance("full", 0))
schedule.every().wednesday.at("09:10").do(lambda: auto_attendance("full", 0))
schedule.every().wednesday.at("10:10").do(lambda: auto_attendance("full", 1))
schedule.every().wednesday.at("11:10").do(lambda: auto_attendance("full", 2))
schedule.every().wednesday.at("14:10").do(lambda: auto_attendance("full", 3))
schedule.every().wednesday.at("15:10").do(lambda: auto_attendance("full", 4))
schedule.every().wednesday.at("16:00").do(lambda: auto_attendance("full", 5))

#Friday scheds 
schedule.every().friday.at("09:10").do(lambda: auto_attendance("full", 0))
schedule.every().friday.at("10:10").do(lambda: auto_attendance("full", 1))
schedule.every().friday.at("11:10").do(lambda: auto_attendance("full", 2))
schedule.every().friday.at("14:10").do(lambda: auto_attendance("full", 3))
schedule.every().friday.at("15:10").do(lambda: auto_attendance("full", 4))
schedule.every().friday.at("16:10").do(lambda: auto_attendance("full", 5))

while True:
    schedule.run_pending();
    time.sleep(5)
    
