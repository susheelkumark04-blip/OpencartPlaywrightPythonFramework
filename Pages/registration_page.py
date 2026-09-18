from playwright.sync_api import Page

class RegistrationPage:
    '''page object model class for registration page, This class contains
    element locators and methods(actions) to intract with registration form.'''


    def __init__(self, page: Page):
        self.Page = page

        # ===locators===
        # input fields
        self.txt_firstname = page.locator("//input[@id='input-firstname']")
        self.txt_lastname = page.locator("//input[@id='input-lastname']")
        self.txt_email = page.locator("#input-email")
        self.txt_phone = page.locator("#input-telephone")
        self.txt_password = page.locator("//input[@id='input-password']")
        self.txt_confirm_password = page.locator("#input-confirm")

        #---checkbox and buttons
        self.chk_policy = page.locator("input[name='agree']")
        self.continue_button = page.locator("input[value='Continue']")

        #--confirmation message displayed after successful registration--
        self.msg_confirmation = page.locator("//h1[normalize-space()='Your Account Has Been Created!']")

        # ----Action Methods-----

    def set_first_name(self,fname:str ):
         self.txt_firstname.fill(fname)

    def set_last_name(self,lname:str ):
        self.txt_lastname.fill(lname)

    def set_email(self,email:str):
        self.txt_email.fill(email)

    def set_phone(self,phone:str):
        self.txt_phone.fill(phone)

    def set_password(self,password:str):
        self.txt_password.fill(password)

    def set_confirm_password(self,password:str):
        self.txt_confirm_password.fill(password)

    def check_policy(self):
        self.chk_policy.check()

    def continue_button(self):
        self.continue_button.click()

    def get_msg_confirmation(self):
        return self.msg_confirmation




