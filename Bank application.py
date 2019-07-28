# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 15:47:23 2019

@author: Rehan
"""
                        #The Bank Application for adding, viewing , depsiting and withrawing money
import random 
                                # initializing of arrays of fields of an account                   
name_list= []
address_list =[]
phone_list =[]
age_list =[]
acc_no_list =[]
acc_pin_list =[]
balance_list =[]                         
accountpin = 0
iteration = 0
i= 0            #  variable for output loop           
while i>=0:   
                        # Main menu code       
                        print("\t\tPlease Choose the action")
                        print('1- Add Customer \n2- View Customer \n3- Deposit Cash \n4- Deposit Cash \n5- Transactions')
                                                                     
                        # while loop for checking of input value
                        input_loop_check = True  #flag variable for input check loop
                        while input_loop_check:

                            user_input = int(input(":"))
                            if user_input== 1 or user_input==2 or user_input==3 or user_input==4 or user_input==5 :
                                break
                            else:
                                print("user value is not valid, please re-enter")
                   
                        # Code for option 1
                        
                        
                        if user_input ==1:
                         acc = 0    # var for printing account no 
                         acc_no_list.append(random.randint(1,1000))
                         name_list.append(input('Name:'))
                         address_list.append(input('Address:'))
                         phone_list.append(int(input('phone no(please enter integer value):')))
                         age_list.append(int(input('Age:')))
                         acc_pin_list.append(int(input('Pin(please enter integer value):')))
                         balance_list.append(int(input('Initial Account balance is: ')))
                         acc = acc_no_list[i] #variable for printing account number
                         print("your account has been opened. your account no is:   0401",acc)
                         # Code for option 2
                        
                        
                        elif user_input ==2:
                            accountno = int(input(" please Enter your Account NO:"))
                            pinno = int(input(" please Enter the pin NO: "))
                            for iteration in range(0,len(acc_no_list)):
                                if accountno == acc_no_list[iteration] and pinno==acc_pin_list[iteration]:
                                        print(" Name",name_list[iteration])
                                        print(" Address",address_list[iteration])   
                                        print("Phone", phone_list[iteration])
                                        print("Age", age_list[iteration])
                                        print("Balance", balance_list[iteration])
                                else: print("wrong value. Please re-enter")
                                
                        # Code for option 3
                        elif user_input == 3:
                            accountno = int(input(" please Enter your Account NO:"))
                            for iteration in range(0,len(acc_no_list)):
                                if accountno == acc_no_list[iteration] and pinno==acc_pin_list[iteration]:
                        
                                        required_transaction = int(input("Please enter the amount multiple of 500: "))
                                        balance_list[iteration]= required_transaction + balance_list[iteration]
                                        print("Your current balance after deposit is:", balance_list[iteration])
                      # Code for option 4
                      
                      
                      elif user_input == 4:
                            accountno = int(input(" please Enter your Account NO:"))
                            for iteration in range(0,len(acc_no_list)):
                                if accountno == acc_no_list[iteration] and pinno==acc_pin_list[iteration]:
                                    balance_list[iteration]=int(input(" please Enter amount to withdraw that multiple of 500: ")) - balance_list[iteration]
                                    print("Your current balance after Withdrawl is:", balance_list[iteration])
                                
                        i= i+1
                
                             # Code for continuaiton of transaction
                       
                        print("Do you want another transaction ? Y/N")
                        user_check_2 = True  #flag variable for continuation loop
                        while user_check_2:
                            user_input_continuation = input()
                            if user_input_continuation == 'y':
                                break
                            elif user_input_continuation == 'n':
                                i= -1        #condition for exiting loop
                                break
                            else: 
                                print("wrong value, press again")
                                continue
        
print("Program is being closed") 
                        
                              
                        

                        
                        
                        
                