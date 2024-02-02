def start_chrome():
    import os
    os.chdir('C:\\Program Files\\Google\\Chrome\\Application')
    os.system('chrome.exe --remote-debugging-port=9222 --user-data-dir="D:/chromedriver/config"')


if __name__ == '__main__':
    start_chrome()
