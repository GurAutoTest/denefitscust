from selenium.webdriver.common.by import By
import json                         
from pageObjects import AdminCDPage


class editcalculate:


      def __init__(self, driver):
        self.driver = driver


      def initial_cal(self , a,b,c,d):
            # self.cd = AdminCDPage(self.driver)
            # self.cd.textfincedamount()bnmbnmbmbbhjghjhjgjghjgj
            # time.sleep(5)
            # print(self.cd.s)
            # self.cd.valuedownp()
            # time.sleep(5)
            # print(self.cd.vdp)

            # self.cd.valuenofm()
            # time.sleep(5)
            # print(self.cd.nfm)
            
            
            # print(a)
            # print(b)
            # print(c)
            # print(d)
            # print("abc")
            # print(self.finaced_amount)
            finaced_amount = a.replace("$","").replace(",","")
            down_payment = b.replace("$","").replace(",","")
            no_of_month = int(c)
            interest = d.replace("% C","").replace(",","")
            interest = interest.replace("% F","")
            # print(g)
            # print(h)
            interest=float(interest)
            finaced_amount=float(finaced_amount)

            # print(type(g))
            if (interest == 19.9):
             totel_payble_with_intrest_flat = (finaced_amount*1.1990)
             print("flat",totel_payble_with_intrest_flat)
             # print("totel payble   =  "  +str(c2)) 
             principle_per_month=finaced_amount/ no_of_month
             recuring_amont_with_transection  =  principle_per_month * 1.03
             # print("Recuring amount during deffred     =  "  + str(recuring_amont_during_def_with_transection))  
             totel_remaning_amount= recuring_amont_with_transection*no_of_month
              # print("totel_reaning_during def  =  "   + str(totel_remaning_during_def))   
              
             return {'value1': recuring_amont_with_transection , 'value2':totel_remaning_amount , 'value3': principle_per_month , 'value4' : totel_payble_with_intrest_flat} 


            else:
              c1 =1+interest/1200
              # print(c1)
              c3 = pow(c1,no_of_month)
              # print(c3)
              c2 = finaced_amount * c3
              # print("totel payble   =  "  +str(c2)) 
              principle_per_month=finaced_amount/ no_of_month
              recuring_amont_during_def_with_transection  =  principle_per_month * 1.03
              # print("Recuring amount during deffred     =  "  + str(recuring_amont_during_def_with_transection))  
              totel_remaning_during_def= recuring_amont_during_def_with_transection*no_of_month
              # print("totel_reaning_during def  =  "   + str(totel_remaning_during_def))   
              
              return {'value1': recuring_amont_during_def_with_transection , 'value2':totel_remaning_during_def , 'value3': principle_per_month , 'value4' : c2} 









              






              # totel_payble_with_intrest_compund = ((float(finaced_amount)*(1+float(interest)/1200))pow no_of_month)
              # print("compound",totel_payble_with_intrest_compund)
              
              







            # service_amount = int(g)
            # print(service_amount)
            # print(type(service_amount))

            


            
            
      






