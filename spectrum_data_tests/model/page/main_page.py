from selene import browser, by, be


class MainPage:
    def __init__(self):
        self.submit_application_main_page = browser.element('.head-section__main > div > button')
        self.submit_application_via_other_section = browser.element('.head-section__button-block > div > a')
        self.consultation_form = browser.element('#call-form')
        self.consultation_form_close_button = browser.element('#call-form > button')
        self.connection = browser.element(by.text('Подключение'))
        self.connection_description = browser.element(by.text('Удобный формат работы: web-интерфейс, API, мобильное приложение'))
        self.career = browser.element(by.text('Карьера'))
        self.career_description = browser.element(by.text('Стань частью команды SpectrumData'))
        self.view_vacancies = browser.element(by.text('Смотреть вакансии'))
        self.vacancies = browser.element('#vacancies')
        self.about_company = browser.element(by.text('О нас'))
        self.about_company_description = browser.element(by.text('Компания, проекты и наши клиенты'))
        self.blog = browser.element(by.text('Блог'))
        self.blog_description = browser.element(by.text('О продуктах, компании ﻿и отраслевых рынках'))
        self.contacts = browser.element(by.text('Контакты'))
        self.contacts_description = browser.element(by.text('Адреса офисов и способы связи'))
        self.sign_in = browser.element(by.text('Вход'))
        self.sign_in_description = browser.element(by.text('Войти в личный кабинет'))

    def open(self):
        browser.open('/')

    def click_submit_application(self):
        self.submit_application_main_page.click()

    def click_submit_application_via_other_section(self):
        self.submit_application_via_other_section.click()

    def check_consultation_form(self):
        self.consultation_form.should(be.visible)
        self.consultation_form_close_button.click()

    def click_connection(self):
        self.connection.click()

    def check_connection(self):
        self.connection_description.should(be.visible)

    def click_career(self):
        self.career.click()

    def check_career(self):
        self.career_description.should(be.visible)

    def click_view_vacancies(self):
        self.view_vacancies.click()

    def check_vacancies(self):
        self.vacancies.should(be.visible)

    def click_about_company(self):
        self.about_company.click()

    def check_about_company(self):
        self.about_company_description.should(be.visible)

    def click_blog(self):
        self.blog.click()

    def check_blog(self):
        self.blog_description.should(be.visible)

    def click_contacts(self):
        self.contacts.click()

    def check_contacts(self):
        self.contacts_description.should(be.visible)

    def click_sign_in(self):
        self.sign_in.click()

    def check_sign_in(self):
        self.sign_in_description.should(be.visible)

