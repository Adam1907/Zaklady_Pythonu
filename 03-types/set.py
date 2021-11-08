'''
 Set je množina jedinečných hodnot
 A set is a collection which is unordered and unindexed.
 In Python sets are written with curly brackets.
'''
my_set = {2, 3, 9, 7}
print('Množina my_set: ', my_set)
print('Typ my_set: ', type(my_set))

# Vytvoření množiny ze seznamu hodnot (list)
numbers = [1, 4, 1, 5, 3, 3, 1, 2, 8, 2]
print(f'Proměnná numbers - seznam (list): {numbers}')
set_numbers = set(numbers)
print(f'Proměnná set_numbers - množina (set): {set_numbers}')

# Vytvoření množiny jedinečných znaků z řetězce
chars = sorted(list('Hello world'))
set_chars = set(chars)
print(f'Uspořádaná množina (set) jedinečných hodnot: {set_chars}')

#Po vytvoření setu nelze měnit jeho obsah ale můžeme k němu přidávat
#K přidání nového předmětu do setu použijeme metodu add()
set_chars.add('V')

#K přidání více nových předmětů do setu použijeme metodu update()
set_chars.update('X', 'Y', 'Z')

#K odstranění předmětu ze setu pužijeme metodu remove() nebo discard()
set_chars.remove('H')
print(f'Proměnná set_chars: {set_chars}')

#Metoda clear() vyčistí celý set
set_chars.clear()

#Klíčové slovo del vymaže set kompletně
del set_chars

# Přístup k hodnotám množiny
#Nemůžeme přistoupit k předmětům v setu tím že odkážeme na index, protože sety jsou neseřazené a předměty nemají index
# my_set[1]

# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
#Můžeme ale procházet setem pomocí for loop, nebo se můžeme zeptat zda je specifická hodnota v setu pomocí klíčového slova in
for x in my_set:
  print(x)

'''
Množinové operace
'''
# Sjednocení množin
print(f'set_numbers | my_set: {set_numbers | my_set}')
print(f'set_numbers.union(my_set): {set_numbers.union(my_set)}')
# Průnik množin
print(f'set_numbers & my_set: {set_numbers & my_set}')
print(f'set_numbers.intersection(my_set): {set_numbers.intersection(my_set)}')
# Rozdíl množin
print(f'set_numbers - my_set: {set_numbers - my_set}')
print(f'set_numbers.difference(my_set): {set_numbers.difference(my_set)}')
# Doplněk množin
print(f'set_numbers ^ my_set: {set_numbers ^ my_set}')
print(f'set_numbers.symmetric_difference(my_set): {set_numbers.symmetric_difference(my_set)}')
# Zjištění zda množina obsahuje hodnotu
print(f'1 in set_numbers: {1 in set_numbers}')
