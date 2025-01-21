<h1 align="center">Проект автоматизации <a href="https://spectrumdata.ru">сайта</a> компании SpectrumData</h1>

### Описание:
Было разработано несколько тест-кейсов:
- [x] Проверка возможности перехода через главную страницу к разным информационным блокам
- [x] Проверка работы кнопки "Вход" на главной странице сайта
- [x] Проверка работы кнопки "Оставить заявку" на главной странице сайта
- [x] Проверка отображения формы "Оставьте заявку на консультацию" при переходе из разных информационных блоков
- [x] Проверка заполнения формы "Оставьте заявку на консультацию"

Кейсы реализованы основе шаблона PageObject

## Используемый стек технологий и инструментов
|                          Python                                |                          Pytest                                |                              Selene                              |                          Selenoid                       |                       Allure                          |                      Allure TestOps                   |                         Git                                |                           Jenkins                              |                        Telegram                        |
|:--------------------------------------------------------------:|:--------------------------------------------------------------:|:----------------------------------------------------------------:|:-------------------------------------------------------:|:-----------------------------------------------------:|:-----------------------------------------------------:|:----------------------------------------------------------:|:--------------------------------------------------------------:|:------------------------------------------------------:|
|<img src="sources/python-original.svg" height="45" width="45" />|<img src="sources/pytest-original.svg" height="55" width="55" />|<img src="sources/selenium-original.svg" height="40" width="40" />|<img src="sources/selenoid.svg" height="50" width="50" />|<img src="sources/allure.svg" height="40" width="40" />|<img src="sources/TestOps.svg" height="45" width="45"/>|<img src="sources/git-original.svg" height="40" width="40"/>|<img src="sources/jenkins-original.svg" height="45" width="45"/>|<img src="sources/telegram.svg" height="35" width="35"/>|          

## Запуск автотестов
### На Jenkins реализован параметризованный запуск тестов:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest tests --browser_version=${BROWSER_VERSION} --browser_name=${BROWSER_NAME}
```
<img width="1200" src="sources/jenkins-biuid.png" />

          
                                                        

