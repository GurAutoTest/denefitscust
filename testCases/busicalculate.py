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
            finaced_amount = a
            # .replace("$","").replace(",","")
            # print(finaced_amount)
            down_payment = b
            # .replace("$","").replace(",","")
            # print(down_payment)
            no_of_month = int(c)
            print(no_of_month)
            # interest = d.replace("% C","").replace(",","")
            # interest = interest.replace("% F","")
            # # print(g)
            # print(h)
            interest= 19.9

            # finaced_amount=float(finaced_amount)

            # print(type(g))
            if (interest == 19.9):
             totel_payble_with_intrest_flat = (finaced_amount*1.1990)
             totel_payble_with_intrest_flat= round(totel_payble_with_intrest_flat)
             print("flat",totel_payble_with_intrest_flat)
             # print("totel payble   =  "  +str(c2)) 
             principle_per_month=finaced_amount/ no_of_month
             principle_per_month=round(principle_per_month)
             recuring_amont_during_def_with_transection  =  principle_per_month * 1.04
             recuring_amont_during_def_with_transection =round(recuring_amont_during_def_with_transection)
             # print("Recuring amount during deffred     =  "  + str(recuring_amont_during_def_with_transection))  
             totel_remaning_during_def= recuring_amont_during_def_with_transection*no_of_month
             totel_remaning_during_def= round(totel_remaning_during_def)
              # print("totel_reaning_during def  =  "   + str(totel_remaning_during_def))   
            
             new_uf =  totel_payble_with_intrest_flat / no_of_month + 1
             rec_after_def =  totel_payble_with_intrest_flat / no_of_month + 1
             rec_after_def= round(rec_after_def)

             customer_payoff_amount = recuring_amont_during_def_with_transection * no_of_month
             customer_payoff_amount = round(customer_payoff_amount)
          
             expected_monthly_payout = principle_per_month*0.995
             expected_monthly_payout = round(expected_monthly_payout)

             
             remaining_expected_payout = expected_monthly_payout * no_of_month
             remaining_expected_payout = round(remaining_expected_payout)
             Paid_to_Business = "working on it"
             donatedamount = "working on it"


            #  return {'value1': recuring_amont_with_transection , 'value2':totel_remaning_amount , 'value3': principle_per_month , 'value4' : totel_payble_with_intrest_flat ,
            #           'value5' : totel_remaning_amount  ,'rec_after_def' : rec_after_def , 'customer_payoff_amount' : customer_payoff_amount , 'expected_monthly_payout' :expected_monthly_payout 
            #            , 'remaining_expected_payout' : remaining_expected_payout  
            #            } 
             return {'value_finaced_ammount' :finaced_amount , 'text_downpayment_amount': down_payment , 'text_downpayment_amount_less': down_payment , 'text_Interest': interest ,
                       'text_number_of_month': no_of_month,'text_Customer_Payoff_Amount': customer_payoff_amount,'textRemainingExpectedPayout': remaining_expected_payout,
                        'textExpectedMonthlyPayout': expected_monthly_payout, 'texttotalbalanceremaning': totel_remaning_during_def,'text_Paid_to_Business': Paid_to_Business,
                         'textdonatedamount': donatedamount,  'textrecbeforedef': recuring_amont_during_def_with_transection ,  'textrecafterdef': rec_after_def }


            else:
              c1 =1+interest/1200
              # print(c1)
              c3 = pow(c1,no_of_month)
              # print(c3)
              totel_remaning_amount = finaced_amount * c3
              # print("totel payble   =  "  +str(c2)) 
              principle_per_month=finaced_amount/ no_of_month
              recuring_amont_during_def_with_transection  =  principle_per_month * 1.04
              # print("Recuring amount during deffred     =  "  + str(recuring_amont_during_def_with_transection))  
              totel_remaning_during_def= recuring_amont_during_def_with_transection*no_of_month
              # print("totel_reaning_during def  =  "   + str(totel_remaning_during_def))   
              rec_after_def =  totel_remaning_amount / no_of_month
              customer_payoff_amount = recuring_amont_during_def_with_transection * no_of_month
          
              expected_monthly_payout = recuring_amont_during_def_with_transection*0.995
              remaining_expected_payout = expected_monthly_payout * no_of_month
              Paid_to_Business = "working on it"
              donatedamount = "working on it"




              
              return {'value_finaced_ammount' :finaced_amount , 'text_downpayment_amount': down_payment , 'text_downpayment_amount_less': down_payment , 'text_Interest': interest ,
                       'text_number_of_month': no_of_month,'text_Customer_Payoff_Amount': customer_payoff_amount,'textRemainingExpectedPayout': remaining_expected_payout,
                        'textExpectedMonthlyPayout': expected_monthly_payout, 'texttotalbalanceremaning': totel_remaning_during_def,'text_Paid_to_Business': Paid_to_Business,
                         'textdonatedamount': donatedamount,  'textrecbeforedef': principle_per_month ,  'textrecafterdef': rec_after_def

                      #  'totel_remaning_during_def':totel_remaning_during_def , 'principle_per_month': principle_per_month , 'value4' : totel_remaning_amount 
                      #    ,'value5' : rec_after_def, 'expected_monthly_payout' : expected_monthly_payout , 
                      #    'remaining_expected_payout' : remaining_expected_payout  
                         } 










              






              # totel_payble_with_intrest_compund = ((float(finaced_amount)*(1+float(interest)/1200))pow no_of_month)
              # print("compound",totel_payble_with_intrest_compund)
              
              
      def compare(self, a, b):
         print("inside compare")

         print(a)
         print(b)
         dict1 = json.loads(a)
         dict2 = json.loads(b)
         for key in dict1:
                if key in dict2:
                   if dict1[key] != dict2[key]:
                     print(f"Difference found at key '{key}': '{dict1[key]}' vs '{dict2[key]}'")
                else:
                    print(f"Key '{key}' not found in second JSON")
    
    # Check for keys in dict2 not in dict1
         for key in dict2:
                if key not in dict1:
                  print(f"Key '{key}' not found in first JSON")



            


            
            
      






