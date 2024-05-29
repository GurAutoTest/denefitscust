import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AdminCDPage import AdminCDPage
from testCases.admin_get_all import  admin_get_all
from testCases.calculate import calculate
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time


class Test_001_Login:
    # baseURL = "https://testcustomer.denefits.com"
    baseURL = "https://testadminv2.denefits.com/app/contracts/75901"
    username = "gurdeep.singh@bridgingtech.com"
    password = "Gur@22aug"
    logger = LogGen.loggen()

    # @pytest.mark.regression
    # def test_homePageTitle(self, setup):
    #     self.logger.info("*************** Test_001_Login *****************")
    #     self.logger.info("****Started Home page title test ****")
    #     self.driver = setup
    #     self.logger.info("****Opening URL****")
    #     self.driver.get(self.baseURL)
    #     time.sleep(6)
    #     act_title = self.driver.title

    #     if act_title == "Denefits - Admin Panel":
    #         self.logger.info("**** Home page title test passed ****")
    #         self.driver.close()
    #         print("1t")
    #     else:
    #         self.logger.error("**** Home page title test failed****")
    #         self.driver.save_screenshot(".\\Screenshots\\" + "test_admin.png")
    #         self.driver.close()
    #         print("1f")

    #  @pytest.mark.regression
    def getAllfunc():
        printO("called")

    





    def test_login(self, setup ):

        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        time.sleep(7)
        self.lp.clickContinue()
        self.lp.setPassword(self.password)
        time.sleep(5)
        self.lp.clickLogin()
        act_title = self.driver.title
        time.sleep(5)


        if act_title == "Denefits - Admin Panel":
            self.logger.info("****Login test passed ****")
            # print("2t")

            self.driver.get(self.baseURL)
            time.sleep(5)
            self.get=admin_get_all(self.driver)
            panelresult = self.get.getAll()
            # print("plan executed")
            # self.cd = AdminCDPage(self.driver)
            # # panel_all_values_dict = self.cd.get_all_values()
            # # result5 = panel_all_values['value_finaced_ammount']
            # # result6 = panel_all_values['value_of_downpayment']
            # # result7 = panel_all_values['value_of_no_of_month'] 
            # # result8 = panel_all_values['value_of_intrest']



            # # print("panel_totel payble   =  "  + str(result5))
            # # print("panel_principle per rec     =" +str(result6))
            # # print("panel_Precuring amount during def = " +str(result7))
            # # print("panel_totel reminnig amount during def = " +str(result8))
            # self.cd.textfincedamount()
            # time.sleep(5)
            # # print(self.cd.s)
            # self.cd.valuedownp()
            # time.sleep(5)
            # # print(self.cd.vdp)

            # self.cd.valuenofm()
            # time.sleep(5)
            # # print(self.cd.nfm)
            
            # self.cd.valueoftheintrest()
            # time.sleep(2)
            
            
            # self.cd.panelrecurring()
            # time.sleep(2)
            # self.cd.panelupfrontfee()
            # time.sleep(2)
            # self.cd.panelExpectedmonthlypayouttobusiness()
            # time.sleep(2)
            # self.cd.panelTotalExpectedPayouttoBusiness()
            # time.sleep(2)
            # self.cd.panelTotalRemainingAmount()
            # time.sleep(2)
            # self.cd.panelCustomerPayoffAmount()
            # time.sleep(2)
            # self.cd.panelBusinessExpectedPayoff()
            # time.sleep(2)
            # self.cd.panelPrincipalAmount()
            # time.sleep(2)
            # self.cd.panelTotalBalanceRemaining()
            # time.sleep(2)
            





            # print(self.cd.intpanel)

            # self.cal = fun_caluculate(self.driver)       
            
            
            # self.calcalculte(self.driver)
            self.cal = calculate(self.driver)
            result_dict = self.cal.initial_cal(self.cd.value_finaced_ammount,self.cd.value_of_downpayment,self.cd.value_of_no_of_month,self.cd.value_of_intrest)
            result1 = result_dict['value1']
            result2 = result_dict['value2']
            result3 = result_dict['value3'] 
            result4 = result_dict['value4']

            print("totel payble   =  "  + str(result4))
            print("principle per rec     =" +str(result3))
            print("recuring amount during def = " +str(result1))
            print("totel reminnig amount during def = " +str(result2))

            

            # self.cd.clickShowPayments()
            # time.sleep(8)

        




        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_adming.png")
            self.driver.close()
            # print("2ffffffffffffffffffffffffffffff")



   
         
        # def fun_caluculate(self):
        #     cd = AdminCDPage(self.driver)
        #     cd.textfincedamount()
        #     finaced_amount = self.cd.s
        #     print(finaced_amount) 