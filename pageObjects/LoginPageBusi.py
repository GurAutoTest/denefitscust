from selenium.webdriver.common.by import By


class LoginPageBusi:
    # textbox_username_xpath = "/html/body/app-root/div/div/app-login/div/form/div[1]/div[1]/input"
    textbox_username_xpath = "/html/body/app-root/app-login/div/div/div[1]/div/div/div/div[3]/div/input"

    button_continue_xpath = "/html/body/app-root/app-login/div/div/div[1]/div/div/div/div[4]/button[1]"
  
    # textbox_password_xpath = "/html/body/app-root/div/div/app-login/div/form/div[1]/div[2]/input"
    textbox_password_xpath = "/html/body/app-root/app-login/div/div/div[1]/div/div/div/form/div[2]/div/input"

    button_login_xpath = "/html/body/app-root/app-login/div/div/div[1]/div/div/div/form/div[3]/button"

    button_logout_drop_xpath = "/html/body/app-root/div/div/app-dashboard/div/div[2]/div[1]/div/div[2]/div/app-profile-drop-down/header/div/div/button"
    button_logout_xpath = "/html/body/app-root/div/div/app-dashboard/div/div[2]/div[1]/div/div[2]/div/app-profile-drop-down/header/div/div/ul/li[7]/a"
  
    button_logout_last_xpath = "/html/body/modal-container/div[2]/div/app-logout-confirm/div[2]/div/button[2]"
    
    button_Payment_plans_xpath = "/html/body/app-root/app-layouts/mat-sidenav-container/mat-sidenav/div/mat-nav-list/div[2]/app-sidemenu[3]/mat-list-item/div/div[2]/a"
   
    button_Manage_contracts_xpath ="/html/body/app-root/app-layouts/mat-sidenav-container/mat-sidenav/div/mat-nav-list/div[2]/app-sidemenu[3]/div/div/app-sidemenu[1]/mat-list-item/div/div[2]/a"
    button_full_payment_plan_xpath = "/html/body/app-root/app-layouts/mat-sidenav-container/mat-sidenav-content/main/app-contract-list/div/div[2]/div[2]/app-contract-details/div/div/div[2]/mat-accordion[1]/mat-expansion-panel/mat-expansion-panel-header/span[1]/mat-panel-title"
  

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

    def clickContinue(self):
        self.driver.find_element(By.XPATH, self.button_continue_xpath).click()  

    def clickLogoutDrop(self):
        self.driver.find_element(By.XPATH, self.button_logout_drop_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()

    def clickLogoutLast(self):
        self.driver.find_element(By.XPATH, self.button_logout_last_xpath).click()
    def clickPaymentPlans(self):
        self.driver.find_element(By.XPATH, self.button_Payment_plans_xpath).click()
    def clickManagecontracts(self):
        self.driver.find_element(By.XPATH, self.button_Manage_contracts_xpath).click()
    def clickFullPaymentPlanDetails(self):
        self.driver.find_element(By.XPATH, self.button_full_payment_plan_xpath).click()
