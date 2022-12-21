
users = {1000:2000,2000:1000}  #Admin level 

#Main function
def main():
    print("           (⌐■_■) Cɾҽα𝜏ҽԃ ßყ Sԋιʋα𝓶 ẞαɾι ᗯι𝜏ԋ Ⳑσʋҽ (>‿◠)✌\n\n")
    print("                  💲Welcome to ICIC Bank💲               \n\n")
    print("          🔷Enter number to perfom your task.🔷 \n 🔸1.Login \n 🔸2.View Login \n 🔸3.Account Info \n 🔸4.Exit            \n\n" )
    try:
        menu=int(input("Enter desired value: "))
        if (menu==1):
            login()
        elif (menu==2):
            view()
        elif (menu==3):
            account()
        elif (menu==4):
            print("(͡• ͜ʖ ͡•)\n©all rights reserved\nExiting..... ")
        else:
            print("Invalid Number❗❗\n Returning to main menue ↩")
            main()
            
    except(ValueError):
        print("Invalid input❗❗")
        main()
#______________________Login Function_____________________________


def login():
    print("******************************************************\n\n----------📲Login--------\n\n")
    global name,age,AadharNumber,UserID,c
    name=input("Enter your Name: ")
    age=int(input("Enter your age: "))
    UserID=int(input("Enter you User iD: "))
    print("~~~~~~~~~~~~Input Stored sucessfully✔✔~~~~~~~~~~~~~~")
    nex=int(input("\n🔷To View your info press 1 \n🔷To view account press 2 \n🔷To go to main menu press 3 :- "))
    if (nex==1):
        view()
    elif (nex==2):
        account()
    elif (nex==3):
        main()
    else:
        print("~~~~~~Invalid input❗❗~~~~~~\n        Returning to main menue.      \n")
        main()

#_________________________View Function______________________________   

def view():
    print("\n----------------🆔User Login Info----------------")
    print("◽Your Name:- ",name)
    print("◽Your Age:- ",age)
    print("◽Your UserID:-",UserID)
    print("◽Returning to home screen.")
    main()

#________________________Account Function____________________________

def account():
   
    if UserID==1000:
        Userd()
    elif UserID==2000:
        Userd()
    else:
        print("\n\nYour User ID is not valid Login with proper ID❗❗")
        login()

#___________________________Sub Transection Part________________________
    
def Userd():
    print("\n-------------------🏧Your Account------------------")
    print("\n💰Your balance is : ",users[UserID])
    print("🔹To visit to Transection page enter:- 1 \n🔹To exit enter:- 2 ")
    a=int(input("Enter desired value:"))
    if a==1:
        Transection()
    elif a==2:
        print("\n\nReturning to main menue.\n\n")
        main()
    else:
        print("\n\nInvalid input❗❗\n Returning to Account page.\n")
        account()
#____________________________Transection Part____________________________

def Transection():
    global tran
    print("\n\n------------------🏧Transection------------------\n\n")
    print("\n\n💰Your account balance is : ",users[UserID])
    tran=int(input("🔷Select the operation to perform🔷 \n 1.Withdraw 💳 \n 2.Deposit 💵 \n 3.Go back to Account page ↩\n🔸Enter number to perform operation:- "))
    if (tran==1):
          WithdrawFun()
    elif (tran==2):
        Deposit()
    elif (tran==3):
        account()
    else:
        print("Error 🚫\nTry again❗")
        Transection()


def WithdrawFun():
    a=int(input("How much money do you want to withdraw 💰 : "))
    if (a<=users[UserID]):
        users[UserID]=users[UserID] - a
        print("Opertaion Completed Sucessfully✔✔")
        account()
    else:
        print("\n\nNot Enough account balance❗❗\nTry again❗❗\n")
        WithdrawFun()

def Deposit():
    a=int(input("Enter the amount you want to Deposit 💰 : "))
    users[UserID]=users[UserID] + a
    account()

#_______________________________________________________________________

#Main function below
main()
