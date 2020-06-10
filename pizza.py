def make_pizza(size,*toppings):
    print('\nmaking '+str(size)+
            'inch pizzza')
    for topping in toppings:
        print('- '+topping)