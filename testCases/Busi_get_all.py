from selenium.webdriver.common.by import By
import json
from pageObjects.BusiApplePage import BusiApplePage
import time


class Busi_get_all:
    # self.driver = setup
    # cd = AdminCDPage()
    # cd.textfincedamount()
    # finaced_amount = 78
    print("in the class gettalllllllllll busi get")

    def __init__(self, driver):
        self.driver = driver

    def getAll(self):
        print("plan executed in get values")
        self.busivalue = BusiApplePage(self.driver)
        # panel_all_values_dict = self.cd.get_all_values()
        # result5 = panel_all_values['value_finaced_ammount']
        # result6 = panel_all_values['value_of_downpayment']
        # result7 = panel_all_values['value_of_no_of_month']
        # result8 = panel_all_values['value_of_intrest']

        # print("panel_totel payble   =  "  + str(result5))
        # print("panel_principle per rec     =" +str(result6))
        # print("panel_Precuring amount during def = " +str(result7))
        # print("panel_totel reminnig amount during def = " +str(result8))
        self.busivalue.textfinacedamount()
        time.sleep(5)
        self.busivalue.textnumberofmonth()
        time.sleep(5)
        number = int(self.busivalue.text_number_of_month)
        # if number < 12:
        self.busivalue.textdownpaymentamount()
        time.sleep(5)
        #    return {'text_downpayment_amount': self.busivalue.text_downpayment_amount}
        # else:
        self.busivalue.textdownpaymentamountless12()
        print("inelsefromdp")
        #   return{'text_downpayment_amount_less': self.busivalue.text_downpayment_amount_less}
        self.busivalue.textCustomerPayoffAmount()
        time.sleep(5)
        self.busivalue.textRemainingExpectedPayout()
        time.sleep(5)

        self.busivalue.textExpectedMonthlyPayout()
        time.sleep(5)

        self.busivalue.textPaidtoBusiness()
        time.sleep(5)
        

        self.busivalue.textrecbeforedef()
        time.sleep(5)
        self.busivalue.textrecafterdef()
        time.sleep(5)



        self.busivalue.texttotalbalanceremaning()
        time.sleep(5)
        self.busivalue.textdonatedamount()
        time.sleep(5)
        self.busivalue.textInterest()
        time.sleep(5)
        print(self.busivalue.value_finaced_ammount)


        return {'value_finaced_ammount': self.busivalue.value_finaced_ammount ,'text_downpayment_amount': self.busivalue.text_downpayment_amount,  'text_downpayment_amount_less': self.busivalue.text_downpayment_amount_less,
                'text_Interest':self.busivalue.text_Interest,  'text_number_of_month' : self.busivalue.text_number_of_month ,  'text_Customer_Payoff_Amount': self.busivalue.text_Customer_Payoff_Amount ,'textRemainingExpectedPayout' :
                self.busivalue.text_Remaining_Expected_Payout ,'textExpectedMonthlyPayout' : self.busivalue.text_Expected_Monthly_Payout,
                  'texttotalbalanceremaning' : self.busivalue.text_total_balance_remaning ,'text_Paid_to_Business':self.busivalue.text_Paid_to_Business
               , 'textdonatedamount': self.busivalue.text_donated_amount , 'textrecbeforedef' : self.busivalue.text_rec_before_def , 'textrecafterdef' : self.busivalue.text_rec_after_def} 


        # self.busivalue.valueoftheintrest()
        # time.sleep(2)

        # self.busivalue.panelrecurring()
        # time.sleep(2)
        # self.busivalue.panelupfrontfee()
        # time.sleep(2)
        # self.busivalue.panelExpectedmonthlypayouttobusiness()
        # time.sleep(2)
        # self.busivalue.panelTotalExpectedPayouttoBusiness()
        # time.sleep(2)
        # self.busivalue.panelTotalRemainingAmount()
        # time.sleep(2)
        # self.busivalue.panelCustomerPayoffAmount()
        # time.sleep(2)
        # self.busivalue.panelBusinessExpectedPayoff()
        # time.sleep(2)
        # self.busivalue.panelPrincipalAmount()
        # time.sleep(2)
        # self.busivalue.panelTotalBalanceRemaining()
        # time.sleep(2)
        # print(self.cd.panelTotalBalanceRemaining)


    def getnewvalues(self):

        print("edit function")
        self.editbusivalue = BusiApplePage(self.driver)

        self.editbusivalue.clickaction()
        time.sleep(2)
        self.editbusivalue.clickContinue()
        time.sleep(2)
        self.editbusivalue.textnewfinacedamount()
        time.sleep(5)
