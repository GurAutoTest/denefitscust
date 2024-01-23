from selenium.webdriver.common.by import By
import json

class AdminCDPage:
    # textbox_username_xpath = "/html/body/app-root/div/div/app-login/div/form/div[1]/div[1]/input"
    button_showpayments_xpath = "/html/body/app-root/app-layout/div/section/div/app-details/div[3]/div[2]/div/button"

    Text_finced_amount_xpath = "/html/body/app-root/app-layout/div/section/div/app-details/div[3]/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div[2]/h6"
    value_downp_amount_xpath = "/html/body/app-root/app-layout/div/section/div/app-details/div[3]/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div[3]/h6"
    value_no_of_month_xpath = "/html/body/app-root/app-layout/div/section/div/app-details/div[3]/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div[6]/h6"
    value_intrest_xpath = "after_deferred_interest_rate"
    
    # # textbox_password_xpath = "/html/body/app-root/div/div/app-login/div/form/div[1]/div[2]/input"
    # textbox_password_xpath = "/html/body/app-root/app-login/div[2]/div/form/div[1]/div/input"

    # button_login_xpath = "/html/body/app-root/app-login/div[2]/div/form/div[2]/button[1]"

    # button_logout_drop_xpath = "/html/body/app-root/div/div/app-dashboard/div/div[2]/div[1]/div/div[2]/div/app-profile-drop-down/header/div/div/button"
    # button_logout_xpath = "/html/body/app-root/div/div/app-dashboard/div/div[2]/div[1]/div/div[2]/div/app-profile-drop-down/header/div/div/ul/li[7]/a"   
    # button_logout_last_xpath = "/html/body/modal-container/div[2]/div/app-logout-confirm/div[2]/div/button[2]"
 

    def __init__(self, driver):
        self.driver = driver

    # def setUserName(self, username):
    #     self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
    #     self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    # def setPassword(self, password):
    #     self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
    #     self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickShowPayments(self):
        self.driver.find_element(By.XPATH, self.button_showpayments_xpath).click()

    def textfincedamount(self):
        self.s=(self.driver.find_element(By.XPATH, self.Text_finced_amount_xpath).text)
        print(self.s)
    def valuedownp(self):
        self.vdp=(self.driver.find_element(By.XPATH, self.value_downp_amount_xpath).text)
        print(self.vdp)    
    
    def valuenofm(self):
        self.nfm=(self.driver.find_element(By.XPATH, self.value_no_of_month_xpath).text)
        print(self.nfm)    
    def valueoftheintrest(self):
        self.intpanel=(self.driver.find_element(By.ID, self.value_intrest_xpath).text)
        print(self.intpanel)

    # def clickLogoutDrop(self):
    #     self.driver.find_element(By.XPATH, self.button_logout_drop_xpath).click()

    # def clickLogout(self):
    #     self.driver.find_element(By.XPATH, self.button_logout_xpath).click()

    # def clickLogoutLast(self):
    #     self.driver.find_element(By.XPATH, self.button_logout_last_xpath).click()
