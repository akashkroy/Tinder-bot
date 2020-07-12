from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class Tinder_bot():
    def __init__(self):
        self.total_likes = 0
        print("# Copy the full path including 'chromedriver.exe'")
        chromedriver_path = input("# Enter full path to chromedriver: ")
        
        self.email = input("# Enter your Facebook email: ")
        self.password = input("# Enter your Facebook password: ")

        self.driver = webdriver.Chrome(executable_path=chromedriver_path)
    
    def login(self):
        self.driver.get("https://tinder.com")
        
        sleep(4)
        
        try:
            more_opt = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/button')
            more_opt.click()
            sleep(3)
        except NoSuchElementException:
            pass
        
        #//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button
        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        fb_btn.click()
        
        #switch to popup window
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        self.driver.find_element_by_name("email").send_keys(self.email)
        self.driver.find_element_by_name("pass").send_keys(self.password)
        self.driver.find_element_by_name("login").click()
        sleep(3)
        self.driver.switch_to_window(base_window)
        sleep(5)
    
    def popups(self):
        location = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        location.click()
        sleep(2)
        notifications = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
        notifications.click()
        sleep(2)
        cookie = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        cookie.click()
        sleep(2)
    
    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        while True:
            try:
                #add tinder to home screen 
                home_scrn_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
                home_scrn_btn.click()
            except NoSuchElementException:
                like_btn.click()
                self.total_likes += 1
                sleep(2)
            
        
        
bot = Tinder_bot()
bot.login()
bot.popups()
try:
    bot.like()
except:
    print(f'# Total Liked : {bot.total_likes}')
        