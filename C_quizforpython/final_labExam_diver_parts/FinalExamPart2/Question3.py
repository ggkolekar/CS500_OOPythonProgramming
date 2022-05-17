from state_machine import (State, Event, acts_as_state_machine,
after, before, InvalidStateTransition)
from typing import Timer, endrun

@acts_as_state_machine
class TestCycle:

    unknown =State(initial= True)
    init = State()
    faulted =State()
    idle = State()
    ready =State()
    assigned =State()
    running=State()
    completed =State()
    aborted =State()

    powerup= Event (from_states = (unknown, init),to_state=idle )
    load = Event(from_states=idle, to_state=ready)
    assign = Event(from_states= ready, to_state=assigned)
    start = Event(from_states= assigned, to_state= running)
    cancel = Event(from_states=running, to_state=aborted)
    exit = Event(from_states=aborted, to_state=exit)

    def __init__(self, name):
        self.name = name

    @after('wait')
    def powerup_info(self):
        print(f'{self.name}  powered up the system')

    @after('run')
    def load_info(self):
        print(f'{self.name} loaded devices into the system

')

    @after('run')
    def assign_info(self):
        print(f'{self.name} assigned a test program')

    @after('run')
    def start_info(self):
        print(f'{self.name} started a test run')

    @after('run')
    def cancel_info(self):
        print(f'{self.name} canceled the test run')

    @before('terminate')
    def exit_info(self):
        print(f'{self.name} exited the program')


def makeTransition(process, event, event_name):
    try:
        event()
    except  InvalidStateTransition as err:
        print(f'Error: transition of {TestCycle.name} from {TestCycle.current_state} to {event_name} failed')




class TestPlan:
    def __init__(self):
        self.cycle = TestCycle('TLB')

def showmenu(self):
        print("COMMAND MENU")
        print(" \n powerup :Power up the system  \n  load : Load devices into the system \n assign  : Assign a test program",
                 " \n start  : Start a test run \n F  : Record final exam score for all ",
                "students \n cancel : Cancel the test run \n exit :  Exit the program ")
        print()





def main(endRun=None):

    POWERUP = 'powerup'
    LOAD ='load'
    ASSIGN ='assign'
    START ='start'
    CANCEL ='cancel'
    EXIT='exit'
    showmenu()
    while True:
        command = input("command: ")
        if command == "start":
            print("Running")
            t= Timer(10,endRun)
            t.start()
        elif command == "cancel":
            t.cancel()
            print("Aborted")
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again. \n")

main()
