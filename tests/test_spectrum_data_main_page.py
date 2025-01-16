from time import sleep

from selene import browser, by, be
from selene.support.shared import browser


def test_main_page_object():
    # ----------------
    browser.open('/')

    browser.element('.head-section__main > div > button').click()
    browser.element('#call-form > button').click()

    browser.element(by.text('Подключение')).click()
    browser.element('.head-section__button-block > div > a').click()
    browser.element('#call-form > button').click()

    browser.element(by.text('Карьера')).click()
    browser.element(by.text('Смотреть вакансии')).click()
    browser.element('#vacancies').should(be.visible)

    browser.element(by.text('О нас')).click()
    browser.element('.head-section__button-block > div > a').click()
    browser.element('#call-form > button').click()

    browser.element(by.text('Блог')).click()
    browser.element(by.text('Связаться с нами')).click()
    browser.element('#call-form > button').click()

    browser.element(by.text('Контакты')).click()
    browser.element(by.text('Связаться с нами')).click()
    browser.element('#call-form > button').click()

    browser.element(by.text('Вход')).click()
    browser.element('#kc-page-title').should(be.visible)
    sleep(5)










    sleep(5)




