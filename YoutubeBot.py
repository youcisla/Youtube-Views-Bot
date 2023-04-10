import os
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager as CM
from getpass import getpass

# FOR TESTING ==================
#username = ''
#password = ''
# ==============================

ELEMENTS_TIMEOUT = 15
FOLLOW_DATA_LOADING_TIMEOUT = 50


def getYoutubeViews():
    
    username = "Enter Your Google Username"
    password = "Enter Your Password"

    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--log-level=0")

    mobile_emulation = {
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/535.19"}
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    bot = webdriver.Chrome(executable_path=CM().install(), options=options)
    bot.set_window_size(600, 1000)

    YoutubeLink = bot.get('https://www.youtube.com/watch?v=TSFVuErKlTQ')
    time.sleep(3)
    
    coockies = bot.find_element(By.XPATH,'//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button')
    coockies.click()
    print("Cookies accepted")
    time.sleep(3)

    YoutubeLink = bot.get('https://www.youtube.com/watch?v=TSFVuErKlTQ&list=PL2tcOaG8yVgY8ZwLrhu2N0TfeIishKr97')
    time.sleep(3)

    print("Done !")

    loginButton = bot.find_element(By.XPATH,'//*[@id="buttons"]/ytd-button-renderer/yt-button-shape')
    loginButton.click()
    time.sleep(3)
    
    user_element = bot.find_element(By.XPATH,'//*[@id="identifierId"]')
    user_element.send_keys(username)

    NextButton = bot.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button')
    NextButton.click()
    time.sleep(3)

    pass_element = bot.find_element(By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input')
    pass_element.send_keys(password)
    time.sleep(3)

    NextButton = bot.find_element(By.XPATH,'//*[@id="passwordNext"]/div/button')
    NextButton.click()    
    time.sleep(36)
    
    ProfileButton = bot.find_element(By.XPATH,'//*[@id="avatar-btn"]')
    ProfileButton.click()
    time.sleep(3)
    
    Disconnection = bot.find_element(By.XPATH,'//*[@id="items"]/ytd-compact-link-renderer[4]')
    Disconnection.click()
    time.sleep(3)
        
    while True:
        YoutubeLink = bot.get('https://www.youtube.com/watch?v=TSFVuErKlTQ&list=PL2tcOaG8yVgY8ZwLrhu2N0TfeIishKr97')
        time.sleep(3)

        print("Done !")

        loginButton = bot.find_element(By.XPATH,'//*[@id="buttons"]/ytd-button-renderer/yt-button-shape')
        loginButton.click()
        time.sleep(3)
        
        user_element = bot.find_element(By.XPATH,'//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]/div/div[1]/div/div[2]/div[1]')
        user_element.click()
        time.sleep(3)

        pass_element = bot.find_element(By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input')
        pass_element.send_keys(password)
        time.sleep(3)
    
        NextButton = bot.find_element(By.XPATH,'//*[@id="passwordNext"]/div/button')
        NextButton.click()        
        time.sleep(36)
        
        ProfileButton = bot.find_element(By.XPATH,'//*[@id="avatar-btn"]')
        ProfileButton.click()
        time.sleep(3)
        
        Disconnection = bot.find_element(By.XPATH,'//*[@id="items"]/ytd-compact-link-renderer[4]')
        Disconnection.click()
        time.sleep(3)   

if __name__ == '__main__':
    getYoutubeViews()
