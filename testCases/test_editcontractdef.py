import pytest
from pageObjects.LoginPageBusi import LoginPageBusi
from pageObjects.AdminCDPage import AdminCDPage
from testCases.calculate import calculate
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time


class Test_001_Login:
    # baseURL = "https://testcustomer.denefits.com"
    baseURL = "https://testbusiness.denefits.com"
    username = "gurdeep.singh+secoldpart1712@bridgingtech.com"
    password = "sookie"
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
    
    def test_login(self, setup ):

        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPageBusi(self.driver)
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
            print("2t")

            self.driver.get(self.baseURL)
            time.sleep(5)
            print("plan executed")
            self.cd = AdminCDPage(self.driver)
            self.cd.textfincedamount()
            time.sleep(5)
            print(self.cd.s)
            self.cd.valuedownp()
            time.sleep(5)
            print(self.cd.vdp)

            self.cd.valuenofm()
            time.sleep(5)
            print(self.cd.nfm)
            
            self.cd.valueoftheintrest()
            time.sleep(5)
            print(self.cd.intpanel)

            # self.cal = fun_caluculate(self.driver)       
            
            
            # self.calcalculte(self.driver)
            self.cal = calculate(self.driver)
            self.cal.initial_cal(self.cd.s,self.cd.vdp,self.cd.nfm,self.cd.intpanel)

            # self.cd.clickShowPayments()
            # time.sleep(8)

        




        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_adming.png")
            self.driver.close()
            print("2ffffffffffffffffffffffffffffff")



   
         
        # def fun_caluculate(self):
        #     cd = AdminCDPage(self.driver)
        #     cd.textfincedamount()
        #     finaced_amount = self.cd.s
        #     print(finaced_amount) 