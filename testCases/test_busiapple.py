import pytest
from pageObjects.LoginPageBusi import LoginPageBusi
from pageObjects.AdminCDPage import AdminCDPage
from testCases.Busi_get_all import Busi_get_all
from testCases.busicalculate import busicalculate
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
from openpyxl import Workbook
from testCases.createExcel import excelFileCreation
import time


class Test_001_Login:
    # # baseURL = "https://testcustomer.denefits.com"
    baseURL = "https://testbusiness.denefits.com"
    username = "gurdeep.singh+secoldpart1712@bridgingtech.com"
    password = "sookie"
    contract_id = "84679"

    # logger = LogGen.loggen()
    # def getAllfunc():
    #     printO("called")

    # def test_login(self, setup ):

    #     self.logger.info("****Started Login Test****")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.lp = LoginPageBusi(self.driver)
    #     self.lp.setUserName(self.username)
    #     time.sleep(7)
    #     self.lp.clickContinue()
    #     self.lp.setPassword(self.password)
    #     time.sleep(2)
    #     self.lp.clickLogin()
    #     time.sleep(25)
    #     act_title = self.driver.title
    #     time.sleep(2)
    #     print(act_title)
    # baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()  # Logger

    # @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("******* Starting Test_002_DDT_Login Test **********")
        self.logger.info("******* Starting Login DDT Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        # self.driver.maximize_window()
        self.lp = LoginPageBusi(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print('Number of rows...', self.rows)
        lst_status = []
        time.sleep(2)

        # for r in range(2, self.rows + 1):
        #     self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
        #     self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
        #     self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
        time.sleep(2)
        print(self.username)
        print(self.password)

        self.lp.setUserName(self.username)
        time.sleep(2)
        
        self.lp.clickContinue()
        time.sleep(2)
        
        self.lp.setPassword(self.password)
        time.sleep(2)

        self.lp.clickLogin()
        time.sleep(15)

        act_title = self.driver.title
        exp_title = "Denefits Customer"
        print(act_title)

        if act_title == "Denefits Business":

              self.logger.info("****Login test passed ****")
              print("2t")

              self.lp.clickPaymentPlans()
              time.sleep(2)
              self.lp.clickManagecontracts()
              time.sleep(10)
              
              self.lp.setsearchbar(self.contract_id)
              time.sleep(2)


              self.lp.pressenter()
              time.sleep(10)




            #   self.driver.save_screenshot(
            #       ".\\Screenshots\\" + "test_where_i_m.png")
              self.lp.clickFullPaymentPlanDetails()
              time.sleep(2)
              self.get = Busi_get_all(self.driver)
              time.sleep(2)
              panelresult = self.get.getAll()
              time.sleep(2)
              print("testmeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
              print(panelresult)

              excelFileCreation(panelresult, "test_file2", "sheet") 
              # return
              
              result1 = panelresult['value_finaced_ammount']
              result2 = panelresult['text_downpayment_amount']
              result3 = panelresult['text_number_of_month']
              result4 = panelresult['text_Customer_Payoff_Amount']
              
              # wb = self.path
              
              # headers = list(panelresult.keys())
              # # # wb.append(headers)
              
              # values = [panelresult[header] for header in headers]
              # # # wb.append(values)
              
              # # for r in range(2, self.rows + 1):
              # XLUtils.writeData(self.path, 'Sheet1',values)
              # print(values)
                  
              
              
              
              
              
              
              
              # wb = Workbook()
              # ws = wb.active
              #      # Write data to the worksheet
              # for row in panelresult:
              #     ws.append(row)
              #     # Save the workbo
              #     wb.save(result1+".xlsx")
              
              # print("totel payble   =  " + str(result4))
              # print("principle per rec     =" + str(result3))
              # print("recuring amount during def = " + str(result1))
              # print("totel reminnig amount during def = " + str(result2))
              

    

            # calcalculte my values
              self.cal = busicalculate(self.driver)
              result_dict = self.cal.initial_cal(result1,result2,result3)
              print(result_dict)



              self.cal = busicalculate(self.driver)
              compare_result = self.cal.compare(panelresult,result_dict)



     

            # print("totel payble   =  " + str(result4))
            # print("principle per rec     =" + str(result3))
            # print("recuring amount during def = " + str(result1))
            # print("totel reminnig amount during def = " + str(result2))


# compare function sys value and my calculated values


# print in excel

        # self.newget = Busi_get_all(self.driver)
        # time.sleep(2)
        # panelresult = self.newget.getnewvalues()
        # self.busivalue.textnewfinacedamount()
        # time.sleep(2)

            #  calculate after edit
            # self.editcal = editcalculate(self.driver)
            # result_edit_dict = self.cal.initial_cal(
            #     self.busivalue.text_finaced_ammount, self.busivalue.text_of_downpayment, self.busivalue.text_no_of_month, self.busivalue.text_intrest)
            # print(result_edit_dict)

        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_busiapple.png")
            self.driver.close()
            print("2ffffffffffffffffffffffffffffff")

        # def fun_caluculate(self):
        #     cd = AdminCDPage(self.driver)
        #     cd.textfincedamount()
        #     finaced_amount = self.cd.s
        #     print(finaced_amount)
