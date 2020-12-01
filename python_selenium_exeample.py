from time import sleep

from selenium import webdriver

def OuverturedeUrl():
    driver = webdriver.Chrome(executable_path='Driver\chromedriver.exe')

    # La fenetre prend la totalité de l'écran
    #driver.maximize_window()

    driver.get('http://www.seleniumeasy.com/test/basic-first-form-demo.html')

    #
    # assert "Selenium Easy Demo - Simple Form to Automate using Selenium" in driver.title
    #
    # eleUserMessage = driver.find_element_by_id("user-message")
    #
    # eleUserMessage.clear()
    #
    # eleUserMessage.send_keys("Test Python")
    #
    # eleShowMsgBtn = driver.find_element_by_css_selector('#get-input > .btn')
    #
    # eleShowMsgBtn.click()
    #
    # eleYourMsg = driver.find_element_by_id("display")
    #
    # assert "Test Python" in eleYourMsg.text

    sleep(9999999999999)
    driver.close()


if __name__ == '__main__':
    OuverturedeUrl()
