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
        if number < 12:
           self.busivalue.textdownpaymentamount()
           time.sleep(5)
        else:
          self.busivalue.textdownpaymentamountless12()   
          print("inelsefromdp")
             
        self.busivalue.textCustomerPayoffAmount()
        time.sleep(5)
        self.busivalue.textRemainingExpectedPayout()
        time.sleep(5)

   
        self.busivalue.textExpectedMonthlyPayout()
        time.sleep(5)
        # print(self.cd.nfm)
            
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
            