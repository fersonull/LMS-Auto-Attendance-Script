from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as webWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime as dt
import schedule
import time
from colorama import Fore, Style, init

init(autoreset=True)

# paste your email and password inside.
email = "youremal@gmail.com";
password = "pass123";

print(r"""
                _                _   _                 _ 
     /\        | |              | | | |               | |
    /  \  _   _| |_ ___     __ _| |_| |_ ___ _ __   __| |
   / /\ \| | | | __/ _ \   / _` | __| __/ _ \ '_ \ / _` |
  / ____ \ |_| | || (_) | | (_| | |_| ||  __/ | | | (_| |
 /_/    \_\__,_|\__\___/   \__,_|\__|\__\___|_| |_|\__,_|
                                                                                                               
""")

print(Fore.GREEN + "Auto Attendance Script Successfuly Loaded.")
time.sleep(2)
print(Fore.LIGHTBLUE_EX + "Reading your Schedules... Don't close the Program.")



def waitURL(driver, time, link):
    webWait(driver, time).until(EC.url_to_be(
        link
    ))
 
def webInv(driver, time, elem):
    webWait(driver, time).until(EC.invisibility_of_element(elem))


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

            hours = dt.now().hour
            mins = dt.now().minute

            print(f"\n[{hours}:{mins:02d}] {Fore.GREEN}Subject: {subName} Successfuly Loaded. ")
            time.sleep(1)
            print(f"{Fore.LIGHTBLUE_EX}Waiting for Lesson to be Published...")
            
            max_retries = 12
            attempts = 0
            lessonFound = False
            while not lessonFound and attempts < max_retries:
                try:
                    attendBtn = webWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='View Lesson']")))
                    attendBtn.click()
                    time.sleep(3)

                    confirmBtn = webWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='OK']")))
                    confirmBtn.click()
                    time.sleep(5)

                    lessonFound = True
                    hours = dt.now().hour
                    mins = dt.now().minute

                    print(f"\n[{hours}:{mins:02d}] {Fore.GREEN}Succesfuly Attended your Subject: {subName}.\n")
                    time.sleep(2)
                    driver.close()
                except TimeoutException:
                    attempts += 1

                    hours = dt.now().hour
                    mins = dt.now().minute

                    print(f"[{hours}:{mins:02d}] {Fore.RED}Lesson not Found, Refreshing Page...")
                    driver.refresh()
                    time.sleep(3)
                    lessonFound = False

            if not lessonFound:
                print(f"{Fore.RED}\nMax Retries Reached. No published Lesson on Subject: {subName}.")
                

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

            hours = dt.now().hour
            mins = dt.now().minute

            print(f"\n[{hours}:{mins:02d}] {Fore.GREEN}Subject: {subName} Successfuly Loaded. ")
            time.sleep(1)
            print(f"{Fore.LIGHTBLUE_EX}Waiting for Lesson to be Published...")

            max_retries = 12
            attempts = 0
            lessonFound = False
            while not lessonFound and attempts < max_retries:
                try:
                    attendBtn = webWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='View Lesson']")))
                    attendBtn.click()
                    time.sleep(3)

                    confirmBtn = webWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='OK']")))
                    confirmBtn.click()
                    time.sleep(5)
            
                    lessonFound = True
                    hours = dt.now().hour
                    mins = dt.now().minute

                    print(f"\n[{hours}:{mins:02d}] {Fore.GREEN}Succesfuly Attended your Subject: {subName}.\n")
                    time.sleep(2)
                    driver.close()
                except TimeoutException:
                    attempts += 1
                    hours = dt.now().hour
                    mins = dt.now().minute
                    
                    print(f"[{hours}:{mins:02d}] {Fore.RED}Lesson not Found, Refreshing Page...")
                    driver.refresh()
                    time.sleep(3)
                    lessonFound = False

            if not lessonFound:
                print(f"{Fore.RED}\nMax Retries Reached. No published Lesson on Subject: {subName}.")

# Monday scheds
schedule.every().monday.at("09:00").do(lambda: auto_attendance("full", 0))
schedule.every().monday.at("10:00").do(lambda: auto_attendance("full", 1))
schedule.every().monday.at("11:00").do(lambda: auto_attendance("full", 2))
schedule.every().monday.at("14:00").do(lambda: auto_attendance("full", 3))
schedule.every().monday.at("15:00").do(lambda: auto_attendance("full", 4))
schedule.every().monday.at("16:00").do(lambda: auto_attendance("full", 5))

# Tuesday scheds
schedule.every().tuesday.at("10:00").do(lambda: auto_attendance("half", 0))

# Wednesday scheds
schedule.every().wednesday.at("09:00").do(lambda: auto_attendance("full", 0))
schedule.every().wednesday.at("10:00").do(lambda: auto_attendance("full", 1))
schedule.every().wednesday.at("11:00").do(lambda: auto_attendance("full", 2))
schedule.every().wednesday.at("14:00").do(lambda: auto_attendance("full", 3))
schedule.every().wednesday.at("15:00").do(lambda: auto_attendance("full", 4))
schedule.every().wednesday.at("16:00").do(lambda: auto_attendance("full", 5))

# Friday scheds 
schedule.every().friday.at("09:00").do(lambda: auto_attendance("full", 1))
schedule.every().friday.at("10:00").do(lambda: auto_attendance("full", 0))
schedule.every().friday.at("11:00").do(lambda: auto_attendance("full", 2))
schedule.every().friday.at("14:00").do(lambda: auto_attendance("full", 3))
schedule.every().friday.at("15:00").do(lambda: auto_attendance("full", 4))
schedule.every().friday.at("16:00").do(lambda: auto_attendance("full", 5))


while True:
    schedule.run_pending();
    time.sleep(5)
