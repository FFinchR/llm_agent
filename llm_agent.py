from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def start_chrome_debug():
    import os
    os.chdir('C:\\Program Files\\Google\\Chrome\\Application')
    os.system(r'chrome.exe --remote-debugging-port=9222 --user-data-dir="D:/chromedriver/config"')


class LLMAgent:
    def __init__(self):
        # start_debugger()
        options = Options()
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.driver = webdriver.Chrome(options=options)
        self.driver.minimize_window()
        self.driver.get("https://www.coze.com/space/x/bot/x")


    def ask(self, question):
        # self.driver.minimize_window()
        # self.driver.get("https://www.coze.com/space/7322348804131536904/bot/7329338760456470529")
        # 2 | setWindowSize | 1936x1048 |
        # self.driver.set_window_size(1936, 1048)
        # 3 | click | xpath=//div[3]/div/button |
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//div[3]/div/div/textarea")))
        try:
            self.driver.find_element(By.XPATH, "//div[3]/div/button").click()
        except NoSuchElementException:  # 捕捉 NoSuchElementException 异常
            print("元素不存在")
        # 4 | sendKeys | xpath=//div[3]/div/div/textarea | mysql的所有表接入
        self.driver.find_element(By.XPATH, "//div[3]/div/div/textarea").send_keys(question)
        # 5 | click | xpath=//div/div[2]/div/button |
        self.driver.find_element(By.XPATH, "//div/div[2]/div/button").click()
        # 6 | click | xpath=//body/div/div/div/div/div[2]/div/div[3]/div[2]/div/div/div |
        self.driver.find_element(By.XPATH, "//body/div/div/div/div/div[2]/div/div[3]/div[2]/div/div/div").click()
        # 7 | runScript | window.scrollTo(0,0) |
        self.driver.execute_script("window.scrollTo(0,0)")
        # 8 | waitForElementPresent | css=.semi-icon-tick > svg | 30000
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".semi-icon-tick > svg")))
        # 9 | echo | css=.auto-hide-last-sibling-br |
        result = self.driver.find_element(By.XPATH, "//div[2]/div/div/div/div[2]/div/div[2]/div/div").text
        print(result)
        return result
