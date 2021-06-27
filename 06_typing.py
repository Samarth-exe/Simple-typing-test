import time
import random
lst = ['Brownie is too brown to be brown so he is brown', 'Over the trees the wind blew and made the tree fall down', 'The tree fell because of the wind rip tree', 'You should type faster now to win or you lose', 'This sentence is complicated to type because it is too long', 'I play with plastic toy cars just a joke']
randomizer = random.choice(lst)

print('You will be given 7 seconds to write the sentence')
time.sleep(5)
print('You have 10 seconds to read the sentence')
time.sleep(4)
print('\n')
print('The sentence is: ')
print(randomizer)
print('\n')

time.sleep(6)
print('Starting in 4 seconds')
time.sleep(4)

test = input('Write the sentence: ')
time.sleep(7)
if test==randomizer:
    print('You passed the typing test')
elif test != randomizer:
    print("You didn't pass the test")