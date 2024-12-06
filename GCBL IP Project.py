import pymysql
import string
import time
import datetime
import random
from playsound import playsound
from PIL import Image

im = Image.open("Logo2.png")
im.show()

link = pymysql.connect(host='localhost', user='root', password='IPProject123!')
link.cursor().execute('create database atm')
a = link.cursor()
a.execute("use ATM")
a.execute('create table Account_Details (Acc_No char(8) primary key, PIN char(4), Current int, Savings int)')
a.execute('create table MINI (Sl_No int NOT NULL AUTO_INCREMENT PRIMARY KEY, Acc_No char(8), Date_Of_Transaction datetime, Type_Of_Transaction varchar(20), FROM_ varchar(20), TO_ varchar(20), Amount int)')
link.commit()
count=0

while(True):
    time.sleep(1)
    abc = int(input('--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--\n\nPress "1" to continue:'))
    if (abc == 1):
        print('Welcome to Gafan Commercial Bank Limited!!!')
        print('Instructions:')
        print('1. Insert Card carefully. Make sure the chip is inserted first.')
        print('2. Enter PIN secretly. Make sure you do not give your PIN to anyone.')
        print('3. If the number of PIN entering attempts exceed 3, the ATM will lock the account for 60 seconds. If it exceeds 6, the account is locked. Call the nearest branch manager to reinstate account.')
        print('4. Vandalising/Damaging this ATM or any property owned or claimed by the bank will attract fines of ₹1000 and imprisonment lasting for 6 months.')
        print('5. Attempting to break into the ATM, or impersonating another person and using his/her/their username and/or PIN, attracts a fine of ₹2500 and imprisonment lasting for 6 months to 2 years.')

        print('\n******************************\n \nInsert card:')
        time.sleep(2)
        print('\nWould you like to \n1.Register as a New User \nor\n2.Sign in as an Existing User?') 
        CHOICE_A = int(input("Enter your choice: "))

        if (CHOICE_A == 1): #NEW USER
            link = pymysql.connect(host='localhost', user='root', password='IPProject123!', db = 'ATM')
            a = link.cursor()
            users = input("Enter Account Number: ")
            pin = input("Enter PIN: ")
            zero=0
            mysql_insert_query = "insert into Account_Details(Acc_No, PIN, Current, Savings) values(%s,%s,%s,%s)"
            record=(users,pin,zero,zero)
            a.execute(mysql_insert_query, record)
            print('Loading......Wait for a few seconds')
            time.sleep(2)
            print('3...')
            time.sleep(1)
            print('2...')
            time.sleep(1)
            print('1...')
            time.sleep(0.5)
            print("--* NEW USER ACCOUNT HAS BEEN SUCCESSFULLY CREATED!! PLEASE SIGN IN AGAIN.*--")
            print('Intial value of Current Account: 0 \nIntial value of Savings Account: 0')
            print('Deposit money to increase balance \n')
            link.commit()
              

        elif (CHOICE_A == 2): #EXISTING USER
            link = pymysql.connect(host='localhost', user='root', password='IPProject123!', db = 'ATM')
            a = link.cursor()
            user = input('\nEnter Account Number: ')
            pin_main = input('Enter PIN: ')
            a.execute("select * from Account_Details where Acc_No='" + user + "' and PIN = '" + pin_main + "'")
            c_main = a.fetchall()
            
            if (len(c_main) == 0 and count < 3):
                print('\nINVALID Username or Password! \n \n')
                count+=1
                
            elif (count >= 3 and count < 6):
                print('Account blocked for 60 seconds')
                count+=1
                time.sleep(60)
                
            elif (count >= 6):
                print('User Blocked')
                mysql_insert_query = "insert into Account_Details(PIN) values(%s)"
                pin_main  = random.randint(1000, 9999)
                record=pin_main
                a.execute(mysql_insert_query, record)
                
            else:
                count=0
                print(" \nLOGIN AUTHORIZED!! \n \n")        
                while(True):
                    print('\n\n************************************\n1. Deposit \n2. Withdrawal \n3. Transfer \n4. PIN change \n5. Account Details \n6. MINI Statement \n7. About Bank \n8. Go to HOME Page')
                    CHOICE_B = int(input("Please enter your choice: "))
                    print('************************************')
                    time.sleep(1)
                    
                    if (CHOICE_B == 1):#DEPOSIT
                        link = pymysql.connect(host='localhost', user='root', password='IPProject123!', db = 'ATM')
                        a = link.cursor()
                        print('\n1.Current Account \n2.Savings Account')
                        CHOICE_B1 = int(input("Enter your Account: "))
                        time.sleep(1)
                        if (CHOICE_B1 == 1):#DEPOSIT_CURRENT                            
                            amt = int(input("Enter Amount to Deposit: "))
                            print('Loading......Please wait while your transaction is being completed.....')
                            playsound('atmsound.mp3')                            
                            print('3...')
                            time.sleep(1)
                            print('2...')
                            time.sleep(1)
                            print('1...')
                            time.sleep(0.5)
                            print('total Sum Deposited: ₹', amt ,'\n')
                            mysql_insert = "insert into MINI (Acc_No, Date_Of_Transaction, Type_Of_Transaction, FROM_, TO_, Amount) values (%s, %s, %s, %s, %s, %s)"
                            ct = datetime.datetime.now()
                            tot = 'Deposit'
                            _from_ = 'One-self'
                            _to_ = 'Current'
                            amt_transfer = amt
                            variables = (user,ct,tot, _from_ , _to_ , amt_transfer)
                            a.execute(mysql_insert, variables)
                            continue_prompt = str(input('Do you want to print receipt? Please keep in mind the effect on the environment (yes/no)? '))                                      
                            b = continue_prompt.lower()                            
                            if (b[0] == 'y'):
                                playsound('printersound.mp3') 
                                print('**** Receipt Printed ****')
                            a.execute("select Current from Account_Details WHERE Acc_No = '"+ user +"'")
                            c=a.fetchone()
                            price = int(c[0])
                            record = price+amt
                            a.execute("UPDATE Account_Details SET Current = '%s' WHERE Acc_No = '"+ user +"'",record)
                            continue_prompt = str(input('Do you want to continue (yes/no)? '))
                            b = continue_prompt.lower()
                            link.commit()                    
                            if (b[0] == 'y'):
                                continue
                            else:                            
                                break;
                        elif (CHOICE_B1 == 2): #DEPOSIT_SAVINGS
                            amt = int(input("Enter Amount to Deposit: "))
                            print('Loading......Please wait while your transaction is being completed.....')
                            playsound('atmsound.mp3')                            
                            print('3...')
                            time.sleep(1)
                            print('2...')
                            time.sleep(1)
                            print('1...')
                            time.sleep(0.5)
                            print('total Sum Deposited: ₹', amt ,'\n')
                            mysql_insert = "insert into MINI (Acc_No, Date_Of_Transaction, Type_Of_Transaction, FROM_, TO_, Amount) values (%s, %s, %s, %s, %s, %s)"
                            ct = datetime.datetime.now()
                            tot = 'Deposit'
                            _from_ = 'One-self'
                            _to_ = 'Savings'
                            amt_transfer = amt
                            variables = (user,ct,tot, _from_ , _to_ , amt_transfer)
                            a.execute(mysql_insert, variables)
                            continue_prompt = str(input('Do you want to print receipt? Please keep in mind the effect on the environment (yes/no)? '))                                      
                            b = continue_prompt.lower()                            
                            if (b[0] == 'y'):
                                playsound('printersound.mp3')
                                print('**** Receipt Printed ****')
                            a.execute("select Savings from Account_Details WHERE Acc_No = '"+ user +"'")
                            c=a.fetchone()
                            price = int(c[0])
                            record = price+amt
                            a.execute("UPDATE Account_Details SET Savings = '%s' WHERE Acc_No = '"+ user +"'",record)
                            continue_prompt = str(input('Do you want to continue (yes/no)? '))
                            b = continue_prompt.lower()
                            link.commit()                    
                            if (b[0] == 'y'):
                                continue
                            else:                            
                                break;
                            
                    elif (CHOICE_B == 2):#WITHDRAWAL                    
                        print('\n1.Current Account \n2.Savings Account')
                        CHOICE_B2 = int(input("Enter which Account: "))                    
                        if (CHOICE_B2 == 1):#WITHDRAWAL_Current
                            amt = int(input("Enter Amount to Withdraw: "))
                            print('Loading......Please wait while your transaction is being completed.....')
                            playsound('atmsound.mp3')                            
                            print('3...')
                            time.sleep(1)
                            print('2...')
                            time.sleep(1)
                            print('1...')
                            time.sleep(0.5)
                            print('Amount Withdrawn: ₹', amt , '\n')
                            mysql_insert = "insert into MINI (Acc_No, Date_Of_Transaction, Type_Of_Transaction, FROM_, TO_, Amount) values (%s, %s, %s, %s, %s, %s)"
                            ct = datetime.datetime.now()
                            tot = 'Withdrawal'
                            _from_ = 'Current'
                            _to_ = 'One-self'
                            amt_transfer = amt
                            variables = (user,ct,tot, _from_ , _to_ , amt_transfer)
                            a.execute(mysql_insert, variables)
                            continue_prompt = str(input('Do you want to print receipt? Please keep in mind the effect on the environment (yes/no)? '))                                      
                            b = continue_prompt.lower()                            
                            if (b[0] == 'y'):
                                playsound('printersound.mp3')
                                print('**** Receipt Printed ****')
                            a.execute("select Current from Account_Details WHERE Acc_No = '"+ user +"'")
                            c=a.fetchone()
                            price = int(c[0])
                            record = price-amt
                            a.execute("UPDATE Account_Details SET Current = '%s' WHERE Acc_No = '"+ user +"'",record)
                            continue_prompt = str(input('Do you want to continue (yes/no)? \n'))
                            b = continue_prompt.lower()
                            link.commit()                        
                            if (b[0] == 'y'):
                                continue
                            else:                            
                                break;
                        elif (CHOICE_B2 == 2):#WITHDRAWAL_SAVINGS                       
                            amt = int(input("Enter Amount to Withdraw: "))
                            print('Loading......Please wait while your transaction is being completed.....')
                            playsound('atmsound.mp3')                            
                            print('3...')
                            time.sleep(1)
                            print('2...')
                            time.sleep(1)
                            print('1...')
                            time.sleep(0.5)
                            print('Amount Withdrawn: ₹', amt , '\n')
                            mysql_insert = "insert into MINI (Acc_No, Date_Of_Transaction, Type_Of_Transaction, FROM_, TO_, Amount) values (%s, %s, %s, %s, %s, %s)"
                            ct = datetime.datetime.now()
                            tot = 'Withdrawal'
                            _from_ = 'Savings'
                            _to_ = 'One-self'
                            amt_transfer = amt
                            variables = (user,ct,tot, _from_ , _to_ , amt_transfer)
                            a.execute(mysql_insert, variables)
                            continue_prompt = str(input('Do you want to print receipt? Please keep in mind the effect on the environment (yes/no)? '))                                      
                            b = continue_prompt.lower()                            
                            if (b[0] == 'y'):
                                playsound('printersound.mp3')
                                print('**** Receipt Printed ****')
                            a.execute("select Savings from Account_Details WHERE Acc_No = '"+ user +"'")
                            c=a.fetchone()
                            price = int(c[0])
                            record = price-amt
                            a.execute("UPDATE Account_Details SET Savings = '%s' WHERE Acc_No = '"+ user +"'",record)
                            continue_prompt = str(input('Do you want to continue (yes/no)? '))
                            b = continue_prompt.lower()
                            link.commit()                            
                            if (b[0] == 'y'):
                                continue
                            else:                            
                                break;
                                 
                    elif (CHOICE_B == 3):#TRANSFER
                        link = pymysql.connect(host='localhost', user='root', password='IPProject123!', db = 'ATM')
                        a = link.cursor()
                        print('\n1.Bank to Bank Transfer \n2.Current to Savings \n3.Savings to Current')
                        CHOICE_B3 = int(input("Enter mode of transfer: " ))                    
                        if (CHOICE_B3 == 1):#TRANSFER__BANK to BANK
                            print('1.SBI \n2.HDFC \n3.Axis \n4.CITI')
                            CHOICE_B3_1 = int(input("Enter Recipient Bank: " ))                        
                            if (CHOICE_B3_1 == 1):#SBI
                                print ('1. Current \n2. Savings')
                                CHOICE_C = int(input('Enter Account: '))
                                if (CHOICE_C == 1):
                                    amt = int(input("Enter Amount to transfer: "))
                                    print('Loading......Please wait while your transaction is being completed.....')
                                    playsound('atmsound.mp3')                                    
                                    print('3...')
                                    time.sleep(1)
                                    print('2...')
                                    time.sleep(1)
                                    print('1...')
                                    time.sleep(0.5)
                                    print('Amount transferred: ₹', amt , '\n')
                                    mysql_insert = "insert into MINI (Acc_No, Date_Of_Transaction, Type_Of_Transaction, FROM_, TO_, Amount) values (%s, %s, %s, %s, %s, %s)"
                                    ct = datetime.datetime.now()
                                    tot = 'Transfer'
                                    _from_ = 'Current'
                                    _to_ = 'SBI'
                                    amt_transfer = amt
                                    variables = (user,ct,tot, _from_ , _to_ , amt_transfer)
                                    a.execute(mysql_insert, variables)
                                    continue_prompt = str(input('Do you want to print receipt? Please keep in mind the effect on the environment (yes/no)? '))                                      
                                    b = continue_prompt.lower()                            
                                    if (b[0] == 'y'):
                                        playsound('printersound.mp3')
                                        print('**** Receipt Printed ****')
                                    a.execute("select Current from Account_Details WHERE Acc_No = '"+ user +"'")
                                    c=a.fetchone()
                                    price = int(c[0])
                                    record = price-amt
                                    a.execute("UPDATE Account_Details SET Current = '%s' WHERE Acc_No = '"+ user +"'",record)
                                elif (CHOICE_C == 2):
                                    amt = int(input("Enter Amount to transfer: "))
                                    print('Loading......Please wait while your transaction is being completed.....')
                                    playsound('atmsound.mp3')                                    
                                    print('3...')
                                    time.sleep(1)
                                    print('2...')
                                    time.sleep(1)
                                    print('1...')
                                    time.sleep(0.5)
                                    print('Amount transferred ₹:', amt , '\n')
                                    mysql_insert = "insert into MINI (Acc_No, Date_Of_Transaction, Type_Of_Transaction, FROM_, TO_, Amount) values (%s, %s, %s, %s, %s, %s)"
                                    ct = datetime.datetime.now()
                                    tot = 'Transfer'
                                    _from_ = 'Savings'
                                    _to_ = 'SBI'
                                    amt_transfer = amt
                                    variables = (user,ct,tot, _from_ , _to_ , amt_transfer)
                                    a.execute(mysql_insert, variables)
                                    continue_prompt = str(input('Do you want to print receipt? Please keep in mind the effect on the environment (yes/no)? '))                                      
                                    b = continue_prompt.lower()                            
                                    if (b[0] == 'y'):
                                        playsound('printersound.mp3')
                                        print('**** Receipt Printed ****')
                                    a.execute("select Savings from Account_Details WHERE Acc_No = '"+ user +"'")
                                    c=a.fetchone()
                                    price = int(c[0])
                                    record = price-amt
                                    a.execute("UPDATE Account_Details SET Savings = '%s' WHERE Acc_No = '"+ user +"'",record)
                                else:
                                    print("\nENTER VALID INPUT! \n \n")
                                    continue
                                continue_prompt = str(input('Do you want to continue (yes/no)? '))
                                b = continue_prompt.lower()
                                link.commit()                            
                                if (b[0] == 'y'):
                                    continue
                                else:                            
                                    break;                            
                            elif (CHOICE_B3_1 == 2):#HDFC
                                print ('1. Current \n2. Savings')
                                CHOICE_C = int(input('Enter Account: '))
                                if (CHOICE_C == 1):
                                    amt = int(input("Enter Amount to transfer: "))
                                    print('Loading......Please wait while your transaction is being completed.....')
                                    playsound('atmsound.mp3')                                    
                                    print('3...')
                                    time.sleep(1)
                                    print('2...')
                                    time.sleep(1)
                                    print('1...')
                                    time.sleep(0.5)
                                    print('Amount transferred: ₹', amt , '\n')
                                    mysql_insert = "insert into MINI (Acc_No, Date_Of_Transaction, Type_Of_Transaction, FROM_, TO_, Amount) values (%s, %s, %s, %s, %s, %s)"
                                    ct = datetime.datetime.now()
                                    tot = 'Transfer'
                                    _from_ = 'Current'
                                    _to_ = 'HDFC'
                                    amt_transfer = amt
                                    variables = (user,ct,tot, _from_ , _to_ , amt_transfer)
                                    a.execute(mysql_insert, variables)
                                    continue_prompt = str(input('Do you want to print receipt? Please keep in mind the effect on the environment (yes/no)? '))                                      
                                    b = continue_prompt.lower()                            
                                    if (b[0] == 'y'):
                                        playsound('printersound.mp3')
                                        print('**** Receipt Printed ****')
                                    a.execute("select Current from Account_Details WHERE Acc_No = '"+ user +"'")
                                    c=a.fetchone()
                                    price = int(c[0])
                                    record = price-amt
                                    a.execute("UPDATE Account_Details SET Current = '%s' WHERE Acc_No = '"+ user +"'",record)
                                elif (CHOICE_C == 2):
                                    amt = int(input("Enter Amount to transfer: "))
                                    print('Loading......Please wait while your transaction is being completed.....')
                                    playsound('atmsound.mp3')                                    
                                    print('3...')
                                    time.sleep(1)
                                    print('2...')
                                    time.sleep(1)
                                    print('1...')
                                    time.sleep(0.5)
                                    print('Amount transferred: ₹', amt , '\n')
                                    mysql_insert = "insert into MINI (Acc_No, Date_Of_Transaction, Type_Of_Transaction, FROM_, TO_, Amount) values (%s, %s, %s, %s, %s, %s)"
                                    ct = datetime.datetime.now()
                                    tot = 'Transfer'
                                    _from_ = 'Savings'
                                    _to_ = 'HDFC'
                                    amt_transfer = amt
                                    variables = (user,ct,tot, _from_ , _to_ , amt_transfer)
                                    a.execute(mysql_insert, variables)
                                    continue_prompt = str(input('Do you want to print receipt? Please keep in mind the effect on the environment (yes/no)? '))                                      
                                    b = continue_prompt.lower()                            
                                    if (b[0] == 'y'):
                                        playsound('printersound.mp3')
                                        print('**** Receipt Printed ****')
                                    a.execute("select Savings from Account_Details WHERE Acc_No = '"+ user +"'")
                                    c=a.fetchone()
                                    price = int(c[0])
                                    record = price-amt
                                    a.execute("UPDATE Account_Details SET Savings = '%s' WHERE Acc_No = '"+ user +"'",record)
                                else:
                                    print("\nENTER VALID INPUT! \n \n")
                                    continue
                                continue_prompt = str(input('Do you want to continue (yes/no)? '))
                                b = continue_prompt.lower()
                                link.commit()                            
                                if (b[0] == 'y'):
                                    continue
                                else:                            
                                    break;                              
                            elif (CHOICE_B3_1 == 3):#Axis
                                print ('1. Current \n2. Savings')
                                CHOICE_C = int(input('Enter Account: '))
                                if (CHOICE_C == 1):
                                    amt = int(input("Enter Amount to transfer: "))
                                    print('Loading......Please wait while your transaction is being completed.....')
                                    playsound('atmsound.mp3')                                    
                                    print('3...')
                                    time.sleep(1)
                                    print('2...')
                                    time.sleep(1)
                                    print('1...')
                                    time.sleep(0.5)
                                    print('Amount transferred: ₹', amt , '\n')
                                    mysql_insert = "insert into MINI (Acc_No, Date_Of_Transaction, Type_Of_Transaction, FROM_, TO_, Amount) values (%s, %s, %s, %s, %s, %s)"
                                    ct = datetime.datetime.now()
                                    tot = 'Transfer'
                                    _from_ = 'Current'
                                    _to_ = 'Axis'
                                    amt_transfer = amt
                                    variables = (user,ct,tot, _from_ , _to_ , amt_transfer)
                                    a.execute(mysql_insert, variables)
                                    continue_prompt = str(input('Do you want to print receipt? Please keep in mind the effect on the environment (yes/no)? '))                                      
                                    b = continue_prompt.lower()                            
                                    if (b[0] == 'y'):
                                        playsound('printersound.mp3')
                                        print('**** Receipt Printed ****')
                                    a.execute("select Current from Account_Details WHERE Acc_No = '"+ user +"'")
                                    c=a.fetchone()
                                    price = int(c[0])
                                    record = price-amt
                                    a.execute("UPDATE Account_Details SET Current = '%s' WHERE Acc_No = '"+ user +"'",record)
                                elif (CHOICE_C == 2):
                                    amt = int(input("Enter Amount to transfer: "))
                                    print('Loading......Please wait while your transaction is being completed.....')
                                    playsound('atmsound.mp3')                                    
                                    print('3...')
                                    time.sleep(1)
                                    print('2...')
                                    time.sleep(1)
                                    print('1...')
                                    time.sleep(0.5)
                                    print('Amount transferred: ₹', amt , '\n')
                                    mysql_insert = "insert into MINI (Acc_No, Date_Of_Transaction, Type_Of_Transaction, FROM_, TO_, Amount) values (%s, %s, %s, %s, %s, %s)"
                                    ct = datetime.datetime.now()
                                    tot = 'Transfer'
                                    _from_ = 'Savings'
                                    _to_ = 'Axis'
                                    amt_transfer = amt
                                    variables = (user,ct,tot, _from_ , _to_ , amt_transfer)
                                    a.execute(mysql_insert, variables)
                                    continue_prompt = str(input('Do you want to print receipt? Please keep in mind the effect on the environment (yes/no)? '))                                      
                                    b = continue_prompt.lower()                            
                                    if (b[0] == 'y'):
                                        playsound('printersound.mp3')
                                        print('**** Receipt Printed ****')
                                    a.execute("select Savings from Account_Details WHERE Acc_No = '"+ user +"'")
                                    c=a.fetchone()
                                    price = int(c[0])
                                    record = price-amt
                                    a.execute("UPDATE Account_Details SET Savings = '%s' WHERE Acc_No = '"+ user +"'",record)
                                else:
                                    print("\nENTER VALID INPUT! \n \n")
                                    continue
                                continue_prompt = str(input('Do you want to continue (yes/no)? '))
                                b = continue_prompt.lower()
                                link.commit()                            
                                if (b[0] == 'y'):
                                    continue
                                else:                            
                                    break;                           
                            elif (CHOICE_B3_1 == 4):#CITI
                                print ('1. Current \n2. Savings')
                                CHOICE_C = int(input('Enter Account: '))
                                if (CHOICE_C == 1):
                                    amt = int(input("Enter Amount to transfer: "))
                                    print('Loading......Please wait while your transaction is being completed.....')
                                    playsound('atmsound.mp3')                                    
                                    print('3...')
                                    time.sleep(1)
                                    print('2...')
                                    time.sleep(1)
                                    print('1...')
                                    time.sleep(0.5)
                                    print('Amount transferred: ₹', amt , '\n')
                                    mysql_insert = "insert into MINI (Acc_No, Date_Of_Transaction, Type_Of_Transaction, FROM_, TO_, Amount) values (%s, %s, %s, %s, %s, %s)"
                                    ct = datetime.datetime.now()
                                    tot = 'Transfer'
                                    _from_ = 'Current'
                                    _to_ = 'CITI'
                                    amt_transfer = amt
                                    variables = (user,ct,tot, _from_ , _to_ , amt_transfer)
                                    a.execute(mysql_insert, variables)
                                    continue_prompt = str(input('Do you want to print receipt? Please keep in mind the effect on the environment (yes/no)? '))                                      
                                    b = continue_prompt.lower()                            
                                    if (b[0] == 'y'):
                                        playsound('printersound.mp3')
                                        print('**** Receipt Printed ****')
                                    a.execute("select Current from Account_Details WHERE Acc_No = '"+ user +"'")
                                    c=a.fetchone()
                                    price = int(c[0])
                                    record = price-amt
                                    a.execute("UPDATE Account_Details SET Current = '%s' WHERE Acc_No = '"+ user +"'",record)
                                elif (CHOICE_C == 2):
                                    amt = int(input("Enter Amount to transfer: "))
                                    print('Loading......Please wait while your transaction is being completed.....')
                                    playsound('atmsound.mp3')                                    
                                    print('3...')
                                    time.sleep(1)
                                    print('2...')
                                    time.sleep(1)
                                    print('1...')
                                    time.sleep(0.5)
                                    print('Amount transferred: ₹', amt , '\n')
                                    mysql_insert = "insert into MINI (Acc_No, Date_Of_Transaction, Type_Of_Transaction, FROM_, TO_, Amount) values (%s, %s, %s, %s, %s, %s)"
                                    ct = datetime.datetime.now()
                                    tot = 'Transfer'
                                    _from_ = 'Axis'
                                    _to_ = 'CITI'
                                    amt_transfer = amt
                                    variables = (user,ct,tot, _from_ , _to_ , amt_transfer)
                                    a.execute(mysql_insert, variables)
                                    continue_prompt = str(input('Do you want to print receipt? Please keep in mind the effect on the environment (yes/no)? '))                                      
                                    b = continue_prompt.lower()                            
                                    if (b[0] == 'y'):
                                        playsound('printersound.mp3')
                                        print('**** Receipt Printed ****')
                                    a.execute("select Savings from Account_Details WHERE Acc_No = '"+ user +"'")
                                    c=a.fetchone()
                                    price = int(c[0])
                                    record = price-amt
                                    a.execute("UPDATE Account_Details SET Savings = '%s' WHERE Acc_No = '"+ user +"'",record)
                                else:
                                    print("\nENTER VALID INPUT! \n \n")
                                    continue
                                continue_prompt = str(input('Do you want to continue (yes/no)? '))
                                b = continue_prompt.lower()
                                link.commit()                            
                                if (b[0] == 'y'):
                                    continue
                                else:                            
                                    break;                             
                        elif (CHOICE_B3 == 2):#TRANSFER__CURRENT to SAVINGS
                                link = pymysql.connect(host='localhost', user='root', password='IPProject123!', db = 'ATM')
                                a = link.cursor()
                                a.execute("select Current from Account_Details WHERE Acc_No = '"+ user +"'")                            
                                c1=a.fetchone()
                                current =int(c1[0])
                                a.execute("select Savings from Account_Details WHERE Acc_No = '"+ user +"'")
                                c2 =a.fetchone()
                                savings =int(c2[0])
                                print('Current Account Balance: ₹', current)
                                print('Savings Account Balance: ₹', savings)
                                amt = int(input('Enter amount for transfer: '))
                                new_current = current - amt
                                a.execute("UPDATE Account_Details SET Current = '%s' WHERE Acc_No = '"+ user +"'",new_current)
                                new_savings = savings + amt
                                a.execute("UPDATE Account_Details SET Savings = '%s' WHERE Acc_No = '"+ user +"'",new_savings)
                                print('Loading......Please wait while your transaction is being completed.....')
                                playsound('atmsound.mp3')                                
                                print('3...')
                                time.sleep(1)
                                print('2...')
                                time.sleep(1)
                                print('1...')
                                time.sleep(0.5)
                                print('After transfer, balance remaining:')
                                print('Current Account: ₹', new_current)
                                print('Savings Account: ₹', new_savings)
                                mysql_insert = "insert into MINI (Acc_No, Date_Of_Transaction, Type_Of_Transaction, FROM_, TO_, Amount) values (%s, %s, %s, %s, %s, %s)"
                                ct = datetime.datetime.now()
                                tot = 'Transfer'
                                _from_ = 'Current'
                                _to_ = 'Savings'
                                amt_transfer = amt
                                variables = (user,ct,tot, _from_ , _to_ , amt_transfer)
                                a.execute(mysql_insert, variables)
                                continue_prompt = str(input('Do you want to print receipt? Please keep in mind the effect on the environment (yes/no)? '))                                      
                                b = continue_prompt.lower()                            
                                if (b[0] == 'y'):
                                    playsound('printersound.mp3')
                                    print('**** Receipt Printed ****')
                                continue_prompt = str(input('Do you want to continue (yes/no)? '))
                                b = continue_prompt.lower()
                                link.commit()                        
                                if (b[0] == 'y'):
                                    continue
                                else:                            
                                    break;                        
                        elif (CHOICE_B3 ==3 ):#TRANSFER__SAVINGS to CURRENT
                                link = pymysql.connect(host='localhost', user='root', password='IPProject123!', db = 'ATM')
                                a = link.cursor()
                                a.execute("select Savings from Account_Details WHERE Acc_No = '"+ user +"'")                            
                                c1=a.fetchone()
                                savings =int(c1[0])
                                a.execute("select Current from Account_Details WHERE Acc_No = '"+ user +"'")
                                c2 =a.fetchone()
                                current =int(c2[0])
                                print('Savings Account Balance: ₹', savings)
                                print('Current Account Balance: ₹', current)
                                amt = int(input('Enter amount for transfer: '))
                                new_savings = savings - amt
                                a.execute("UPDATE Account_Details SET Savings = '%s' WHERE Acc_No = '"+ user +"'",new_savings)
                                new_current = current + amt
                                a.execute("UPDATE Account_Details SET Current = '%s' WHERE Acc_No = '"+ user +"'",new_current)
                                print('Loading......Please wait while your transaction is being completed.....')
                                playsound('atmsound.mp3')                                
                                print('3...')
                                time.sleep(1)
                                print('2...')
                                time.sleep(1)
                                print('1...')
                                time.sleep(0.5)
                                print('After transfer, balance remaining:')
                                print('Savings Account: ₹', new_savings)
                                print('Current Account: ₹', new_current)
                                mysql_insert = "insert into MINI (Acc_No, Date_Of_Transaction, Type_Of_Transaction, FROM_, TO_, Amount) values (%s, %s, %s, %s, %s, %s)"
                                ct = datetime.datetime.now()
                                tot = 'Transfer'
                                _from_ = 'Savings'
                                _to_ = 'Current'
                                amt_transfer = amt
                                variables = (user,ct,tot, _from_ , _to_ , amt_transfer)
                                a.execute(mysql_insert, variables)
                                continue_prompt = str(input('Do you want to print receipt? Please keep in mind the effect on the environment (yes/no)? '))                                      
                                b = continue_prompt.lower()                            
                                if (b[0] == 'y'):
                                    playsound('printersound.mp3')
                                    print('**** Receipt Printed ****')
                                continue_prompt = str(input('Do you want to continue (yes/no)? '))
                                b = continue_prompt.lower()
                                link.commit()                        
                                if (b[0] == 'y'):
                                    continue
                                else:                            
                                    break;
                       
                        else:
                           print("\nENTER VALID INPUT! \n \n")
                           continue
                       
                    elif(CHOICE_B == 4):#PIN CHANGE
                        link = pymysql.connect(host='localhost', user='root', password='IPProject123!', db = 'ATM')
                        a = link.cursor()
                        original_pin = input('Enter PIN: ')                           
                        if (pin_main != original_pin):
                            print(' \nInvalid username or password! \n \n')
                            continue
                        else:
                            print(" \nLOGIN AUTHORIZED!! \n \n ")
                            new_pin = input('Enter new PIN: ')
                            confirm_new_pin = input('Confirm new PIN: ')
                            if (new_pin != confirm_new_pin):
                                print(' \nInvalid PIN, try again! \n \n')
                                continue
                            else:
                                a.execute("UPDATE Account_Details SET PIN = '" + new_pin + "' WHERE Acc_No = '" + user + "'")
                                mysql_insert = "insert into MINI (Acc_No, Date_Of_Transaction, Type_Of_Transaction, FROM_, TO_, Amount) values (%s, %s, %s, %s, %s, %s)"
                                ct = datetime.datetime.now()
                                tot = 'PIN CHANGE'
                                _from_ = original_pin
                                _to_ = new_pin
                                amt_transfer = 0
                                variables = (user,ct,tot, _from_ , _to_ , amt_transfer)
                                a.execute(mysql_insert, variables)
                                link.commit()
                                print('Loading......Please wait while your PIN is being changed.....')
                                time.sleep(2)
                                print('3...')
                                time.sleep(1)
                                print('2...')
                                time.sleep(1)
                                print('1...')
                                time.sleep(0.5)
                                print('PIN change successful, please log in again')
                                    
                    elif(CHOICE_B == 5):#ACCOUNT DETAILS
                        link = pymysql.connect(host='localhost', user='root', password='IPProject123!', db = 'ATM')
                        a = link.cursor()
                        a.execute("select Acc_No from Account_Details WHERE Acc_No = '"+ user +"'")
                        c1=a.fetchone()
                        d1=int(c1[0])
                        print('Account Number:     ', d1)
                        a.execute("select PIN from Account_Details WHERE Acc_No = '"+ user +"'")
                        c2=a.fetchone()
                        d2=int(c2[0])
                        print('PIN:                ', d2)
                        a.execute("select Current from Account_Details WHERE Acc_No = '"+ user +"'")
                        c3=a.fetchone()
                        d3=int(c3[0])
                        print('Current Account:    ', d3)
                        a.execute("select Savings from Account_Details WHERE Acc_No = '"+ user +"'")
                        c4=a.fetchone()
                        d4=int(c4[0])
                        print('Savings Account:    ', d4)
                        link.commit()
                                
                    elif(CHOICE_B == 6):#MINI STATEMENT
                        link = pymysql.connect(host='localhost', user='root', password='IPProject123!', db = 'ATM')
                        a = link.cursor()                        
                        #a.execute("select Sl_No, Acc_No, year(Date_Of_Transaction), month(Date_Of_Transaction), day(Date_Of_Transaction), hour(Date_Of_Transaction), minute(Date_Of_Transaction), second(Date_Of_Transaction), Type_Of_Transaction, FROM_, TO_, Amount from MINI where Acc_No = '"+ user +"' order by Sl_No DESC")                                                                                                                       
                        a.execute("select Sl_No, Acc_No,Date_Of_Transaction, Type_Of_Transaction, FROM_, TO_, Amount from MINI where Acc_No = '"+ user +"' order by Sl_No DESC")
                        c=a.fetchall()
                        cnt=0
                        print('Last 10 transactions:')
                        for row in c:
                            cnt+=1
                            if(cnt<=10):
                                print(cnt)
                                """
                                print("Transaction ID = ", row[0])
                                print("Account Id = ", row[1])
                                print("Year = ", row[2])
                                print("Month = ", row[3])
                                print("Day = ", row[4])
                                print("Hour = ", row[5])
                                print("Minute = ", row[6])
                                print("Second = ", row[7])
                                print("Type  = ", row[8])
                                print("From  = ", row[9])
                                print("To  = ", row[10])
                                print("Amount  = ", row[11], "\n\n")
                                """
                                print("Transaction ID = ", row[0])
                                print("Account Id = ", row[1])
                                print("Date = ", row[2])
                                print("Type = ", row[3])
                                print("From = ", row[4])
                                print("To = ", row[5])
                                print("Amount = ", row[6], "\n\n")
                                time.sleep(0.5)
                            else:
                                break
                        link.commit()
                        

                    elif (CHOICE_B == 7):
                        print('\nAbout:')
                        print('Gafan Commercial Bank Limited is India\'s largest bank, both for personal and for business applications. It was founded in 20th April 1969 under the stewardship of Shri Reeshav Sinha. Throughout the years')
                        print('it has grown from strength to strength and has now become India\'s largest private bank. It has a total market capitalization of $1.5 trillion, and it\'s cash reserves are amongst the highest in the world,')
                        print('amounting to $5 trillion. GCBL has an estimated 2 billion customers worldwide, with majority of them in India. GCBL\'s infrastructure is second to none, with more than 200,000 ATMs across India,')
                        print('along with dozens of branches in major city. We are proud to be worthy of the love and trust of our customers. \n')
                        print('Current Board of Directors: ')
                        print('Reeshav Sinha - CEO of GCBL')
                        print('Website: https://www.onlinegcbl.gcbl \n')
                        print('\nYour current location shows Bengaluru. Here is a list of addresses of every GCBL branch in Bengaluru:')
                        print('Ade Bangalore, Aditya Nagar, Aecs Layout, Aero Engine Factory, Afs Jalahalli East, Afs Jalahalli West, Afs Yelahanka Banglore, Air Cargo Complex Bangalore, Air Craft Factory, Airport Road')
                        print('Airport Road Yelahanka, Akshayanagar, Amc Engineering College, Anandnagar, Anekal, Arekere, Asc Centre South , Atomic Energy Dept Bangalore, Attibele, Austin Town, Austin Town Bangalore')
                        print('Avalahalli, B R Market, B S K Stage, Babusapalya, Bagalur, Bagmane Tech Park, Banagalore White Field, Banashankari, Banashankari 3rd Stage, Banashankari 6th Stage Bangalore, Banashankari Bangalore,')
                        print('Banashankari Ii Stage Bangalore, Banaswadi, Banaswadi Bangalore, Bangalore, Bangalore City, Bangalore Gokul, Bangalore Hsr Layout, Bangalore J P Nagar, Bangalore Zonal Office, Bangalore Zone Three,')
                        print('Bangalore Zone Two, Bangaluru Yelahanka, Banglore Indira Nagar, Banglore Nr Square, Bannerghatta Bangalore, Basavakalyan, Basavanagudi, Basavangudi, Basaveshwar Nagar, Basaveshwara Nagar')
                        print('Basaveswaranagar, Basaweshwaranagar, Bashyam Circle Bangalore, Basvangudi, Basweshar Nagar, Begur, Begur Cross, Bellandur, Bengaluru Hudson Circle Branch, Benson Town, Bharath Nagar,')
                        print('Bharti Nagar Bangalore, Bidadi, Bilekahally, Block Rajajinagar, Bommanahalli Bangalore, Bommasandra, Btm Layout, Btm Layout Bengaluru, Byatarayanapura, Byrasandra, Byraveshwar Nagar, C V Raman Nagar,')
                        print('Cauvery Bhavan, Cbab Complex, Central Business District Bangalore, Central Pension Processing Centre, Centralised Clearing Procerssing Cell, Cgo Complex, Chamarajpet, Chandapura, Chandra Layout,')
                        print('Chandra Layout Bangalore, Chandralayout Bangalore, Channapatna, Channasandra, Chickpet, Chikka Tirupathi Road, Chikkabanavara, Cholanagar, Church Street Bangalore, City, City Market, Cleveland Town,')
                        print('Coffee Board Layout, Commercial Branch Bangalore, Commercial Branch Rajajinagar, Concor, Cooke Town, Cottonpet, Cox Town, Cox Town Bangalore, Cpri Bangalore, Cunningham Rd, Cv Raman Nagar, D N Road,')
                        print('Damtal, Dasanapura, Devanahalli, Devanahalli Aircargo Complex, Doddabanaswadi, Doddakallasandra, Dollar Colony, Dollars Colony Branch, Dommasandra, Doorvani Nagar, Dr Ambedkar Veedhi,')
                        print('Dr Shivaram Karanth Nagar, Eight Mile Hesaraghatta, Electronic City Bangalore, Electronic City Bengaluru, Focal Point Link Branch Bangalore, Fort, Fort Branch, G Seva Branch, Gangenahalli,')
                        print('Gayathri Nagar, Girinagar, Gottigere, Hal Bangalore, Hanumagiri, Hanumanthanagar, Hbr Layout, Health City, Hebbal, Helicopter Factory, Hesargatta Road Bangalore, Hmt Indl Estate, Hmt Lay Out,')
                        print('Hongasandra, Honnali, Hoody, Hope Farm Circle, Horamavu, Hosur Road, Hrbr Layout, Hrbr Layout Bangalore, Hsr Layout, Hsr Layout Bengaluru, Hsr Layout Rd Sector, Hsr Layout Sector, Hulimavu,')
                        print('Ideal Homes, Ifb, Ifb Bangalore, Iim Campus, Iis Campus, Ind Finance Br, Indira Nagar, Indiranagar Hal Ii Stage, Int Airport Road, Isec, Isro Vimanpura, Iti Aie Mahadevapur, Itpl Campus, J C Rd,')
                        print('J C Road, J P Nagar, J P Nagar Eight Phase, J P Nagar Seventh Phase, Jalahalli, Jayamahal Extension Bangalore, Jayanagar, Jayanagar Block, Jayanagar Ii Block, Jayanagar Iv Block, Jc Nagar Bangalore,')
                        print('Jeevan Bhima Nagar, Jeevanbhima Nagar Bangalore, Jigani, Jigani Industrial Area Bangalore Rural, Jp Nagar, Jp Nagar Bengaluru, K R Puram, Kacharakanahalli, Kadugodi Bangalore, Kaggalipura,')
                        print('Kalyan Nagar, Kamakshipalya, Kanakapura, Kanakapura Road, Kandaya Bhavan, Kannur, Kasturi Nagar, Kathriguppe, Kaval Byrasandra, Kengeri, Kengeri Satellite Town, Kiocl Campus, Kodichikkanahalli,')
                        print('Konanakunte, Koramangala, Koramangala Block, Kothanur, Krishnaraja Puram, Kudlu, Kumara Park, Kumaran Childrens Home, Kumarswami Layout, Kumbalgodu, Kundalahalli, Kyathanagere Layout, L C Rd, Lakho,')
                        print('Langford Town Branch, Lingarajapuram, M G Rd, M G Road, M S Bldgs, Madhavanagar, Madhavara, Madhura Colony, Magadi Road Bangalore, Mahalakshmi Layout, Malagala Road Bangalore, Mallathahalli,')
                        print('Mallathahally, Malleshwaram, Malleswaram, Marathahalli, Market Yard Yeshwanthpur, Marthahalli, Mathikere, Mathikere Road, Meg Centre B Lore, Mes College Malleswaram, Metro Branch Bangalore,')
                        print('Mico Layout, Mid Corp Loan Admin Unit Bangalore, Mid Corporate Branch Gandhi Nagar Bangalore, Mission Road Bangalore, Mission Road Branch Banglore, Mysore Road, Mysore Road Branch Bhel, N A L,')
                        print('N R Colony, Nagadevanahalli, Nagarabhavi, Nagarabhavi Stage, Nagawarpalya, Nandini Layout, Navanagar Bagalkot, New Bel Road, New Tharagupet, Ngef, Nimhans, Nri Branch Bangalore, Nri Branch Koramangala,')
                        print('Office Administration Dept H O, Office Administration Lho Bangalore, Office Administration Zonal Office Bangalore, Overseas Branch Bangalore, P Sb Indiranagar, P U B Branch Bangalore, Padmanabha Nagar,')
                        print('Padmanabhanagar Banglore, Panathur, Pbb Gandhi Ngr, Pbb Indiranagar, Pbb Jayanagar, Pbb Koramangala, Pbb Malleswaram, Pbb Mysore, Pbb Palace Orchards Bangalore, Peenya, Peenya Indl Area Br,')
                        print('Peenya Indus Estate Bangalore, Personal Banking Branch, Pillana Gardens Bangalore, Prashanth Nagar, Priority Banking Centre Bengalore, Puttenahalli, R K Layout, R P C Layout, R T Nagar,')
                        print('Race Course Road, Racpc, Rajaji Nagar V Block Bangalore, Rajajinagar, Rajajinagar Bangalore, Rajajinagar Ind Est, Rajanukunte, Rajarajeshwari Nagar, Rajarajeswari Nagar, Rajmahal Vilas Extn,')
                        print('Ramagondanahalli, Ramamurty Nagar, Ramanagaram, Ramanjaneyanagar, Rasmecc Bangalore, Rbi Layout Bangalore, Rbo R 1 Bangalore, Region I, Region Ii, Region Iii, Region Iv,')
                        print('Remote Rm Centre Wealth Bangalore, Residency Roadbangalore, Retail Assets Central Processing Centre Racpc , Richards Town, Richmond Roadbranch, Rmv Ii Stage, Rpc Layout, S M C Branch Jayanagar,')
                        print('Sadashiva Nagar, Sahakaranagar, Sahakari Nagar, Samb Bangalore, Sampangiramnagar, Sanjay Nagar, Sanjay Nagar Bangalore, Sarakki, Sarjapur Road Bangalore, Sarjapura, Sarjapura Road,')
                        print('gcblintouch Lite Branch Whitefield, gcblintouch Lite Brookfield Bangalore, gcblintouch Lite Electronics City Bangalore, gcblintouch Lite Jayanagar Bangalore, gcblintouch Lite Vijayanagar Bangalore,')
                        print('gcblintouch Nagavara Bangalore, Sbm Colony, Seegehalli, Service Branch, Service Branch Blore, Seshadripuram, Shankarapuram, Shf Jayanagar, Shivajinagar, Siwanchety Garden Bangalore,')
                        print('Sme City Credit Centre Bangalore, Spb Sarjapur Road Branch, Spbb Bangalore, Specialised Sme Peenya Ii Stage, Srinagar Bangalore, Ssi Jp Nagar, Ssi Peenya I E Bangalore, Ssi Peenya Ind Estate,')
                        print('Ssi Singasandra, Stressed Assets Resolution Centre, Subedarchatram Road, Subramanyanagar, Sudhamanagar, Sultan Palya Bangalore, Sunkadakatte, T F C P C, Tata Silk Farm, Thanisandra, Thygarajanagar,')
                        print('Trade Finance Bangalore, Treasury, Ullal, Ulsoor Bangalore, Uttarahalli, Vasanth Nagar Bangalore, Vasanthapura, Vayalikaval, Vidhana Soudha, Vidyaranyapura, Vidyaranyapura Bengaluru, Vidyarnyapura,')
                        print('Vijay Nagar Extension, Vijaya Nagar, Vijayanagar, Vijayanagar Iiird Stage, Vijayapura Branch, Vijinapura Bangalore, Vikramnagar, Vinayaka Layout, Vishweshwarapuram Bangalore, Visweswarapuram,')
                        print('West Of Chord Road, West Of Chord Road Bangalore, Whitefield, Whitefield Bangalore, Wilson Garden, Wilson Gardens Branch, Yelahanka, Yelahanka New Town, Yelahanka New Town Branch, Yeswantpur,')
                        print('Zonal Inspection Office Bhubaneswar.')
                        continue_prompt = str(input('Do you want to continue (yes/no)? '))
                        b = continue_prompt.lower()
                        link.commit()                        
                        if (b[0] == 'y'):
                            continue
                        else:                            
                            break;

                    elif (CHOICE_B == 8):
                        continue_prompt = str(input('Do you wish to leave (yes/no)? '))                                      
                        b = continue_prompt.lower()
                        link.commit()                            
                        if (b[0] == 'y'):
                            print('Thank you for visiting Gafan Commercial Bank Limited!!! Please come again!')
                            break
                         
                    else:
                            print("\nENTER VALID INPUT! \n \n")
                            continue      
    else:
        print("\nENTER VALID INPUT! \n \n")
