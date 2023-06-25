#Think of something you could store in a list.Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once

states = ['Delhi','Rajasthan','Maharashtra','Bangalore']
states.append('Odisha')
print(states)
states.insert(2 , 'Goa')
print(states)
print(len(states))
states.pop()
print(states)
del(states[1])
print(states)
states.remove('Maharashtra')
print(states)
states.sort()
print(states)
states.sort(reverse=True)
print(states)
print(len(states))
