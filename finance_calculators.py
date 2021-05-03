#This program calculates:
#1.) The total returns on investment, using
#    a) simple interest,  or
#    b) compound interest
# OR
#2.) The montly bond repayment on a home loan.



#The math module is imported to calculate exponents (W3schools.com, 2021, Python math.pow() Method, t.ly/nMwH):

import math



#Function "main()" is defined as all indented code after the colon. 
#This function will help loop the code in case of invalid input (MrLauLearning, 2016, Python Tutorial 11, t.ly/0vUx).
#Note: "main()" is not being run at this point, merely defined:

def main():

        #The user selects "investment" or "bond" from the menu,
        #and their input is stored as variable "user_choice":
        
        user_choice = input("""\nChoose either 'investment' or 'bond' from the menu below to proceed:

investment:\t- to calculate the amount of interest you'll earn on interest
bond:\t\t- to calculate the amount you'll have to pay on a home loan\n\n""")
        

        #An if/elif/else statement (Hyperiondev, 2021, Beginner Control Structures - elif Statements, p.2-3),
        #is used to structure the rest of "main()".

        #If the user chooses "investment",
        #four main variables are declared according to user input:
        #1.) deposit amount, 2.) interest rate, 3.) interest rate expressed as a decimal, and 4.) investment period.
        #Note: A tuple (Python.org, 2021, 5. Data Structures, t.ly/cDd0)
        #is used to accommodate user capitals/variations using "in (tuple)" (Pieters, 2012, Stackoverflow.com, t.ly/qWp3):

        if user_choice in ("investment","Investment","INVESTMENT","i","I"):

                deposit = float(input("\n\nPlease enter your deposit amount(rands):\n\n"))
                
                rate = float(input("\n\nPlease enter the interest rate(%):\n\n"))

                rate_deci = rate/100
                
                time = int(input("\n\nPlease enter how many years you plan on investing:\n\n"))
                
                #"deposit_2" and "rate_2" are also declared, using "format(x,".yf")" (Pieters, 2013, Stackoverflow.com, t.ly/hXOk).
                #"format(x,".yf")" changes a numerical variable "x" into a string that always displays "y" decimals.
                #In case "deposit" and "rate" are whole numbers, Python will only display one decimal,
                #but because they are monetary and percentage values, we always want two decimals displayed:
                
                deposit_2 = format(deposit,".2f")
                
                rate_2 = format(rate,".2f")

        

                #Another function, "minor()", is defined within "main()",
                #to help loop the code in case of invalid entry.
                #Again, function "minor()" is not yet being run, merely defined:

                def minor():

                        #The user selects "simple" or "compound" interest:
                                        
                        user_choice_2 = input("\n\nPlease choose either 'simple' or 'compound' interest:\n\n")
                        

                        #Another if/elif/else statement is used to structure the rest of "minor()". 
                                     
                        #If the user selects simple interest (again a tuple is used in case of user variation),
                        #then variable "int_type" is set to "simple",
                        #and the total investment return calculated using formula "total = deposit x (1 + rate x time)"
                        #(Hyperiondev, 2021, Capstone Project 1, p.9).
                        #The total is rounded off to two decimals using "round(x,y)" (W3schools.com, 2021, www.w3schools.com/python/ref_func_round.asp),
                        #and fixed as a two-decimal string using "format(x,".yf")": 

                        if user_choice_2 in ("simple", "Simple", "SIMPLE","s","S"):
                                
                                int_type = "simple"
                                
                                total = format(round((deposit*(1 + rate_deci*time)),2),".2f")

                                #The total amount is displayed in one sentence along with the investment period, interest rate, deposit,
                                #and summary, using an f-string (Hyperiondev, 2021, The String Data Type, p.4), 
                                #and triple quotations (Hyperiondev, 2021, The String Data Type, p.2)
                                #to make adding the visual aid easier:

                                print(f"""\n\n\nAfter {time} years at {rate_2}% interest, with a deposit of R{deposit_2},
you will have earned interest up to a total amount of R{total}:

--------------------------------------------------------------------------------

deposit:\t\t\tR {deposit_2}

interest rate:\t\t\t{rate_2}%

investment period:\t\t{time} years

investment type:\t\t{int_type}

total amount:\t\t\tR {total}

--------------------------------------------------------------------------------""")

                        #Else, if the user chooses compound interest,
                        #then "int_type" is set to "compound",
                        #and the total amount calculated using formula "total = deposit x (1 + rate)^time"
                        #(Hyperiondev, 2021, Capstone Project 1, p.9).
                        #Note, the "math.pow(x,y)" function is used to calculate exponents (x = number, y = exponent)
                        #(W3schools.com, 2021, Python math.pow() Method, t.ly/o0fl). 

                        elif user_choice_2 in ("compound", "Compound", "COMPOUND","c","C"):
                                
                                int_type = "compound"
                                
                                total = format(round((deposit*math.pow((1 + rate_deci),time)),2),".2f")
                                
                                #The total amount, investment period, interest rate, deposit, and summary are displayed:      

                                print(f"""\n\n\nAfter {time} years at {rate_2}% interest, with a deposit of R{deposit_2},
you will have earned interest up to a total amount of R{total}:

--------------------------------------------------------------------------------

deposit:\t\t\tR {deposit_2}

interest rate:\t\t\t{rate_2}%

investment period:\t\t{time} years

investment type:\t\t{int_type}

total amount:\t\t\tR {total}

--------------------------------------------------------------------------------""")


                        #Else (if the user didn't enter "simple" or "compound"), an error message is displayed,
                        #and the user asked if they want to restart.
                        #If "yes" then "minor()" is run, if "no", the program closes.
                                
                        #In case user doesn't enter "yes" or "no"
                        #A while loop (Hyperiondev, 2021, Beginner Control Structurs - While Loop, p.3),
                        #and two if statements are used to loop back to the error message.
                        
                        #First, Boolean variable "invalid_entry_minor" is set to "True" (outside the loop) if the user didn't choose "simple" or "complex".
                        #Then, while "invalid_entry" is True, the code loops back to the error message,
                        #and terminates as soon as the user enters "yes" or "no" ("invalid_entry" becomes "False" in both cases):
                
                                
                        else:
                                invalid_entry_minor = True
                                
                                while invalid_entry_minor:
                                        
                                        restart_minor = input("""\n\nSorry, that was an invalid entry.

Would you like to try again? Please enter 'yes' or 'no':\n\n""")
                                                
                                        
                                                
                                        if restart_minor in ("yes","Yes","YES","y","Y"):
                                                
                                                invalid_entry_minor = False
                                                
                                                minor()
                                                
                                        if restart_minor in ("no","No","NO","n","N"):
                                                
                                                invalid_entry_minor = False
                                                
                                                exit()



                #Last, "minor()" is run.
                #The code will start at "Please choose either "simple" or "compound" interest:"
                        
                minor()


        #Back in "main()", if the user chose bond in the first choice,
        #then five main variables are declared,
        #1.) property value, 2.) interest rate, 3.) interest rate expressed as decimal,
        #4.) repayment period, and 5.) monthly interest rate.
        #Note "value_2" is also declared, using "format(x,".yf")", in case the property value is a whole number.
                
        elif user_choice in ("bond","Bond","BOND","b","B"):

                value = float(input("\n\nWhat is the present value of the property (Rands):\n\n"))
                
                value_2 = format(value,".2f")
                
                rate = float(input("\n\nPlease enter the interest rate(%):\n\n"))
                
                rate_deci = rate/100
                
                time = int(input("\n\nPlease enter how many months you plan on repaying your bond:\n\n"))
                
                month_rate = rate_deci/12

                #The monthly bond repayment amount is calculated using 
                #"monthly rate = (montly rate x property value)/(1 - (1/(1 + monthly rate)^total months))"
                #(Hyperiondev, 2021, Capstone Project 1, p.9).
                #Again the amount is rounded off to two decimals using "round()",
                #and casted to a two-decimal string using "format(x,".yf")", in case the amount is a whole number.

                per_month = format(round((month_rate*value)/(1 - math.pow((1/(1 + month_rate)),time)),2),".2f")     
        
                #The monthly bond amount is displayed along with the property value and repayment period,
                #using an f-string and triple quotations again:
                
                print(f"""\n\n\nFor a bond of R{value_2}, you will have to pay R{per_month} per month for {time} months:

--------------------------------------------------------------------------------------

bond:\t\t\t\tR {value_2}
        
repayment period:\t\t{time} months
        
monthly repayment:\t\tR {per_month} per month

--------------------------------------------------------------------------------------""")
                
        #Else, (if the user didn't enter "investment" or "bond"), an error message is displayed,
        #and the user asked if they would like to continue.
        #If "yes", "main()" is started again.
        #if "no", the program closes.
        #If the user enters anything else, a while loop is used again to loop back to the error message,
        #using the exact same structure as in the first while loop in "minor()":
                
        else:
                invalid_entry_main = True
                
                while invalid_entry_main:
                        
                        restart_main = input("""\n\nSorry, that was an invalid entry.

Would you like to start again? Please enter 'yes' or 'no':\n\n""")
                
                        if restart_main in ("yes","Yes","YES","y","Y"):
                                
                                invalid_entry_main = False
                                
                                print()
                                
                                main()
                        
                        if restart_main in ("no","No","NO","n","N"):
                                
                                invalid_entry_main = False
                                
                                exit()
                                


#Last, "main()" is run.
#The code will start at "Choose either 'investment' or 'bond' from the menu below to proceed:"
                        
main()
                        




####################### THE END ###########################








