from selenium.webdriver.common.by import By
import json                         
from pageObjects import AdminCDPage


class busicalculate:
      # self.driver = setup
      # cd = AdminCDPage()
      # cd.textfincedamount()
      # finaced_amount = 78
      print("in the class caluculate finaced_amount") 


      def __init__(self, driver):
        self.driver = driver


      def initial_cal(self , a,b,c):
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
            
            
            # print(a)
            # print(b)
            # print(c)
            # print(d)
            # print("abc")
            # print(self.finaced_amount)
            finaced_amount = a.replace("$","").replace(",","")
            print(finaced_amount)
            down_payment = b.replace("$","").replace(",","")
            print(down_payment)
            no_of_month = int(c)
            print(no_of_month)
            # interest = d.replace("% C","").replace(",","")
            # interest = interest.replace("% F","")
            # # print(g)
            # print(h)
            interest= 19.9

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
             rec_after_def =  totel_payble_with_intrest_flat / no_of_month

             return {'value1': recuring_amont_with_transection , 'value2':totel_remaning_amount , 'value3': principle_per_month , 'value4' : totel_payble_with_intrest_flat , 'value5' : totel_remaning_amount  ,'value6' : rec_after_def } 


            else:
              c1 =1+interest/1200
              # print(c1)
              c3 = pow(c1,no_of_month)
              # print(c3)
              totel_remaning_amount = finaced_amount * c3
              # print("totel payble   =  "  +str(c2)) 
              principle_per_month=finaced_amount/ no_of_month
              recuring_amont_during_def_with_transection  =  principle_per_month * 1.03
              # print("Recuring amount during deffred     =  "  + str(recuring_amont_during_def_with_transection))  
              totel_remaning_during_def= recuring_amont_during_def_with_transection*no_of_month
              # print("totel_reaning_during def  =  "   + str(totel_remaning_during_def))   
              rec_after_def =  totel_remaning_amount / no_of_month

              
              return {'recuring_amont_during_def_with_transection': recuring_amont_during_def_with_transection , 'totel_remaning_during_def':totel_remaning_during_def , 'principle_per_month': principle_per_month , 'value4' : totel_remaning_amount  ,'value5' : rec_after_def } 









              






              # totel_payble_with_intrest_compund = ((float(finaced_amount)*(1+float(interest)/1200))pow no_of_month)
              # print("compound",totel_payble_with_intrest_compund)
              
              







            # service_amount = int(g)
            # print(service_amount)
            # print(type(service_amount))

            


            
            
      






