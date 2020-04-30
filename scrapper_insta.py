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
input_login.send_keys('')

input_password = browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
input_password.click()
input_password.send_keys('')

# Clicando no botão enter.
btn_enter = browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button')
btn_enter.click()

# Rejeitando primeiro pop up
btn_enter = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
btn_enter.click()

# Acessando galeria.
btn_enter = browser.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a')
btn_enter.click()

# Acessando um item na galeria.
btn_enter = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div['
                                          '1]/a/div')
btn_enter.click()

# Pegando descriçao.
btn_enter = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/div[1]/ul/div/li/div/div/div['
                                          '2]/span')
print(btn_enter.text)

# Pegando data.
btn_enter = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/div[2]/a/time')
print(btn_enter.text)

# Pegando likes.
btn_enter = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div[2]/button/span')
print(btn_enter.text)



