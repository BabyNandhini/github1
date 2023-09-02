
##class UDF (user define function) -- example page initialze , page open
## call obj for the class
## object function call
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


# declare the class
class OrangeWebsite:
    def __init__(self):
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.driver = webdriver.Chrome()

    def browse_orangeHRM(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(5)

    #testcase 1 login with hrm page valid forgot password menu
    def click_forgot_password(self):
        forgot_password_web_element = self.driver.find_element(By.XPATH, '//*[@class="orangehrm-login-forgot"]')
        forgot_password_web_element.click()
        sleep(3)

    # def user_name_testcase(self,valid ):
    #     user_name_web_element = self.driver.find_element(By.XPATH, '//*[@name="username"]')
    #     if valid:
    #         user_name_web_element.send_keys(" ")
    #     else:
    #         user_name_web_element.send_keys("Admin")
    #     sleep(5)
    #     user_name_web_element.click()
    #     sleep(5)
    # def click_reset_button(self):
    #     reset_password_web_element = self.driver.find_element(By.XPATH, '//*[@type="submit"]')
    #     reset_password_web_element.click()
    #     sleep(3)

    def login_module(self):
        user_name_web_element = self.driver.find_element(By.NAME, "username")
        password_web_element = self.driver.find_element(By.NAME, "password")
        user_name_web_element.send_keys("Admin")
        password_web_element.send_keys("admin123")
        login_web_element = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_web_element.click()
        sleep(3)

    def admin_module(self):
        admin_web_element = self.driver.find_element(By.XPATH, "//a[@href= '/web/index.php/admin/viewAdminModule']")
        admin_web_element.click()
        sleep(3)

    def header_validation_of_page(self):
        header_menu = ['User Management', 'Job', 'Organization', 'Qualifications', 'Nationalities', 'Corporate Branding',
                       'Configuration']
        header_items = self.driver.find_elements(By.XPATH, '//*[@class="oxd-topbar-body-nav-tab-item"]')

        for item in header_items:
            if item.text in header_menu and item.is_displayed():
                print(item.text + ' - option displayed.')
            else:
                print(item.text + ' - option not Displayed.')

    def side_menu_validation_of_page(self):
        side_menu = ['Admin', 'PIM', 'Leave', 'Time', 'Recruitment', 'My Info',
                       'Performance','Dashboard','Directory','Maintenance','Buzz']
        side_items = self.driver.find_elements(By.XPATH, '//*[@class="oxd-main-menu-item-wrapper"]')

        for item in side_items:
            if item.text in side_menu and item.is_displayed():
                print(item.text + ' - option displayed.')
            else:
                print(item.text + ' - option not Displayed.')



obj = OrangeWebsite()
obj.browse_orangeHRM()
# obj.click_forgot_password()
# obj.user_name_testcase(False)
# obj.user_name_testcase(True)
# obj.click_reset_button()
obj.login_module()
obj.admin_module()
obj.header_validation_of_page()
obj.side_menu_validation_of_page()
