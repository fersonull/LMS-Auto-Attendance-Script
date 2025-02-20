from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as webWait
from selenium.webdriver.support import expected_conditions as EC
import schedule
import time

# paste your email and password inside.
email = "youremail@gmail.com";
password = "yourpass123";

print("Auto Attendance Script successfuly loaded.")
time.sleep(2)
print("Detecting your your time and schedule, don't close the program...")

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
            subName = ""

            match ind:
                case 0:
                    # ArtHum
                    sub = "https://pmftci.com/college/view-subject-lessons/125149"
                    subName = "Arths and Humanities"
                case 1:
                    # ArtApp
                    sub = "https://pmftci.com/college/view-subject-lessons/125150"
                    subName = "Art Appreciation"
                case 2:
                    # Integrative Programming
                    sub = "https://pmftci.com/college/view-subject-lessons/125151"
                    subName = "Integrative Programming and Technologies"
                case 3:
                    # Information System
                    sub = "https://pmftci.com/college/view-subject-lessons/125152"
                    subName = "Information Management"
                case 4:
                    # QM
                    sub = "https://pmftci.com/college/view-subject-lessons/125153"
                    subName = "Quantitave Methods"
                case 5:
                    # Networking
                    sub = "https://pmftci.com/college/view-subject-lessons/125154"
                    subName = "Networking 1"


            driver.get(sub)
            waitURL(driver, 20, sub)
            time.sleep(2)

            buttons = driver.find_elements(By.TAG_NAME, "button")
            
            for i, button in enumerate(buttons):
                if button.text == "Available":
                    button.click()
                    print("Successfuly Attended your Subject: " + subName)
                    time.sleep(3)
                    return
            
            print("No Available Lessons for Subject: " + subName)
            time.sleep(2)
            driver.close()

        case "half":
            sub = ""
            subName = ""

            match ind:
                case 0:
                    sub = "https://pmftci.com/college/view-subject-lessons/125155"
                    subName = "Physical Education"

            driver.get(sub)
            waitURL(driver, 20, sub)
            time.sleep(2)

            buttons = driver.find_elements(By.TAG_NAME, "button")
            
            for i, button in enumerate(buttons):
                if button.text == "Available":
                    button.click()
                    print("Successfuly Attended your Subject: " + subName)
                    time.sleep(3)
                    return
            
            print("No Available Lessons for Subject: " + subName)
            time.sleep(2)

            driver.close()

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
schedule.every().wednesday.at("09:10").do(lambda: auto_attendance("full", 0))
schedule.every().wednesday.at("09:10").do(lambda: auto_attendance("full", 0))
schedule.every().wednesday.at("10:10").do(lambda: auto_attendance("full", 1))
schedule.every().wednesday.at("11:10").do(lambda: auto_attendance("full", 2))
schedule.every().wednesday.at("14:10").do(lambda: auto_attendance("full", 3))
schedule.every().wednesday.at("15:10").do(lambda: auto_attendance("full", 4))
schedule.every().wednesday.at("16:10").do(lambda: auto_attendance("full", 5))

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
