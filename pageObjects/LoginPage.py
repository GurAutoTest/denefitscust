from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_xpath = "/html/body/app-root/div/div/app-login/div/form/div[1]/div[1]/input"
    textbox_password_xpath = "/html/body/app-root/div/div/app-login/div/form/div[1]/div[2]/input"
    button_login_xpath = "/html/body/app-root/div/div/app-login/div/form/div[2]/button[1]"
    button_logout_drop_xpath = "/html/body/app-root/div/div/app-dashboard/div/div[2]/div[1]/div/div[2]/div/app-profile-drop-down/header/div/div/button"
    button_logout_xpath = "/html/body/app-root/div/div/app-dashboard/div/div[2]/div[1]/div/div[2]/div/app-profile-drop-down/header/div/div/ul/li[7]/a"
    print("yyyyyyyyyy")
    button_logout_last_xpath = "/html/body/modal-container/div[2]/div/app-logout-confirm/div[2]/div/button[2]"
    print("Dddddddddddd")

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogoutDrop(self):
        self.driver.find_element(By.XPATH, self.button_logout_drop_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()

    def clickLogoutLast(self):
        self.driver.find_element(By.XPATH, self.button_logout_last_xpath).click()
