# -*- coding: utf-8 -*-
import re
import pickle

from colorama import init
from termcolor import colored

init() # Termcolor support for win32

#
# Color Message Printing for Terminal
#

def printGreen(msg):
    print(colored(msg, 'green'))

def printYellow(msg):
    print(colored(msg, 'yellow'))

def printMagenta(msg):
    print(colored(msg, 'magenta'))

def printRed(msg):
    print(colored(msg, 'red'))


#
# Display Terminal Messages / Prompts
#

help_message = '''
  🛍️ Machine Learning eCommerce Recommender System

  Usage
    $ retailbox [<options> ...]

  Options
    --help, -h                Display help message
    --search, -s              Search customer by ID [Can be any integer 0-4338]
    --customer, -c <int>      Input customer ID [Can be any integer 0-4338]
    --info, -i                Display customer information
    --status, -s              Display process info
    --list, -l                List available customer IDs
    --version, -v             Display installed version

  Examples
    $ retailbox --help
    $ retailbox --search
    $ retailbox --customer 1028
    $ retailbox -c 1028
    $ retailbox -m 1028 --info
    $ retailbox -m 1028 -i --status
'''

def displayHelpMessage():
    print(help_message)

def displayVersion(version):
    print('RetailBox ' + version)


'''
Display Customer Information:

customer_id     (int)
items_purchases (list)
country         (string) 
amount_spent    (float) 

'''
def display_customer_information(customer_id, country, items, amount_spent):
    # Print Customer ID
    print('\n')
    # customer_id_short
    
    # Load Customer table for display
    table_file = open('../data/final/df_customer_table_long.pkl', "rb")
    customer_table = pickle.load(table_file)
    customer_id_display = customer_table[customer_id]
    table_file.close()
    
    print(colored('❯ Customer_ID: ' + str(customer_id_display), 'green'))

    # Print Customer's Country of Origin
    print(colored('• Country: ' + country, 'green'))

    # Print Items the Customer Purchased
    print(colored('• Items Purchased:', 'green'))
    counter = 0
    for i in items:
        i = i.lower()
        if counter < 5:
            print(colored('  - ' + i.title(), 'green'))
            counter += 1
        else:
            print(colored('  and ' + str(len(items) - 5) + ' other items..', 'green'))
            break
    
    # Print Total Amount Spent and Number of Items Purchased
    print(colored('• Number of Items: ' + str(len(items)), 'green'))
    print(colored('• Amount Spent: ' + '{:0.2f}'.format(amount_spent), 'green'))

    return 0

def display_recommender_items(recommended_items):
    print('\n')
    print(colored('❯ Recommended Items:', 'yellow'))
    for i in recommended_items:
        print(colored('  - ' + i, 'yellow'))
    print('\n')
