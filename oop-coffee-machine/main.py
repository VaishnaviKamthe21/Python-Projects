from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
maker=CoffeeMaker()
machine=MoneyMachine()

while True:
    order=input("What would you like? "+menu.get_items()).lower()
    if order=='off':
        break
    item=menu.find_drink(order)
    if order=='report':
        maker.report()
        machine.report()
    elif maker.is_resource_sufficient(item):
        if machine.make_payment(item.cost):
            maker.make_coffee(item)
        



        

