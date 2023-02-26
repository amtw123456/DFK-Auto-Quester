from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from threading import Thread
import time
import config
from time import perf_counter
import math

EXTENSION_PATH_ONE = "../crx_file_location/10.24.2_0.crx"
EXTENSION_PATH_TWO = "../crx_file_location/4.6.5_0.crx"
PATH = "C:\Program Files (x86)\Chrome Driver\chromedriver.exe"

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
opt.add_extension(EXTENSION_PATH_ONE)
opt.add_extension(EXTENSION_PATH_TWO)

opt.add_experimental_option("useAutomationExtension", False)
opt.add_experimental_option("excludeSwitches",["enable-automation"])

driver = webdriver.Chrome(options=opt, executable_path=PATH)
time.sleep(1)
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
# original_window = driver.current_window_handle

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
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/button'))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/button[1]'))).click()

    for i in range(12):
        input_seedphrase_keys(xpaths_location[i], config.your_seedphrase[i])
 
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/button').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input').send_keys(config.mm_browser_pwd)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input').send_keys(config.mm_browser_pwd)
    driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/button').click()
    time.sleep(1)
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
    time.sleep(4)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[3]/button[2]').click()

def import_private_key():
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/button').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/button[2]').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div[2]/div[2]/div[1]/input').send_keys(config.your_private_key)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div[2]/div[2]/div[2]/button[2]').click()


def check_number_of_questers(quest_type):
    # time.sleep(1)
    print("CHANGE TAB")
    driver.switch_to.window(driver.window_handles[0])
    print("CHANGE TAB")
    time.sleep(2)
    driver.get("https://game.defikingdoms.com/#/professions")
    driver.refresh();
    time.sleep(3)
    
    driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/button').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/button[2]').click()
    profession_xpaths = {
        "Mining" : "/html/body/div[3]/div[1]/div[1]/div[2]/div[3]/div/div[1]/label[2]/span[1]", # mining
        "Gardening" : "/html/body/div[3]/div[1]/div[1]/div[2]/div[3]/div/div[1]/label[3]/span[1]", # gardening
        "Fishing" : "/html/body/div[3]/div[1]/div[1]/div[2]/div[3]/div/div[1]/label[4]/span[1]", # fishing
        "Foraging" : "/html/body/div[3]/div[1]/div[1]/div[2]/div[3]/div/div[1]/label[5]/span[1]" # foraging
    
    }
    
    # driver.get("https://game.defikingdoms.com/#/professions")
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/div[2]/div[2]/div/button[2]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, profession_xpaths[quest_type]).click()

    driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/div[1]/button[1]').click()
    time.sleep(0.500)
    parent_element = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div/div")
    child_elements = parent_element.find_elements(By.XPATH, "./*")
    print("Number of " + quest_type + " heroes:", len(child_elements))

    return len(child_elements)
    

def queue_foraging_dfk_quest():

    num_of_foragers = check_number_of_questers("Foraging")
    num_of_quests = math.ceil(num_of_foragers / 6)
    time.sleep(0.500)
    driver.refresh();
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/button').click()
    # driver.get("https://game.defikingdoms.com/#/professions")
    # clicks the foraging quest
    time.sleep(0.2500)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[5]/div[5]/div/div/div/button[4]').click()
    # clicks the start quest
    time.sleep(0.500)
    driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/div[2]/div/ul/div/button').click()
    time.sleep(0.250)
    for i in range(num_of_quests):
        
        driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[1]/button').click()
        time.sleep(0.750)
        driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[3]/div[1]/div/button').click()
        time.sleep(0.250)
        driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[3]/button').click()
        time.sleep(0.750)
        driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[4]/button[2]').click()
        time.sleep(1.75)
    
    driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div[1]/button[2]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[5]/div[6]/div/button[2]').click()
    time.sleep(2)
    # driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div[3]/div[3]/button[3]').click()
    
    
    
def queue_fishing_dfk_quest():

    num_of_fishers = check_number_of_questers("Fishing")
    num_of_quests = math.ceil(num_of_fishers / 6)
    print(num_of_quests)
    time.sleep(0.500)
    driver.refresh();
    time.sleep(3)
    
    driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/button').click()
    # driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[5]/div[5]/div/div/div/button[2]').click()
    # driver.get("https://game.defikingdoms.com/#/professions")
    # clicks the foraging quest
    time.sleep(0.7500)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[5]/div[5]/div/div/div/button[2]').click()
    # clicks the start quest
    time.sleep(0.500)
    driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/div[2]/div/ul/div/button').click()
    time.sleep(0.250)
    for i in range(num_of_quests):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[1]/button'))).click()
        time.sleep(0.750)
        driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[3]/div[1]/div/button').click()
        time.sleep(0.250)
        driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[3]/button').click()
        time.sleep(0.750)
        driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[4]/button[2]').click()
        time.sleep(1.75)
    
    driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div[1]/button[2]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[5]/div[6]/div/button[2]').click()
    time.sleep(2)
    # driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div[3]/div[3]/button[3]').click()


def complete_dfk_quest():
    # clicks the active quest
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[5]/div[6]/div/button[3]').click()
    time.sleep(3)
    # checks for all the active quests and check their length gets the finished and the questing groups
    parent_element = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div/div[3]/div[2]")
    child_elements = parent_element.find_elements(By.XPATH, "./*")
    
    print("NUMBER OF CHILD ELEMENTS", len(child_elements))
    print("STARTIING COMPLETION OF QUEST")

    ctr = 0
    time.sleep(3)
    # iterates over all the active quest and checks if all are finished
    for i in range(1, len(child_elements) + 1):
        questing_group = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div[3]/div[2]/div['+ str(i) +']/div/div[3]')
        # checks the current questing group
        child_of_questing_group = questing_group.find_elements(By.XPATH, ".//*")
        # for checking if the questing group is finished must return a len of 4
        print(len(child_of_questing_group))
        if(len(child_of_questing_group) == 4):
            driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div/div[3]/div[2]/div[" + str(i) + "]/div/div[3]/button[1]").click()
            print("QUEST COMPLETED")
            ctr += 1
        else:
            print("QUEST NOT COMPLETED")
            break
    driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div[2]/button').click()
   
    
    # switches to mm and accepts all the contracts
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#")
    time.sleep(3)
    for i in range(ctr):
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[5]/div[3]/footer/button[2]').click()
        time.sleep(4)

def open_dfk_website():
    time.sleep(1)
    driver.get("https://game.defikingdoms.com/#/professions")
    
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[1]/div/button'))).click()
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[3]/div/div/button'))).click()
    # WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[1]/div/button'))).click()
    time.sleep(3)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/section/div[2]/div/button'))).click()
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div[1]/button'))).click()
    
    
    
    time.sleep(1)
    driver.switch_to.new_window('tab')
    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#")
    time.sleep(3)
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div[3]/div[2]/button[2]'))).click()
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]'))).click()
    # time.sleep(50)
    
    driver.switch_to.window(driver.window_handles[0])
    
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/button').click()
    time.sleep(3)
    
    # driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[3]/button[1]').click()
    # parent_element = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[3]")
    # child_elements = parent_element.find_elements(By.XPATH, ".//*")
   
    # time.sleep(5)
    # print("CLICKED THE X")
def main(): 

    login_to_metamask()
    import_private_key()
    open_dfk_website()
    # complete_dfk_quest()

    
    # num_of_fishers = check_number_of_questers("Fishing")
    # num_of_miners = check_number_of_questers("Mining")
    # num_of_gardening = check_number_of_questers("Gardening")

    queue_foraging_dfk_quest()
    time.sleep(2)
    queue_fishing_dfk_quest()

    while True:
        bool_loop = int(input("Type 0 to exit the program:"))
        if bool_loop == 0:
            break

    driver.close()


main()
