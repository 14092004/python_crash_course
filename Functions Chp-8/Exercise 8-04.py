# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python
def make_shirt(size='large', message='I love Python!'):
      print("\nI'm going to make a " + size + " t-shirt.")
      print('It will say, "' + message + '"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Programmers are loopy.')