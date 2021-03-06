import pickle
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from datetime import datetime
import schedule


def leave(driver):
    # leave meeting
    btn = driver.find_element_by_xpath(
        '//*[@id="wc-footer"]/div/div[3]/div/button')
    driver.execute_script("arguments[0].click();", btn)
    btn = driver.find_element_by_xpath(
        '//*[@id="wc-footer"]/div[2]/div[2]/div[3]/div/div/button')
    btn.click()
    time.sleep(5)


def main(args):
    option = Options()

    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")

    driver = webdriver.Chrome(
        ChromeDriverManager().install(), chrome_options=option)

    if args.cookies == False:
        driver.get("https://zoom.us")

        # please sign in manually through the created window
        import ipdb
        ipdb.set_trace()

        # if you get an error message on the screen and you're an UofA student,
        # please type 'driver.get("https://arizona.zoom.us")' at the prompt and sign in again.
        # if you succeed in login,
        # then, type "c" at the promt to run the rest of the code below
        pickle.dump(driver.get_cookies(), open("cookie.pkl", "wb"))
        driver.quit()
        exit()

    else:
        url = args.url + "\#success"
        passcode = args.passcode

        driver.get(url)
        cookies = pickle.load(open("cookie.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.find_element_by_xpath(
            '//*[@id="zoom-ui-frame"]/div[2]/div/div[2]/h3[2]/a').click()
        time.sleep(2)
        driver.find_element_by_id("joinBtn").click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "inputpasscode"))
        )
        driver.find_element_by_id("inputpasscode").send_keys(passcode)
        driver.find_element_by_id("joinBtn").click()
        driver.implicitly_wait(10)

        audio = False
        mute = False
        print("The meeting starts now.")
        while True:

            # if [ALERT] this meeting is being recorded
            try:
                # click continue
                driver.find_element_by_xpath(
                    '/html/body/div[8]/div/div/div/div[2]/div/div/button[1]').click()
            except:
                pass

            # computer audio
            try:
                if audio == False:
                    driver.find_element_by_xpath(
                        '//*[@id="voip-tab"]/div/button').click()
                    audio = True
            except:
                pass

            try:
                if mute == False:
                    mute_btn = driver.find_element_by_xpath(
                        '//*[@id="wc-footer"]/div/div[1]/div[1]/button')
                    if mute_btn.get_attribute("aria-label") == 'mute my microphone':
                        driver.execute_script(
                            "arguments[0].click();", mute_btn)
                        mute = True
            except:
                pass

            # breakout rooms alert
            try:
                driver.find_element_by_xpath(
                    "/html/body/div[12]/div/div/div/div[2]/div/div/button[1]").click()
                mute = False
            except:
                pass

            localtime = time.localtime()
            times = args.end_time.split(":")
            hr = int(times[0])
            minute = int(times[1])
            if localtime.tm_hour == hr and (localtime.tm_min < minute + 2 and localtime.tm_min > minute - 2):
                leave(driver)
                driver.quit()
                print(localtime, "\n The meeting is ended.")
                exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--cookies', action='store_true')
    parser.add_argument('--url', type=str, default='https://zoom.us')
    parser.add_argument('--passcode', type=str, default='12345')
    parser.add_argument('--start_time', type=str, default='06:00')
    parser.add_argument('--end_time', type=str, default='07:15')
    args = parser.parse_args()

    if args.cookies:
        schedule.every().day.at(args.start_time).do(main, args)

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        main(args)
