from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from threading import Thread
import time
import config
from time import perf_counter

EXTENSION_PATH_ONE = "C:/Users/amtw123/Desktop/PROJECTS/crx_file_location/10.24.2_0.crx"
EXTENSION_PATH_TWO = "C:/Users/amtw123/Desktop/PROJECTS/crx_file_location/4.6.5_0.crx"
PATH = "C:\Program Files (x86)\Chrome Driver\chromedriver.exe"

opt = webdriver.ChromeOptions()
opt.add_extension(EXTENSION_PATH_ONE)
opt.add_extension(EXTENSION_PATH_TWO)

driver = webdriver.Chrome(options=opt, executable_path=PATH)

driver.switch_to.window(driver.window_handles[0])
original_window = driver.current_window_handle

xpaths_location = [
        '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[1]/div[1]/div/input',
        '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[2]/div[1]/div/input',
        '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[3]/div[1]/div/input',
        '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[4]/div[1]/div/input',
        '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[5]/div[1]/div/input',
        '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[6]/div[1]/div/input',
        '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[7]/div[1]/div/input',
        '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[8]/div[1]/div/input',
        '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[9]/div[1]/div/input',
        '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[10]/div[1]/div/input',
        '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[11]/div[1]/div/input',
        '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[12]/div[1]/div/input'
    ]


class DFK_API_calls:
    def forage_heroes():
        pass

    def fish_heroes():
        pass

    def mine_heroes():
        pass

    def garden_heroes():
        pass
    pass


def input_seedphrase_keys(xpath_location, seedphrase_key):
    driver.find_element(By.XPATH, xpath_location).send_keys(seedphrase_key)


def login_to_metamask():
        
    time.sleep(1)
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/ul/li[2]/button'))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/button[1]'))).click()

    for i in range(12):
        input_seedphrase_keys(xpaths_location[i], config.your_seedphrase[i])
        
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/button').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input').send_keys(config.mm_browser_pwd)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input').send_keys(config.mm_browser_pwd)
    driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/button').click()

    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button'))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button'))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button'))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-content"]/div/div[1]/div/div[2]/div/div'))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div[3]/button'))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[3]/a'))).click()

    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/label/input').send_keys("DFK Chain Mainnet")
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/label/input').send_keys("https://subnets.avax.network/defi-kingdoms/dfk-chain/rpc")
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/label/input').send_keys("53935")
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[4]/label/input').send_keys("JEWEL")
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[5]/label/input').send_keys("https://subnets.avax.network/defi-kingdoms/dfk-chain/explorer")
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[3]/button[2]').click()

def main():

    login_to_metamask()

    while True:
        bool_loop = int(input("Type 0 to exit the program:"))
        if bool_loop == 0:
            break

    driver.close()


main()
