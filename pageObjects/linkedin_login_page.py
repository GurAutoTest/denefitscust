from selenium.webdriver.common.by import By


class Linkedin_LoginPage:
    # textbox_username_xpath = "/html/body/app-root/div/div/app-login/div/form/div[1]/div[1]/input"
    textbox_username_id = "session_key"

    # button_continue_xpath = "/html/body/app-root/app-login/div[2]/div/form/div[2]/button[1]"
  
    # textbox_password_xpath = "/html/body/app-root/div/div/app-login/div/form/div[1]/div[2]/input"
    textbox_password_id = "session_password"

    button_login_name = "homepage-basic_sign-in-submit-btn"

    # button_logout_drop_xpath = "/html/body/app-root/div/div/app-dashboard/div/div[2]/div[1]/div/div[2]/div/app-profile-drop-down/header/div/div/button"
    # button_logout_xpath = "/html/body/app-root/div/div/app-dashboard/div/div[2]/div[1]/div/div[2]/div/app-profile-drop-down/header/div/div/ul/li[7]/a"
  
    # button_logout_last_xpath = "/html/body/modal-container/div[2]/div/app-logout-confirm/div[2]/div/button[2]"
  

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.NAME, self.button_login_name).click()

    # def clickContinue(self):
    #     self.driver.find_element(By.XPATH, self.button_continue_xpath).click()  

    # def clickLogoutDrop(self):
    #     self.driver.find_element(By.XPATH, self.button_logout_drop_xpath).click()

    # def clickLogout(self):
    #     self.driver.find_element(By.XPATH, self.button_logout_xpath).click()

    # def clickLogoutLast(self):
    #     self.driver.find_element(By.XPATH, self.button_logout_last_xpath).click()
