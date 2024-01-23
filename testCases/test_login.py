import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time


class Test_001_Login:
    baseURL = "https://testcustomer.denefits.com"
    username = "gurdeep.singh+cust@bridgingtech.com"
    password = "123123"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Login to your customer panel - Denefits":
            self.logger.info("**** Home page title test passed ****")
            self.driver.close()
            print("1t")
        else:
            self.logger.error("**** Home page title test failed****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            print("1f")
    # @pytest.mark.sanity

    @pytest.mark.regression
    def test_login(self, setup):

        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)                  
        self.lp.setPassword(self.password)
        time.sleep(5)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Denefits Customer":
            self.logger.info("****Login test passed ****")
            self.driver.close()
            print("2t")
        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            print("2f")
