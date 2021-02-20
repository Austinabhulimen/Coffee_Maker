from materials import MENU, resources

#TODO: 1. print a report of all the coffee machine




#TODO: Funds calculator(to determine the total value of different change entered)

On = True
while On:

    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'report':
        print(f"Water: {resources['water']}ml \nmilk: {resources['milk']}ml"
              f"\ncoffee: {resources['coffee']}g\nmoney:${resources['money']}")
    else:
        print("please insert coin.")

        quarters = int(input("how many quarters?:"))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))

        def convert_into_dollar(quarters,dimes,nickles,pennies):

            dol_quarters = quarters*0.25
            dol_dimes = dimes*0.10
            dol_nickles = nickles*0.05
            dol_pennies = pennies*0.01
            result = dol_quarters + dol_dimes + dol_nickles + dol_pennies
            return round(result, 2)


        total_money_entered = convert_into_dollar(quarters,dimes,nickles,pennies)

        print(convert_into_dollar(quarters, dimes, nickles, pennies))




        def Check_resource_And_process_transaction(total_money_entered):

            latte_cost = int(2.50)
            money = latte_cost
            cappuccino_cost = int(3.00)
            espresso_cost = int(1.50)

            if choice == "latte" and int(total_money_entered) >= latte_cost:
                change = total_money_entered - latte_cost

                resources.update({"water": 300 -200, "milk": 200- 150, "coffee": 100 - 24, "money":money})
                return f"Here is {change} in change.\n here is your {choice} ☕ Enjoy!"

            elif choice == "cappuccino" and int(total_money_entered) >= cappuccino_cost:
                change = total_money_entered - cappuccino_cost
                return f"Here is {change} in change.\n here is your {choice} ☕ Enjoy!"

            elif choice == "espresso" and int(total_money_entered) >= espresso_cost:
                change = total_money_entered - espresso_cost
                return f"Here is {change} in change.\n here is your {choice} ☕ Enjoy!"

            elif int(total_money_entered) < latte_cost or int(total_money_entered) < cappuccino_cost or int(total_money_entered) < espresso_cost:
                return "sorry that's not enough money. Money refunded"






        print(Check_resource_And_process_transaction(total_money_entered))






