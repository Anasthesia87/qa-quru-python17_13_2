from selene import browser, be


class ConsultationForm:
    def __init__(self):
        self.company = browser.element('#form_text_7_2')
        self.name = browser.element('#form_text_8_2')
        self.email = browser.element('#form_email_9_2')
        self.phone = browser.element('#form_text_10_2')
        self.comment = browser.element('#form_textarea_11_2')
        self.send = browser.element('#call-form > div > form > label > button')

    def type_company(self, value):
        self.company.click().should(be.blank)
        self.company.type(value)

    def type_name(self, value):
        self.name.click().should(be.blank)
        self.name.type(value)

    def type_email(self, value):
        self.email.click().should(be.blank)
        self.email.type(value)

    def type_phone(self, value):
        self.phone.click().should(be.blank)
        self.phone.type(value)

    def type_comment(self, value):
        self.comment.click().should(be.blank)
        self.comment.type(value)

    def click_send(self):
        self.send().click()
