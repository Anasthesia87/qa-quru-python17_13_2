from spectrum_data_tests.model.page.main_page import MainPage
from spectrum_data_tests.model.form.consultation_form import ConsultationForm
import allure


@allure.title('Корректная работа кнопки "Вход" на главной странице сайта')
def test_main_page_element_sign_in(setup_browser):
    with allure.step('Открыть главную страницу сайта'):
        main_page = MainPage()
        main_page.open()

    with allure.step('Найти и нажать на кнопку "Вход"'):
        main_page.click_sign_in()

    with allure.step('Проверить появление формы "Войти в личный кабинет"'):
        main_page.check_sign_in()


@allure.title('Корректная работа кнопки "Оставить заявку" на главной странице сайта')
def test_main_page_element_submit_application(setup_browser):
    with allure.step('Открыть главную страницу сайта'):
        main_page = MainPage()
        main_page.open()

    with allure.step('Найти и нажать на кнопку "Оставить заявку"'):
        main_page.click_submit_application()

    with allure.step('Проверить открытие формы "Оставьте заявку на консультацию"'):
        main_page.check_consultation_form()


@allure.title('Корректный переход к блоку "Подключение" на главной странице сайта')
def test_main_page_element_connection(setup_browser):
    with allure.step('Открыть главную страницу сайта'):
        main_page = MainPage()
        main_page.open()

    with allure.step('Найти и нажать на элемент "Подключение"'):
        main_page.click_connection()

    with allure.step('Проверить переход к разделу "Подключение"'):
        main_page.check_connection()


@allure.title('Корректный переход к блоку "Карьера" на главной странице сайта')
def test_main_page_element_career(setup_browser):
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


@allure.title('Корректный переход к блоку "О нас" на главной странице сайта')
def test_main_page_element_about_company(setup_browser):
    with allure.step('Открыть главную страницу сайта'):
        main_page = MainPage()
        main_page.open()

    with allure.step('Найти и нажать на элемент "О нас"'):
        main_page.click_about_company()

    with allure.step('Проверить переход к разделу "О нас"'):
        main_page.check_about_company()


@allure.title('Корректный переход к блоку "Блог" на главной странице сайта')
def test_main_page_element_blog(setup_browser):
    with allure.step('Открыть главную страницу сайта'):
        main_page = MainPage()
        main_page.open()

    with allure.step('Найти и нажать на элемент "Блог"'):
        main_page.click_blog()

    with allure.step('Проверить переход к разделу "Блог"'):
        main_page.check_blog()


@allure.title('Корректный переход к блоку "Контакты" на главной странице сайта')
def test_main_page_element_contacts(setup_browser):
    with allure.step('Открыть главную страницу сайта'):
        main_page = MainPage()
        main_page.open()

    with allure.step('Найти и нажать на элемент "Контакты"'):
        main_page.click_contacts()

    with allure.step('Проверить переход к разделу "Контакты"'):
        main_page.check_contacts()


@allure.title('Корректное отображение формы "Оставьте заявку на консультацию" при переходе через блок "Подключение"')
def test_correct_display_consultation_form_via_connection(setup_browser):
    with allure.step('Открыть главную страницу сайта'):
        main_page = MainPage()
        main_page.open()

    with allure.step('Найти и нажать на элемент "Подключение"'):
        main_page.click_connection()

    with allure.step('Найти и нажать на кнопку "Оставить заявку" в разделе "Подключение"'):
        main_page.click_submit_application_via_other_section()

    with allure.step('Проверить появление формы "Оставьте заявку на консультацию"'):
        main_page.check_consultation_form()


@allure.title('Корректное отображение формы "Оставьте заявку на консультацию" при переходе через блок "О нас"')
def test_main_page_element_submit_application(setup_browser):
    with allure.step('Открыть главную страницу сайта'):
        main_page = MainPage()
        main_page.open()

    with allure.step('Найти и нажать на элемент "О нас"'):
        main_page.click_about_company()

    with allure.step('Найти и нажать на кнопку "Оставить заявку" в разделе "О нас"'):
        main_page.click_submit_application_via_other_section()

    with allure.step('Проверить появление формы "Оставьте заявку на консультацию"'):
        main_page.check_consultation_form()


@allure.title('Корректное отображение формы "Оставьте заявку на консультацию" при переходе через блок "Блог"')
def test_main_page_element_blog(setup_browser):
    with allure.step('Открыть главную страницу сайта'):
        main_page = MainPage()
        main_page.open()

    with allure.step('Найти и нажать на элемент "Блог"'):
        main_page.click_blog()

    with allure.step('Найти и нажать на кнопку "Связаться с нами" в разделе "Блог"'):
        main_page.click_submit_application_via_other_section()

    with allure.step('Проверить появление формы "Оставьте заявку на консультацию"'):
        main_page.check_consultation_form()


@allure.title('Корректное отображение формы "Оставьте заявку на консультацию" при переходе через блок "Контакты"')
def test_main_page_element_blog(setup_browser):
    with allure.step('Открыть главную страницу сайта'):
        main_page = MainPage()
        main_page.open()

    with allure.step('Найти и нажать на элемент "Контакты"'):
        main_page.click_contacts()

    with allure.step('Найти и нажать на кнопку "Связаться с нами" в разделе "Контакты"'):
        main_page.click_submit_application_via_other_section()

    with allure.step('Проверить появление формы "Оставьте заявку на консультацию"'):
        main_page.check_consultation_form()


@allure.title('Успешное заполнение и отправка формы "Оставьте заявку на консультацию"')
def test_consultation_form(setup_browser):
    with allure.step('Открыть главную страницу сайта'):
        main_page = MainPage()
        main_page.open()

    with allure.step('Найти и нажать на кнопку "Оставить заявку"'):
        main_page.click_submit_application()

    with allure.step('Заполнить поле "Компания"'):
        consultation_form = ConsultationForm()
        consultation_form.type_company('Technostar')

    with allure.step('Заполнить поле "ФИО"'):
        consultation_form.type_name('Ivanov Ivan Ivanovich')

    with allure.step('Заполнить поле "E-mail"'):
        consultation_form.type_email('test@technostar.ru')

    with allure.step('Заполнить поле "Телефон"'):
        consultation_form.type_phone('89119119191')

    with allure.step('Заполнить поле "Оставьте ваш комментарий"'):
        consultation_form.type_comment('do not distrub')

    with allure.step('Нажать на кнопку "Отправить заявку"'):
        consultation_form.click_send()
