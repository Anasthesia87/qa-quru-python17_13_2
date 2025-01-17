from time import sleep

from selene import browser, by, be
from selene.support.shared import browser
from spectrum_data_tests.model.page.main_page import MainPage
import allure


@allure.title('Корректная работа кнопки "Оставить заявку" на главной странице сайта')
def test_main_page_element_submit_application(settings_browser):
    with allure.step('Открыть главную страницу сайта'):
        main_page = MainPage()
        main_page.open()

    with allure.step('Найти и нажать на кнопку "Оставить заявку"'):
        main_page.click_submit_application()

    with allure.step('Проверить открытие формы "Оставьте заявку на консультацию"'):
        main_page.check_consultation_form()


@allure.title('Корректная работа блока "Подключение" на главной странице сайта')
def test_main_page_element_connection(settings_browser):
    with allure.step('Открыть главную страницу сайта'):
        main_page = MainPage()
        main_page.open()

    with allure.step('Найти и нажать на элемент "Подключение"'):
        main_page.click_submit_application()

    with allure.step('Проверить переход к разделу "Подключение"'):
        main_page.click_submit_application()

    with allure.step('Найти и нажать на кнопку "Оставить заявку" в разделе "Подключение"'):
        main_page.click_submit_application()

    with allure.step('Проверить появление формы "Оставьте заявку на консультацию"'):
        main_page.check_consultation_form()


@allure.title('Корректная работа блока "Карьера" на главной странице сайта')
def test_main_page_element_career(settings_browser):
    with allure.step('Открыть главную страницу сайта'):
        main_page = MainPage()
        main_page.open()

    with allure.step('Найти и нажать на элемент "Карьера"'):
        main_page.click_career()

    with allure.step('Проверить переход к блоку "Карьера:вакансии"'):
        main_page.check_career()

    with allure.step('Найти и нажать на кнопку "Смотреть вакансии"'):
        main_page.click_view_vacancies()

    with allure.step('Проверить появление раздела "Вакансии"'):
        main_page.check_vacancies()


@allure.title('Корректная работа блока "О нас" на главной странице сайта')
def test_main_page_element_about_company(settings_browser):
    with allure.step('Открыть главную страницу сайта'):
        main_page = MainPage()
        main_page.open()

    with allure.step('Найти и нажать на элемент "О нас"'):
        main_page.click_about_company()

    with allure.step('Проверить переход к разделу "О нас"'):
        main_page.check_about_company()

    with allure.step('Найти и нажать на кнопку "Оставить заявку" в разделе "О нас"'):
        main_page.click_submit_application()

    with allure.step('Проверить появление формы "Оставьте заявку на консультацию"'):
        main_page.check_consultation_form()



























    # ----------------
    browser.open('/')

    browser.element('.head-section__main > div > button').click()
    browser.element('#call-form > button').click()

    # browser.element('.head-section__main > div > button').click()
    # browser.element('#form_text_7_2').type('Technostar')
    # browser.element('#form_text_8_2').type('Ivanov Ivan Ivanovich')
    # browser.element('#form_email_9_2').type('test@technostar.ru')
    # browser.element('#form_text_10_2').type('89119119191')
    # browser.element('#form_textarea_11_2').type('do not distrub')
    # browser.element('#call-form > div > form > label > button').click()
    # browser.element('#call-form > button').click()

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




