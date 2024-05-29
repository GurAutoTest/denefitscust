import pytest
from pageObjects.LoginPageBusi import LoginPageBusi
from pageObjects.AdminCDPage import AdminCDPage
from testCases.Busi_get_all import  Busi_get_all
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
    def getAllfunc():
        print("called")



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
        time.sleep(25)
        act_title = self.driver.title
        time.sleep(5)
        print(act_title)


        if act_title == "Denefits Business":
            self.logger.info("****Login test passed ****")
            print("2t")
            
            self.lp.clickPaymentPlans()
            time.sleep(5)
            self.lp.clickManagecontracts()
            time.sleep(25)
            self.driver.save_screenshot(".\\Screenshots\\" + "test_where_i_m.png")
            self.lp.clickFullPaymentPlanDetails()
            time.sleep(5)
            self.get=Busi_get_all(self.driver)
            time.sleep(5)
            panelresult = self.get.getAll()



            

 
 

        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_busiapple.png")
            self.driver.close()
            print("2ffffffffffffffffffffffffffffff")



   
         
        # def fun_caluculate(self):
        #     cd = AdminCDPage(self.driver)
        #     cd.textfincedamount()
        #     finaced_amount = self.cd.s
        #     print(finaced_amount) 