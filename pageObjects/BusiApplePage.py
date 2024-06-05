from selenium.webdriver.common.by import By
import json

class BusiApplePage:
    textbox_username_xpath = "/html/body/app-root/app-login/div/div/div[1]/div/div/div/div[3]/div/input"
    button_showpayments_xpath = "/html/body/app-root/app-layout/div/section/div/app-details/div[3]/div[2]/div/button"

    text_financed_amount_xpath = "/html/body/app-root/app-layouts/mat-sidenav-container/mat-sidenav-content/main/app-contract-list/div[1]/div[2]/div[2]/app-contract-details/div/div/div[2]/mat-accordion[1]/mat-expansion-panel/div/div/div/div/div/div[1]/div[1]/div/label[2]/span"
    text_downpayment_amount_xpath = "/html/body/app-root/app-layouts/mat-sidenav-container/mat-sidenav-content/main/app-contract-list/div/div[2]/div[2]/app-contract-details/div/div/div[2]/mat-accordion[1]/mat-expansion-panel/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/h4"
    text_no_of_month_xpath = "/html/body/app-root/app-layouts/mat-sidenav-container/mat-sidenav-content/main/app-contract-list/div/div[2]/div[2]/app-contract-details/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/p/label/span"
    
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
    text_downpayment_amount_xpath = "/html/body/app-root/app-layouts/mat-sidenav-container/mat-sidenav-content/main/app-contract-list/div[1]/div[2]/div[2]/app-contract-details/div/div/div[2]/mat-accordion[1]/mat-expansion-panel/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/h4"
    text_no_of_month_xpath = "/html/body/app-root/app-layouts/mat-sidenav-container/mat-sidenav-content/main/app-contract-list/div/div[2]/div[2]/app-contract-details/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/p/label/span"

    text_new_financed_amount_xpath = "/html/body/div[4]/div[2]/div/mat-dialog-container/app-contract-dialog/div/div[1]/div[1]/div[2]/div[2]/div/input"
    text_new_number_of_month_xpath="/html/body/div[4]/div[2]/div/mat-dialog-container/app-contract-dialog/div/div[1]/div[1]/div[3]/div[1]/input"
    button_action_xpath = "/html/body/app-root/app-layouts/mat-sidenav-container/mat-sidenav-content/main/app-contract-list/div[1]/div[2]/div[2]/app-contract-details/div/div/div[2]/div[1]/div/div[2]/div/div/a/h4"
    button_edit_contract_xpath = "/html/body/app-root/app-layouts/mat-sidenav-container/mat-sidenav-content/main/app-contract-list/div[1]/div[2]/div[2]/app-contract-details/div/div/div[2]/div[1]/div/div[2]/div/div/a/div/div[3]"
    button_edit_contract_continue_xpath="/html/body/div[4]/div[2]/div/mat-dialog-container/app-contract-dialog/div/div[2]/button/span"


 
    text_Customer_Payoff_Amount_xpath = "/html/body/app-root/app-layouts/mat-sidenav-container/mat-sidenav-content/main/app-contract-list/div/div[2]/div[2]/app-contract-details/div/div/div[2]/mat-accordion[1]/mat-expansion-panel/div/div/div/div/div/div[1]/div[2]/div[1]/div[2]"
    text_Remaining_Expected_Payout_xpath ="/html/body/app-root/app-layouts/mat-sidenav-container/mat-sidenav-content/main/app-contract-list/div/div[2]/div[2]/app-contract-details/div/div/div[2]/mat-accordion[1]/mat-expansion-panel/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]"
    text_Paid_to_Business_xpath ="/html/body/app-root/app-layouts/mat-sidenav-container/mat-sidenav-content/main/app-contract-list/div/div[2]/div[2]/app-contract-details/div/div/div[2]/mat-accordion[1]/mat-expansion-panel/div/div/div/div/div/div[1]/div[2]/div[3]/div[2]"
    text_Expected_Monthly_Payout_xpath =  "/html/body/app-root/app-layouts/mat-sidenav-container/mat-sidenav-content/main/app-contract-list/div/div[2]/div[2]/app-contract-details/div/div/div[2]/mat-accordion[1]/mat-expansion-panel/div/div/div/div/div/div[1]/div[2]/div[4]/div[2]"
    text_downpayment_amount_less_xpath = "/html/body/app-root/app-layouts/mat-sidenav-container/mat-sidenav-content/main/app-contract-list/div/div[2]/div[2]/app-contract-details/div/div/div[2]/mat-accordion[1]/mat-expansion-panel/div/div/div/div/div/div[1]/div[1]/div/div[2]/div[1]/h4"
    text_Interest_xpath = "/html/body/app-root/app-layouts/mat-sidenav-container/mat-sidenav-content/main/app-contract-list/div/div[2]/div[2]/app-contract-details/div/div/div[2]/mat-accordion[1]/mat-expansion-panel/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/span[4]/h4/span"
    text_rec_before_def_xpath = "/html/body/app-root/app-layouts/mat-sidenav-container/mat-sidenav-content/main/app-contract-list/div/div[2]/div[2]/app-contract-details/div/div/div[2]/mat-accordion[1]/mat-expansion-panel/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[1]/h4/span[1]"

    text_rec_after_def_xpath = "/html/body/app-root/app-layouts/mat-sidenav-container/mat-sidenav-content/main/app-contract-list/div/div[2]/div[2]/app-contract-details/div/div/div[2]/mat-accordion[1]/mat-expansion-panel/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/h4/span[1]"

    # text_remaining_expected_payout ="/html/body/app-root/app-layouts/mat-sidenav-container/mat-sidenav-content/main/app-contract-list/div/div[2]/div[2]/app-contract-details/div/div/div[2]/mat-accordion[1]/mat-expansion-panel/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]"
    # text_paid_to_business = "/html/body/app-root/app-layouts/mat-sidenav-container/mat-sidenav-content/main/app-contract-list/div/div[2]/div[2]/app-contract-details/div/div/div[2]/mat-accordion[1]/mat-expansion-panel/div/div/div/div/div/div[1]/div[2]/div[3]/div[2]"
    # text_expected_monthly_payout = "/html/body/app-root/app-layouts/mat-sidenav-container/mat-sidenav-content/main/app-contract-list/div/div[2]/div[2]/app-contract-details/div/div/div[2]/mat-accordion[1]/mat-expansion-panel/div/div/div/div/div/div[1]/div[2]/div[4]/div[2]"
    text_donated_amount_xpath ="/html/body/app-root/app-layouts/mat-sidenav-container/mat-sidenav-content/main/app-contract-list/div/div[2]/div[2]/app-contract-details/div/div/div[2]/mat-accordion[1]/mat-expansion-panel/div/div/div/div/div/div[1]/div[2]/div[5]/div[2]/span"
    text_total_balance_remaning_xpath ="/html/body/app-root/app-layouts/mat-sidenav-container/mat-sidenav-content/main/app-contract-list/div/div[2]/div[2]/app-contract-details/div/div/div[2]/mat-accordion[1]/mat-expansion-panel/div/div/div/div/div/div[1]/div[2]/div[8]/div[2]"







    def __init__(self, driver):
        self.driver = driver


    def textfinacedamount(self):
        self.value_finaced_ammount=(self.driver.find_element(By.XPATH, self.text_financed_amount_xpath).text)
        self.value_finaced_ammount = self.value_finaced_ammount.replace("$","").replace(",","")
        self.value_finaced_ammount = float(self.value_finaced_ammount)
        self.value_finaced_ammount = round(self.value_finaced_ammount)
        print("round amount")
        print(self.value_finaced_ammount)
    
        # self.text_finaced_ammount=(self.driver.find_element(By.XPATH, self.text_financed_amount_xpath).text)
        # print(self.text_finaced_ammount)
  




    # def textnewfinacedamount(self):
    #     self.text_new_finaced_ammount=(self.driver.find_element(By.XPATH, self.text_new_financed_amount_xpath).text)
    #     print(self.text_finaced_ammount)
  
    def setnewfinacedamount(self, newfinacedammount):
        self.driver.find_element(By.XPATH, self.text_financed_amount_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_financed_amount_xpath).send_keys(newfinacedammount)
  
  
    def textdownpaymentamount(self):
        self.text_downpayment_amount=(self.driver.find_element(By.XPATH, self.text_downpayment_amount_xpath).text)
        self.text_downpayment_amount = self.text_downpayment_amount.replace("$","").replace(",","")
        self.text_downpayment_amount = float(self.text_downpayment_amount)
        self.text_downpayment_amount = round(self.text_downpayment_amount)
        print(self.text_downpayment_amount)   
         
    def textdownpaymentamountless12(self):
        self.text_downpayment_amount_less=(self.driver.find_element(By.XPATH, self.text_downpayment_amount_less_xpath).text)
        print(self.text_downpayment_amount_less)     
    
    def textnumberofmonth(self):
        self.text_number_of_month=(self.driver.find_element(By.XPATH, self.text_no_of_month_xpath).text)
        self.text_number_of_month = self.text_number_of_month.replace("$","").replace(",","")
        self.text_number_of_month = float(self.text_number_of_month)
        self.text_number_of_month = round(self.text_number_of_month)
        print(self.text_number_of_month)    
    
    
    def textCustomerPayoffAmount(self):
        self.text_Customer_Payoff_Amount=(self.driver.find_element(By.XPATH, self.text_Customer_Payoff_Amount_xpath).text)
        self.text_Customer_Payoff_Amount = self.text_Customer_Payoff_Amount.replace("$","").replace(",","")
        self.text_Customer_Payoff_Amount = float(self.text_Customer_Payoff_Amount)
        self.text_Customer_Payoff_Amount = round(self.text_Customer_Payoff_Amount)

        print("round amount")
        print(self.text_Customer_Payoff_Amount)    
    
    def textRemainingExpectedPayout(self):
        self.text_Remaining_Expected_Payout=(self.driver.find_element(By.XPATH, self.text_Remaining_Expected_Payout_xpath).text)
        self.text_Remaining_Expected_Payout = self.text_Remaining_Expected_Payout.replace("$","").replace(",","")
        self.text_Remaining_Expected_Payout = float(self.text_Remaining_Expected_Payout)
        self.text_Remaining_Expected_Payout = round(self.text_Remaining_Expected_Payout)
        print("round amount")

        print(self.text_Remaining_Expected_Payout)    
    
    def textPaidtoBusiness(self):
        self.text_Paid_to_Business=(self.driver.find_element(By.XPATH, self.text_Paid_to_Business_xpath).text)
        self.text_Paid_to_Business = self.text_Paid_to_Business.replace("$","").replace(",","")
        self.text_Paid_to_Business = float(self.text_Paid_to_Business)
        self.text_Paid_to_Business = round(self.text_Paid_to_Business)
        print(self.text_Paid_to_Business)    
        

    def textInterest(self , number):
        if number > 12:
           self.text_Interest=(self.driver.find_element(By.XPATH, self.text_Interest_xpath).text)
        #    self.text_Interest = self.text_Interest.replace("$","").replace(",","")
        #    self.text_Interest = float(self.text_Interest)
        #    self.text_Interest = round(self.text_Interest)
           print(self.text_Interest)    
        else :
           self.text_Interest = "no intraest"
           print(self.text_Interest)    
            

            

              
          
    
        # 'text_downpayment_amount': self.text_downpayment_amount , 'text_downpayment_amount_less': self.text_downpayment_amount_less ,
    def textExpectedMonthlyPayout(self):
        self.text_Expected_Monthly_Payout=(self.driver.find_element(By.XPATH, self.text_Expected_Monthly_Payout_xpath).text)
        self.text_Expected_Monthly_Payout = self.text_Expected_Monthly_Payout.replace("$","").replace(",","")
        self.text_Expected_Monthly_Payout = float(self.text_Expected_Monthly_Payout)
        self.text_Expected_Monthly_Payout = round(self.text_Expected_Monthly_Payout)
        print(self.text_Expected_Monthly_Payout)
        # return {'value_finaced_ammount': self.value_finaced_ammount ,  
        #         'text_number_of_month' : self.text_number_of_month ,  'text_Customer_Payoff_Amount': self.text_Customer_Payoff_Amount , } 

    def textrecbeforedef(self):
        self.text_rec_before_def=(self.driver.find_element(By.XPATH, self.text_rec_before_def_xpath).text)
        self.text_rec_before_def = self.text_rec_before_def.replace("$","").replace(",","")
        self.text_rec_before_def = float(self.text_rec_before_def)
        self.text_rec_before_def = round(self.text_rec_before_def)
        print(self.text_rec_before_def) 
    
    def textrecafterdef(self , number):
        if number > 12:
            self.text_rec_after_def=(self.driver.find_element(By.XPATH, self.text_rec_after_def_xpath).text)
            self.text_rec_after_def = self.text_rec_after_def.replace("$","").replace(",","")
            self.text_rec_after_def = float(self.text_rec_after_def)
            self.text_rec_after_def = round(self.text_rec_after_def)
            print(self.text_rec_after_def) 
        else :
            self.text_rec_after_def = "no after def"
            print(self.text_rec_after_def) 
              

  
  
  
    def textdonatedamount(self):
        self.text_donated_amount=(self.driver.find_element(By.XPATH, self.text_donated_amount_xpath).text)
        self.text_donated_amount = self.text_donated_amount.replace("$","").replace(",","")
        self.text_donated_amount = float(self.text_donated_amount)
        self.text_donated_amount = round(self.text_donated_amount)
        print(self.text_donated_amount) 
    def texttotalbalanceremaning(self):
        self.text_total_balance_remaning=(self.driver.find_element(By.XPATH, self.text_total_balance_remaning_xpath).text)
        self.text_total_balance_remaning = self.text_total_balance_remaning.replace("$","").replace(",","")
        self.text_total_balance_remaning = float(self.text_total_balance_remaning)
        self.text_total_balance_remaning = round(self.text_total_balance_remaning)
        print(self.text_total_balance_remaning) 
    

    def textnewnumberofmonth(self):
        self.text_new_number_of_month=(self.driver.find_element(By.ID, self.text_new_number_of_month_xpath).text)
        print(self.text_new_number_of_month)  


    def setnewnumberofmonth(self, newnumberofmonth):
        self.driver.find_element(By.XPATH, self.text_new_number_of_month_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_new_number_of_month_xpath).send_keys(newnumberofmonth)  

    def clickeditcontinue(self):
        self.driver.find_element(By.XPATH, self.button_edit_contract_continue_xpath).click()  


    def clickaction(self):
        self.driver.find_element(By.XPATH, self.button_action_xpath).click()  


    def clickeditcontract(self):
        self.driver.find_element(By.XPATH, self.button_edit_contract_xpath).click()  
































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
