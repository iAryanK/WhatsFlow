import os, shutil
from get_chrome_driver import GetChromeDriver
from selenium import webdriver

def install_driver():
    get_driver = GetChromeDriver()

    with open('current_driver_version.txt', 'r+') as file:
        current_version = file.read()
        if (get_driver.stable_version()==current_version):
            return
        else:
            if os.path.exists('chromedriver.exe'):
                os.remove('chromedriver.exe')
            if os.path.exists('chromedriver'):
                shutil.rmtree('chromedriver')
                
            get_driver.auto_download(output_path=".", extract=True)
            get_driver.install()

            file.seek(0)
            file.truncate()
            file.write(get_driver.stable_version())
            if os.path.exists('chromedriver'):
                shutil.rmtree('chromedriver')
