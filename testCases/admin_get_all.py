from selenium.webdriver.common.by import By
import json                         
from pageObjects.AdminCDPage import AdminCDPage
import time

class admin_get_all:
      # self.driver = setup
      # cd = AdminCDPage()
      # cd.textfincedamount()
      # finaced_amount = 78
      print("in the class gettalllllllllll finaced_amount") 


      def __init__(self, driver):
        self.driver = driver

      def  getAll(self):
        print("plan executed in get values")
        self.cds = AdminCDPage(self.driver)
        # panel_all_values_dict = self.cd.get_all_values()
        # result5 = panel_all_values['value_finaced_ammount']
        # result6 = panel_all_values['value_of_downpayment']
        # result7 = panel_all_values['value_of_no_of_month'] 
        # result8 = panel_all_values['value_of_intrest']



        # print("panel_totel payble   =  "  + str(result5))
        # print("panel_principle per rec     =" +str(result6))
        # print("panel_Precuring amount during def = " +str(result7))
        # print("panel_totel reminnig amount during def = " +str(result8))
        self.cds.textfincedamount()
        time.sleep(5)
        # print(self.cd.s)
        self.cds.valuedownp()
        time.sleep(5)
        # print(self.cd.vdp)

        self.cds.valuenofm()
        time.sleep(5)
        # print(self.cd.nfm)
            
        self.cds.valueoftheintrest()
        time.sleep(2)
            
            
        self.cds.panelrecurring()
        time.sleep(2)
        self.cds.panelupfrontfee()
        time.sleep(2)
        self.cds.panelExpectedmonthlypayouttobusiness()
        time.sleep(2)
        self.cds.panelTotalExpectedPayouttoBusiness()
        time.sleep(2)
        self.cds.panelTotalRemainingAmount()
        time.sleep(2)
        self.cds.panelCustomerPayoffAmount()
        time.sleep(2)
        self.cds.panelBusinessExpectedPayoff()
        time.sleep(2)
        self.cds.panelPrincipalAmount()
        time.sleep(2)
        self.cds.panelTotalBalanceRemaining()
        time.sleep(2)
        print(self.cd.panelTotalBalanceRemaining)
            