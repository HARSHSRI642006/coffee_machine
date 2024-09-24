MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

penny = 0.01
dime = 0.10
nickel = 0.05
quarter = 0.25
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0



logo = r"""     (  )   (   )  )
     ) (   )  (  (
     ( )  (    ) )
     _____________
    <_____________> ___
    |             |/ _ \
    |               | | |
    |               |_| |
 ___|             |\___/
/    \___________/    \
\_____________________/


"""
print(logo)
print("WELCOME TO COFFEE MACHINE!")
play_2 = True
while play_2:     
 
 user_input = input("What would you like? (espresso/latte/cappuccino) (FOR MACHINE INFO TYPE 'REPORT'AND 'OFF' TO TURN OFF THE MACHINE):").lower()
 
 def off():
    print("Thank you for using the machine!")
    return
 if user_input == "off":
    off()
    play_2 = False
    
    
    
 if user_input == "report":
     print(f"milk: {milk}ml")
     print(f"water:{water}ml")
     print(f"coffee:{coffee}ml")
     print(f"money:{money}$")
     



 def cappuccino():
     global milk,water,coffee,play_2
     info_input = input("Do yo want information regarding cappucino?,Type Yes on no:").lower()
     def follow_on():
      print("Please insert coins:")
      quarter_input = int(input("How many quarters?:"))

      dime_input = int(input("How many dimes?:"))

      nickel_input = int(input("How many nickels?:"))

      penny_input = int(input("How many pennies?:"))
      money = quarter_input*quarter + dime_input*dime+nickel_input*nickel+penny_input*penny
      if milk<100 :
         print("There is not enough milk!")
        
         return
      if water<250:
         print("There is not enough water!")
        
         return
      if coffee<24:
         print("There is not enough coffee!")
        
         return
      if money<3:
         print("Sorry,that not enough money!,money refunded")
        
         return 
      milk = milk - MENU["cappuccino"]["ingredients"]["milk"]
      coffee= coffee - MENU["cappuccino"]["ingredients"]["coffee"]
      water = water - MENU["cappuccino"]["ingredients"]["water"]
      money_left = round(money- MENU["cappuccino"]["cost"],2)
     
      print("Here is your cappuccino ☕ enjoy!")
      print( f"Here is {money_left} in change.")
     if info_input == "yes":
        print(MENU["cappuccino"])
     follow_on()
     
     
 def latte():
     
     info_input = input("Do yo want information regarding cappucino?,Type Yes on no:").lower()
     
     def follow_on():   
      global milk,water,coffee,play_2
      print("Please insert coins:")
      quarter_input = int(input("How many quarters?:"))

      dime_input = int(input("How many dimes?:"))

      nickel_input = int(input("How many nickels?:"))

      penny_input = int(input("How many pennies?:"))
      money = round(quarter_input*quarter + dime_input*dime+nickel_input*nickel+penny_input*penny,2)
      if milk<150 :
         print("There is not enough milk!")
       
         return
      if water<200:
         print("There is not enough water!")
         return
      if coffee<24:
         print("There is not enough coffee!")
        
         return
      if money<2.5:
         print("Sorry,that not enough money!,money refunded")
         return 
     
      milk = milk - MENU["latte"]["ingredients"]["milk"]
      coffee= coffee - MENU["latte"]["ingredients"]["coffee"]
      water = water - MENU["latte"]["ingredients"]["water"]
      money_left = money- MENU["latte"]["cost"]
     
      print("Here is your latte ☕ enjoy!")
      print( f"Here is {money_left} in change.")   
     if info_input == "yes":
        print(MENU["cappuccino"])
        
     
     follow_on()
 def espresso():
     
     info_input = input("Do yo want information regarding cappucino?,Type Yes on no:").lower()
    
     def follow_on():   
      global milk,water,coffee,play_2
      print("Please insert coins:")
      quarter_input = int(input("How many quarters?:"))

      dime_input = int(input("How many dimes?:"))

      nickel_input = int(input("How many nickels?:"))

      penny_input = int(input("How many pennies?:"))
      money = round(quarter_input*quarter + dime_input*dime+nickel_input*nickel+penny_input*penny,2)
      if water<50:
         print("There is not enough water!")
        
         return
      if coffee<18:
         print("There is not enough coffee!")
       
         return
      if money<1.5:
         print("Sorry,that not enough money!,money refunded")
        
         return 
     
      coffee= coffee - MENU["espresso"]["ingredients"]["coffee"]
      water = water - MENU["espresso"]["ingredients"]["water"]
      money_left = money- MENU["espresso"]["cost"]
      print("Here is your espresso  ☕ enjoy!")
      print( f"Here is {money_left} in change.")    
      
     if info_input == "yes":
        print(MENU["cappuccino"])
        
     follow_on()
     
        
     
      
         
    
    
    
    




 if user_input == "cappuccino":
     cappuccino()
 if user_input == "latte":
     latte()    
 if user_input == "espresso":
     espresso()

