import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("******* Starting Test_002_DDT_Login Test **********")
        self.logger.info("******* Starting Login DDT Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print('Number of rows...', self.rows)
        lst_status = []
        time.sleep(5)

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            time.sleep(5)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(15)

            act_title = self.driver.title
            exp_title = "Denefits Customer"
            print(act_title)

            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** passed ****")
                    self.lp.clickLogoutDrop()
                    time.sleep(5)
                    print("1111ff")
                    self.lp.clickLogout()
                    print("22222ff")
                    time.sleep(5)
                    self.lp.clickLogoutLast()
                    print("3333333ff")
                    lst_status.append("Pass")
                elif self.exp == 'Fail':
                    self.logger.info("**** failed ****")
                    self.lp.clickLogoutDrop()
                    time.sleep(5)
                    print("1111")
                    self.lp.clickLogout()
                    print("22222")
                    time.sleep(5)
                    self.lp.clickLogoutLast()
                    print("3333333")
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** failed ****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**** passed ****")
                    print("kkk")
                    lst_status.append("Pass")
            print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info("******* DDT Login test passed **********")
            self.driver.close()
        else:
            self.logger.error("******* DDT Login test failed **********")
            print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
            self.driver.close()

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ")
