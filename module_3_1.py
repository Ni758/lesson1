
from random import randint

calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()

def is_contains(string, list_to_search):
    count_calls()

for _ in range(randint(5,10)):
    random_var = randint(0,1)
    if random_var:
        string_info('Capybara')
    else:
        is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])

print(calls)
