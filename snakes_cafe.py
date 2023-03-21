
my_current_order = {}

snakes_menu = {
    "Wings": 0,
    "Cookies": 0,
    "Spring Rolls": 0,
    "Salmon": 0,
    "Steak": 0,
    "Meat Tornado": 0,
    "A Literal Garden": 0,
    "Ice Cream": 0,
    "Cake": 0,
    "Pie": 0,
    "Coffee": 0,
    "Tea": 0,
    "Unicorn Tears": 0,
}

def welcome():
    print('''
    *************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************''')


def menu():
    print('''
    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls

    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden

    Desserts
    --------
    Ice Cream
    Cake
    Pie

    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears''')

def order_invitation():
    print('''
    ***********************************
    ** What would you like to order? **
    ***********************************''')
    users_order = input("> ")
    if users_order not in snakes_menu:
        print(f'''
        Your {users_order} is not on the menu, but we can make an exception.''')
    else:
        print(f'''
    1 order of {users_order} has been added to your meal''')
    if users_order in my_current_order:
        my_current_order[users_order] = + 1
    else:
        my_current_order[users_order] = 1

    ask_again = True

    while ask_again:
        print('''
        What else can I prepare for you today?
        Type quit to quit at any time.''')

        users_order = input("> ")
        if users_order == "quit":
            break
        if users_order not in snakes_menu:
            print(f'''
            Your {users_order} is not on the menu, but we can make an exception.''')
        if users_order in my_current_order:
            my_current_order[users_order] += 1
            print(f'''
            You have added {my_current_order[users_order]} orders to your meal of {users_order}.''')
        else:
            my_current_order[users_order] = 1
            print (f'''
            You have added {users_order} to your meal.''')

        print(f'''
        Your meal consists of : {my_current_order}''')

welcome()
menu()
order_invitation()



