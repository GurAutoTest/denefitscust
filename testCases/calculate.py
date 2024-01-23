from selenium.webdriver.common.by import By
import json                         
from pageObjects import AdminCDPage


class calculate:
      # self.driver = setup
      # cd = AdminCDPage()
      # cd.textfincedamount()
      # finaced_amount = 78
      print("in the class caluculate finaced_amount") 


      def __init__(self, driver):
        self.driver = driver


      def initial_cal(self , a,b,c,d):
            # self.cd = AdminCDPage(self.driver)
            # self.cd.textfincedamount()
            # time.sleep(5)
            # print(self.cd.s)
            # self.cd.valuedownp()
            # time.sleep(5)
            # print(self.cd.vdp)

            # self.cd.valuenofm()
            # time.sleep(5)
            # print(self.cd.nfm)
            
            
            print(a)
            print(b)
            print(c)
            print(d)
            # print("abc")
            # print(self.finaced_amount)
            finaced_amount = a.replace("$","").replace(",","")
            interest = d.replace("% C","").replace(",","")
            no_of_month = int(c)
            down_payment = b.replace("$","").replace(",","")
            # print(g)
            # print(h)
            interest=float(interest)
            finaced_amount=float(finaced_amount)

            # print(type(g))
            if (interest == 19.9):
             totel_payble_with_intrest_flat = (finaced_amount*1.1990)
             print("flat",totel_payble_with_intrest_flat)
            else:
              c1 =1+interest/1200
              print(c1)
              c3 = pow(c1,no_of_month)
              print(c3)
              c2 = finaced_amount * c3
              print(c2)
              






              # totel_payble_with_intrest_compund = ((float(finaced_amount)*(1+float(interest)/1200))pow no_of_month)
              # print("compound",totel_payble_with_intrest_compund)
              
              







            # service_amount = int(g)
            # print(service_amount)
            # print(type(service_amount))

            


            
            
      






