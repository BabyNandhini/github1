from selenium import webdriver
# from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.common.by import By


# initialize
class OrangeWebsite:
    def __init__(self):
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.driver = webdriver.Chrome()

    def browse_orangeHRM(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(6)

    #testcase 1 login with valid username & password
    def login_testcases(self, valid):
        user_name_web_element = self.driver.find_element(By.NAME, "username")
        password_web_element = self.driver.find_element(By.NAME, "password")
        user_name_web_element.send_keys("Admin")
        if valid:
            password_web_element.send_keys("admin123")
        else:
            password_web_element.send_keys("adminssj")
        sleep(5)
        login_web_element = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_web_element.click()
        sleep(3)

#//a[@class='oxd-main-menu-item active']
    def click_the_PIM(self):
        user_name_web_element = self.driver.find_element(By.XPATH,
                                                         "//a[@href='/web/index.php/pim/viewPimModule']")
        user_name_web_element.click()
        sleep(3)

# //*[@class='oxd-icon bi-plus oxd-button-icon']

    def click_the_add(self):
        user_name_web_element = self.driver.find_element(By.XPATH,
                                                         "//*[@class='oxd-icon bi-plus oxd-button-icon']")
        user_name_web_element.click()
        sleep(3)

    def add_employee(self):
        add_employee_web_element = self.driver.find_element(By.XPATH, "//input[@name='firstName']")
        add_employee_web_element.send_keys("Ajith")
        sleep(5)
        add_employee_web_element = self.driver.find_element(By.XPATH, "//input[@name='middleName']")
        add_employee_web_element.send_keys("sankar")
        sleep(3)
        add_employee_web_element = self.driver.find_element(By.XPATH, "//input[@name='lastName']")
        add_employee_web_element.send_keys("M")
        sleep(3)
        save_web_element = self.driver.find_element(By.XPATH, "//*[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")
        save_web_element.click()
        sleep(3)

    def delete_test_case(self):
        delete_item = self.driver.find_element(By.XPATH, '//button[@class="oxd-icon-button oxd-table-cell-action-space"]')
        delete_item.click()
        sleep(5)
        delete_item = self.driver.find_element(By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin"]')
        delete_item.click()
        sleep(5)

    def edit_test_case(self):
        edit_item = self.driver.find_element(By.XPATH, '//i[@class="oxd-icon bi-pencil-fill"]')
        edit_item.click()
        sleep(5)

    def edit_personal_details(self):
        edit_employee_web_element = self.driver.find_element(By.XPATH, "//input[@name='firstName']")
        edit_employee_web_element.click()
        edit_employee_web_element.clear()
        edit_employee_web_element.send_keys("Ajith")
        sleep(5)
        edit_employee_web_element = self.driver.find_element(By.XPATH, "//input[@name='middleName']")
        edit_employee_web_element.click()
        edit_employee_web_element.clear()
        edit_employee_web_element.send_keys("sankar")
        sleep(5)
        edit_employee_web_element = self.driver.find_element(By.XPATH, "//input[@name='lastName']")
        edit_employee_web_element.click()
        edit_employee_web_element.clear()
        edit_employee_web_element.send_keys("M")
        sleep(5)
        nickname_web_element = self.driver.find_element(By.XPATH, '//input[@fdprocessedid="48pggo"]')
        nickname_web_element.send_keys(joe)
        sleep(3)
        other_id_web_element = self.driver.find_element(By.XPATH, '//input[@fdprocessedid="wulz1c"]')
        other_id_web_element.send_keys("0334")
        sleep(3)


obj = OrangeWebsite()
obj.browse_orangeHRM()
# obj.login_testcase(False)
obj.login_testcases(True)
obj.click_the_PIM()
# obj.click_the_add()
# obj.add_employee()
obj.delete_test_case()
obj.edit_test_case()
obj.edit_personal_details()