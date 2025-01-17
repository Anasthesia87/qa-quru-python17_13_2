from time import sleep

from selene import browser, by, be, have
from selene.support.shared import browser
from spectrum_data_tests.model.page.main_page import MainPage
import allure



def test_github_desktop():

    # ----------------
    browser.open('/')

    # browser.element('.head-section__main > div > button').click()
    # browser.element('#call-form > button').click()

    # browser.element('.head-section__main > div > button').click()
    # browser.element('#form_text_7_2').type('Technostar')
    # browser.element('#form_text_8_2').type('Ivanov Ivan Ivanovich')
    # browser.element('#form_email_9_2').type('test@technostar.ru')
    # browser.element('#form_text_10_2').type('89119119191')
    # browser.element('#form_textarea_11_2').type('do not distrub')
    # browser.element('#call-form > div > form > label > button').click()
    # browser.element('#call-form > button').click()

    browser.element(by.text('Подключение')).click()
    browser.element(by.text('Удобный формат работы: web-интерфейс, API, мобильное приложение'))
    browser.element('.head-section__button-block > div > a').click()
    sleep(5)
    browser.element('#call-form > button').click()

    # browser.element(by.text('Карьера')).click()
    # browser.element(by.text('Смотреть вакансии')).click()
    # browser.element('#vacancies').should(be.visible)
    #
    # browser.element(by.text('О нас')).click()
    # browser.element('.head-section__button-block > div > a').click()
    # browser.element('#call-form > button').click()
    #
    # browser.element(by.text('Блог')).click()
    # browser.element(by.text('Связаться с нами')).click()
    # browser.element('#call-form > button').click()
    #
    # browser.element(by.text('Контакты')).click()
    # browser.element(by.text('Связаться с нами')).click()
    # browser.element('#call-form > button').click()
    #
    # browser.element(by.text('Вход')).click()
    # browser.element('#kc-page-title').should(be.visible)
    sleep(5)










    sleep(5)




