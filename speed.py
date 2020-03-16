from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

def speed_test():
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://www.speedtest.net")
    test_button = driver.find_element_by_class_name('start-text')
    test_button.click()
    time.sleep(10)
    try:
        latency = int(driver.find_element_by_class_name('ping-speed').text)
    except ValueError:
        print("Could not convert string to float. String 'ping-speed' does not exist.")
    # print(latency)
    time.sleep(20)
    try:
        download = float(driver.find_element_by_class_name('download-speed').text)
    except ValueError:
        print("Could not convert string to float. String 'download-speed' does not exist.")
    # print(download)
    time.sleep(15)
    try:
        upload = float(driver.find_element_by_class_name('upload-speed').text)
    except ValueError:
        print("Could not convert string to float. String 'upload-speed' does not exist.")
    # print(upload)
    # print(speeds)
    driver.quit()
    speeds_dict = { "latency":latency, "download":download, "upload":upload }
    print("Test completed..")
    return speeds_dict
