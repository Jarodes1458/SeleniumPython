from selenium import webdriver


def OuverturedeUrl():
    driver = webdriver.Chrome(executable_path='Driver\chromedriver.exe')
    driver.get('https://esig-sandbox.ch/team20_5_v2/')
    driver.maximize_window()



if __name__ == '__main__':
    OuverturedeUrl()
