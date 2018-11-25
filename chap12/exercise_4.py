from atmmanager import ATMApp, User
from textatm import TextInterface

def main():
    interface = TextInterface()
    app = ATMApp("new_atmusers.json", interface) 
main()
 