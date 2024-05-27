from selenium.webdriver.common.by import By
import json

class BusiApplePage:
    textbox_username_xpath = "/html/body/app-root/app-login/div/div/div[1]/div/div/div/div[3]/div/input"
    button_showpayments_xpath = "/html/body/app-root/app-layout/div/section/div/app-details/div[3]/div[2]/div/button"

    text_financed_amount_xpath = "/html/body/app-root/app-layouts/mat-sidenav-container/mat-sidenav-content/main/app-contract-list/div[1]/div[2]/div[2]/app-contract-details/div/div/div[2]/mat-accordion[1]/mat-expansion-panel/div/div/div/div/div/div[1]/div[1]/div/label[2]/span"
    text_downpayment_amount_xpath = "/html/body/app-root/app-layouts/mat-sidenav-container/mat-sidenav-content/main/app-contract-list/div[1]/div[2]/div[2]/app-contract-details/div/div/div[2]/mat-accordion[1]/mat-expansion-panel/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/h4"
    text_no_of_month_xpath = "/html/body/app-root/app-layouts/mat-sidenav-container/mat-sidenav-content/main/app-contract-list/div[1]/div[2]/div[2]/app-contract-details/div/div/div[2]/mat-accordion[1]/mat-expansion-panel/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/h4"
    
    # value_no_of_month_xpath = "/html/body/app-root/app-layout/div/section/div/app-details/div[3]/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div[6]/h6"
    id_panel_financed_amount="financed_amount"
    id_panel_down_payment="downpayment_amount"
    value_no_of_month_id = "number_of_payments"
    value_intrest_id = "interest_rate"
    id_panelrecurring = "recurring_amount"
    id_panelupfrontfee = "upfront_fee"
    id_panelExpectedmonthlypayouttobusiness = "expected_monthly_pay_to_doctor"
    id_panelTotalExpectedPayouttoBusiness = "doctor_expected_payout"
    id_panelTotalRemainingAmount = "remaining_amount"
    id_panelCustomerPayoffAmount = "patient_payoff_amount"
    id_panelBusinessExpectedPayoff = "doctor_expected_payoff"
    id_panelPrincipalAmount = "recurring_without_interest"
    id_panelTotalBalanceRemaining = "total_balance_remaining"
    
    value_intrest_xpath = "after_deferred_interest_rate"
    
    # textbox_password_xpath = "/html/body/app-root/div/div/app-login/div/form/div[1]/div[2]/input"
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
    # def get_all_values(self ):
        
        # button_showpayments_xpath = "/html/body/app-root/app-layout/div/section/div/app-details/div[3]/div[2]/div/button"

        # Text_finced_amount_xpath = "/html/body/app-root/app-layout/div/section/div/app-details/div[3]/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div[2]/h6"
        # value_downp_amount_xpath = "/html/body/app-root/app-layout/div/section/div/app-details/div[3]/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div[3]/h6"
        # # value_no_of_month_xpath = "/html/body/app-root/app-layout/div/section/div/app-details/div[3]/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div[6]/h6"
        # value_no_of_month_id = "number_of_payments"
        # value_intrest_id = "interest_rate"
        # id_panelrecurring = "recurring_amount"
        # id_panelupfrontfee = "upfront_fee"
        # id_panelExpectedmonthlypayouttobusiness = "expected_monthly_pay_to_doctor"
        # id_panelTotalExpectedPayouttoBusiness = "doctor_expected_payout"
        # id_panelTotalRemainingAmount = "remaining_amount"
        # id_panelCustomerPayoffAmount = "patient_payoff_amount"
        # id_panelBusinessExpectedPayoff = "doctor_expected_payoff"
        # id_panelPrincipalAmount = "recurring_without_interest"
        # id_panelTotalBalanceRemaining = "total_balance_remaining"

    # def clickShowPayments(self):
    #     self.driver.find_element(By.XPATH, self.button_showpayments_xpath).click()

    def textfinacedamount(self):
        self.value_finaced_ammount=(self.driver.find_element(By.XPATH, self.text_financed_amount_xpath).text)
        print(self.value_finaced_ammount)
    def textdownpaymentamount(self):

        self.text_downpayment_amount=(self.driver.find_element(By.XPATH, self.text_downpayment_amount_xpath).text)
        print(self.text_downpayment_amount)    
    
    def textnumberofmonth(self):
        self.text_number_of_month=(self.driver.find_element(By.ID, self.text_no_of_month_xpath).text)
        print("errrorhare")
        print(self.text_number_of_month)    
    # def valueoftheintrest(self):
    #     self.value_of_intrest=(self.driver.find_element(By.ID, self.value_intrest_id).text)
    #     print(self.value_of_intrest)

    # def clickLogoutDrop(self):
    #     self.driver.find_element(By.XPATH, self.button_logout_drop_xpath).click()

    # def clickLogout(self):
    #     self.driver.find_element(By.XPATH, self.button_logout_xpath).click()

    # def clickLogoutLast(self):
    #     self.driver.find_element(By.XPATH, self.button_logout_last_xpath).click()
    # def panelrecurring(self):
    #     self.value_panelrecurring=(self.driver.find_element(By.ID, self.id_panelrecurring).text)
    #     print(self.value_panelrecurring)
    # def panelupfrontfee(self):
    #     self.value_panelupfrontfee=(self.driver.find_element(By.ID, self.id_panelupfrontfee).text)
    #     print(self.value_panelupfrontfee)
    # def panelExpectedmonthlypayouttobusiness(self):
    #     self.value_panelExpectedmonthlypayouttobusiness=(self.driver.find_element(By.ID, self.id_panelExpectedmonthlypayouttobusiness).text)
    #     print(self.value_panelExpectedmonthlypayouttobusiness)
    # def panelTotalExpectedPayouttoBusiness(self):
    #     self.value_panelTotalExpectedPayouttoBusiness=(self.driver.find_element(By.ID, self.id_panelTotalExpectedPayouttoBusiness).text)
    #     print(self.value_panelTotalExpectedPayouttoBusiness)
    # def panelTotalRemainingAmount(self):
    #     self.value_panelTotalRemainingAmount=(self.driver.find_element(By.ID, self.id_panelTotalRemainingAmount).text)
    #     print(self.value_panelTotalRemainingAmount)
    # def panelCustomerPayoffAmount(self):
    #     self.value_panelCustomerPayoffAmount=(self.driver.find_element(By.ID, self.id_panelCustomerPayoffAmount).text)
    #     print(self.value_panelCustomerPayoffAmount)
    # def panelBusinessExpectedPayoff(self):
    #     self.value_panelBusinessExpectedPayoff=(self.driver.find_element(By.ID, self.id_panelBusinessExpectedPayoff).text)
    #     print(self.value_panelBusinessExpectedPayoff)
    # def panelPrincipalAmount(self):
    #     self.value_panelPrincipalAmount=(self.driver.find_element(By.ID, self.id_panelPrincipalAmount).text)
    #     print(self.value_panelPrincipalAmount)
    # def panelTotalBalanceRemaining(self):
    #     self.value_panelTotalBalanceRemaining=(self.driver.find_element(By.ID, self.id_panelTotalBalanceRemaining).text)  
    #     print(self.value_panelTotalBalanceRemaining)
    #     return {'value_finaced_ammount': value_finaced_ammount , 'value_of_downpayment':value_of_downpayment , 'value_of_no_of_month': value_of_no_of_month , 'value_of_intrest' : value_of_intrest} 
