from selenium import webdriver

# Como resolver o erro de geckodriver
# Entrar no site e baixar o driver mais recente geckodriver-v0.26.0-linux64.tar.gz
# https://github.com/mozilla/geckodriver/releases
# Descompactar e copiar o arquivo para a pasta bin no root.
# sudo cp geckodriver /usr/local/bin

browser = webdriver.Firefox()
browser.get('https://www.instagram.com/?hl=pt-br')
browser.maximize_window()
browser.implicitly_wait(10)


def function_click(x_path):
    btn_enter = browser.find_element_by_xpath(x_path)
    btn_enter.click()
    return btn_enter


def login(input_path, key):
    input_login = browser.find_element_by_xpath(input_path)
    input_login.click()
    input_login.send_keys(key)


def get_content(x_path):
    btn_enter = browser.find_element_by_xpath(x_path)
    return btn_enter


def enter_into_account():
    login('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input', 'login')
    login('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input', 'password')

    # Clicando no botão enter.
    function_click('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button')

    try:
        function_click('/html/body/div[1]/section/main/div/div/div/div/button')
    except:
        print('Não há solicitação de salvar senha.')

    # Rejeitando primeiro pop up
    function_click('/html/body/div[4]/div/div/div[3]/button[2]')


def accessing_gallery():
    # Acessando galeria.
    function_click('/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a')

    # Acessando um item na galeria.  FULL_XPATH from class='eLAPa'
    function_click('//div[@class="eLAPa"]')


def scrapping_content():
    browser.implicitly_wait(10)

    # Pegadando a quantidade de publicações.
    quantity = get_content('/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span')

    data_from_intagram = {'Data': []}

    for x in range(int(quantity.text)):
        try:
            try:
                # Pegando descriçao.
                description = get_content(
                    '/html/body/div[4]/div[2]/div/article/div[2]/div[1]/ul/div/li/div/div/div[2]/span')
                photo_description = description.text
            except:
                photo_description = "Não há descrição"

            # Pegando data.

            date_photo = get_content('/html/body/div[4]/div[2]/div/article/div[2]/div[2]/a/time')
            date = date_photo.text

            # Pegando likes.
            total_likes = get_content('/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div[2]/button/span')
            likes = total_likes.text
            likes = int(likes) + 1

            photo_dict = {
                'id': x,
                'date': date,
                'likes': likes,
                'description': photo_description
            }

            data_from_intagram['Data'].append(photo_dict)

            # test
            if x == (int(quantity.text)-1):
                print('End')
            else:
                if x == 0:
                    function_click('/html/body/div[4]/div[1]/div/div/a')
                else:
                    function_click('/html/body/div[4]/div[1]/div/div/a[2]')
        except:
            continue

    return data_from_intagram
