from selenium import webdriver

# Como resolver o erro de geckodriver
# Entrar no site e baixar o driver mais recente geckodriver-v0.26.0-linux64.tar.gz
# https://github.com/mozilla/geckodriver/releases
# Descompactar e copiar o arquivo para a pasta bin no root.
# sudo cp geckodriver /usr/local/bin

browser = webdriver.Firefox()
browser.get('https://www.instagram.com/?hl=pt-br')
browser.maximize_window()
browser.implicitly_wait(20)


input_login = browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
input_login.click()
input_login.send_keys('login')

input_password = browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
input_password.click()
input_password.send_keys('password')


btn_enter = browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button')
btn_enter.click()