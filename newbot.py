import time

import telebot
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get('https://wordstat.yandex.ru')
URL = browser.get('https://wordstat.yandex.ru')


API_KEY = '5465489989:AAGMpca8ww7GmlcF2ofDxFLO_qTZtliUUpM'
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['l'])
def log(message):
    s = bot.send_message(message.chat.id, "Введи логин")
    bot.register_next_step_handler(s, login)

def login(message):
    browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr/td[6]/table/tbody/tr[1]/td[2]/a/span').click()
    email_input = browser.find_element(By.ID, 'b-domik_popup-username')
    email_input.clear()
    email_input.send_keys('serega351351')

@bot.message_handler(commands=['p'])
def pas(message):
    s = bot.send_message(message.chat.id, "Введи пароль")
    bot.register_next_step_handler(s, password)


def password(message):
    browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr/td[6]/table/tbody/tr[1]/td[2]/a/span').click()
    passwor_input = browser.find_element(By.ID,'b-domik_popup-password')
    passwor_input.clear()
    passwor_input.send_keys('.Serega351.')
    passwor_input.send_keys(Keys.ENTER)

@bot.message_handler(commands=['s'])
def s(message):
    otvet = bot.send_message(message.chat.id, "Введите текст для поиска")
    bot.register_next_step_handler(otvet, se)

@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, "Для поиска введи значение /s")

def se(message):
    searc = browser.find_element(By.CLASS_NAME, 'b-form-input__input')
    searc.send_keys(message.text)
    time.sleep(5)
    searc.send_keys(Keys.ENTER)
    time.sleep(5)
    blocks = browser.find_element(By.CLASS_NAME,'b-word-statistics__table')
    all_blocks = blocks.find_elements(By.TAG_NAME, 'a')
    for i in range(len(all_blocks)):
        bot.send_message(message.chat.id, all_blocks[i].get_attribute('href'))
        if i == 3:
            break

bot.polling()

# blocks = browser.find_element(By.CLASS_NAME, 'b-word-statistics__table')
# v_n = blocks.find_elements(By.XPATH, '//td[@class="b-word-statistics__td b-word-statistics__td-number"]')
# for i in v_n:
#     bot.send_message(message.chat.id, i.text)


# blocks = browser.find_elements(By.XPATH, 'html/body/div[2]/div/div/table/tbody/tr/td[4]/div/div/div[2]/div[1]/div/table/tbody/tr[2]/td[1]/span/a')
#     return [i.get_attribute('href') for i in blocks]

# for i in range(len(blocks)):
#     bot.send_message(message.chat.id, blocks[i].get_attribute('href'))

for i in range(len(all_blocks)):
    bot.send_message(message.chat.id, all_blocks[i].text)
    if i == 6:
        break