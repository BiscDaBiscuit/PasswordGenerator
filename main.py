import requests
from random import *
import string
import os
import sys
from time import sleep
from colorama import Fore, Back, Style

class PasswordGen:
  def __init__(self):
    self.main()

  def slowType(self, str):
    for letter in str:
        sys.stdout.write(letter);sys.stdout.flush();sleep(0.05)

  def genpassword(self, length):
      characters = string.ascii_letters + string.digits
      password =  "".join([choice(characters) for i in range(length)])
      return password

  def main(self):

    print(Fore.GREEN)
    print("""
    ██████╗  █████╗ ███████╗███████╗     ██████╗ ███████╗███╗   ██╗
    ██╔══██╗██╔══██╗██╔════╝██╔════╝    ██╔════╝ ██╔════╝████╗  ██║
    ██████╔╝███████║███████╗███████╗    ██║  ███╗█████╗  ██╔██╗ ██║
    ██╔═══╝ ██╔══██║╚════██║╚════██║    ██║   ██║██╔══╝  ██║╚██╗██║
    ██║     ██║  ██║███████║███████║    ╚██████╔╝███████╗██║ ╚████║
    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝
    """)

    sleep(2)
    
    print(Fore.BLUE)
    self.slowType("Made by: Bisc")
    sleep(1)
    self.slowType("\n\nInput how many passwords you would like to generate!\n")

    print(Fore.GREEN)
    num = int(input('Amount of Passwords: '))

    print(Fore.BLUE)
    self.slowType("How long would you like your passwords to be?? (Recommendation: 17)\n")
    print(Fore.GREEN)
    plen = int(input("Length of Passwords: "))
    print(Fore.RED)
    for i in range(num):
      print(self.genpassword(plen))

if __name__ == '__main__':
  PasswordGen()
  
