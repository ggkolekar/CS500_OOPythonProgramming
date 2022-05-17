from state_machine import (State, Event, acts_as_state_machine,
after, before, InvalidStateTransition)
import random

@acts_as_state_machine
class CheckoutProcess:
    #define 4 states
    checkout = State(initial=True)
    payment= State()
    pending = State()
    confirmed = State()
    canceled = State()

    #define transitions
    enterPaymentInfo= Event(from_states = checkout, to_state = payment)
    submit = Event(from_states = payment, to_state=pending)
    approved = Event(from_states = pending, to_state=confirmed)
    disapproved = Event(from_states =pending, to_state=checkout)
    cancel=Event(from_states =confirmed, to_state =canceled)

    def __init__(self,name):
        self.name = name

    def makeTransition(self, event, event_name):
        try:
            event()
        except InvalidStateTransition as err:
            print(f'Error: transition of (self.name) from{self.current_state}to{event_name}failed')

    def begincheckout(self):
        self.makeTransition(self.enterPaymentInfo, "Payment")

    @before('enterPaymentInfo')
    def enterPaymentInfo_info(self):
        print('Please enter your payment information.')
    @after('submit')
    def submitOrder(self):
        self.makeTransition(self.submit, "Pending")

    @after('checkout')
    def ckeckout_info(self):
        print(f'{self.name} checking out.')

    @after('payment')
    def payment_info(self):
        print(f'{self.name} is payment.')

    @before('pending')
    def pending_info(self):
        print(f'{self.name} order is pending.')

    @before('confirmed')
    def confirmed_info(self):
        print(f'{self.name} order is confirmed.')

    @before('canceled')
    def canceled_info(self):
        print(f'{self.name} order is canceled.')

    def VerifyOrder(self):
        approved = random.randint(0, 9) > 3
        if approved == True:
            self.maketransition(self.confirmed, "confirmed")
        else:
            self.maketransition(self.checkout, "Checkout")

    @after("approved")
    def enterpaymentInfo(self):
        print("Your order has been approved")

    @after("approved")
    def enterpaymentInfo(self):
        print("Your order was not approved")

class OrderSystem:
    def __init__(self):
        self.process= CheckoutProcess('Alex')

    def begincheckout(self):
        try:
            self.process.beginCheckout()
        except InvalidStateTransition as err:
            print(f'Error:{self.process.name}cannot begin checkout')



    def showMenu(self):
        print("COMMAND MENU")
        print("begin: Submit your order")
        print("cancel: Cancel my order")
        print("return: Back to checkout")
        print("exit: Exit program")
        print()

def main():
    mall = OrderSystem()
    mall.showMenu()

    while True:
        command = input("Command: ")
        if command == "begin":
            mall.beginCheckout()
        elif command =="submit":
            mall.gotOrder()
        elif command == "cancel":
            mall.cancelOrder()
        elif command == "return":
            mall.back()
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again. \n")

if __name__ == "__main__":
    main()