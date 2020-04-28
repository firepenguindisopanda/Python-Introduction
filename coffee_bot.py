# Define your functions
def extra_options():
  res = input('Would you like a plastic cup or did you bring your own reusable cup? \n[a] I\'ll need a cup. \n[b] Brought my own! \n> ')

  if res == 'a':
    print('Okay, no problem! We\'ll get you a plastic cup.')
  elif res == 'b':
    print('Great! We\'ll fill up your reusable cup.')
  else:
    print_message()
    return extra_options()
  
def get_drink_type():
  res = input('What type of drink would like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte\n> ')
  if res == 'a':
    return 'brewed coffee'
  if res == 'b':
    return 'mocha'
  if res == 'c':
    latte_type = order_latte()
    
    return latte_type
  else:
    print_message()
    return get_drink_type()
  return res

def print_message():
  print ("I'm sorry, I did not understand your selection. Please enter the corresponding leter for your response.")


def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large\n> ')
  
  if res == 'a':
    return 'small'
  if res == 'b':
    return 'medium'
  if res == 'c':
    return 'large'
  else:
    print_message()
    return get_size()

def order_latte():
  res = input('And what kind of milk for your latte?\n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk\n> ')
  
  if res == 'a':
    return 'latte'
  if res == 'b':
    return 'non-fat latte'
  if res == 'c':
    return 'soy latte'
  else:
    print_message()
    return order_latte()
  return res

  
def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  drink_type = get_drink_type()
  print('Alright, that\'s a {} {}!'.format(size, drink_type))
  extra_options()
  
  costumers_name = input('Can i get your name please?')
  print("Thanks, {}! Your drink will be ready shortly.".format(costumers_name))


  

# Call coffee_bot()!
coffee_bot()
