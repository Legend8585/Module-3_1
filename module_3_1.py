#1.Создать переменную calls = 0 вне функций.
calls = 0
#2. Создать функцию count_calls и изменять в ней значение переменной calls.
#Эта функция должна вызываться в остальных двух функциях.
def count_calls():
    global calls
    calls += 1
#3
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())
#4
def is_contains(string, list_to_search):
    count_calls()
    lower_string = string.lower()
    lower_list = [item.lower() for item in list_to_search]
    return lower_string in lower_list
#5,6
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)