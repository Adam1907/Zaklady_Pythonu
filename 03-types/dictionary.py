'''
Slovníky (dictionaries) podobně jako seznamy v sobě obsahují další hodnoty.
Na rozdíl od seznamů, ve kterých jsou všechny prvky uspořádané do jedné sekvence, ve slovnících máme dva druhy prvků:
klíč (angl. key) a hodnotu (angl. value).
Každému klíči je přiřazena jedna hodnota.
'''

# Kolekce které jsou neseřazeny, pozměnitelné a indexované.
# V Pythonu jsou dictionaries  psány složenými zavorkami, mají klíče a hodnoty.
car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}

point = {'x': 1, 'y': 10}

# Vytvoření slovníku pomocí konstruktoru dict()
point = dict(x=1, y=10)

# Změna hodnoty jednoho prvku slovníku
point['x'] = 2

# Vložení nového prvku do slovníku
point['z'] = 20

# Přístup k položkám slovníku
print(f'point["x"]: {point["x"]}')
print(f'point.get("x"): {point.get("x")}')

# Zjištění, zda existuje hodnota
if 'z' in point:
    print(f'point.get("z"): {point.get("z")}')

# Když hodnota neexistuje, vrací 0    
print(f'point.get("v", 0): {point.get("v", 0)}')

# Odstranění prvku ze slovníku  
del point['x']
print(f'point: {point}')

print(f'car.pop(): {car.pop("model")}')

# Odstraní poslední prvek ze slovníku
print(f'car.popitem(): {car.popitem()}')

# Procházení slovníkem - vypíše vždy pár klíč - hodnota
for key, value in point.items():
    print(f'{key} - {value}')

# Dictionary comprehension - zkráceně vytvoří slovník, jehož klíče tvoří čísla od 0 do 9 a hodnoty druhé mocniny 
values = {x: x ** 2 for x in range(10)}
print(f'values: {values}')

# Unpacking operator - pro slovníky se používají **
first = {'x': 1, 'y': 2}
second = {'x': 10, 'z': 5}
common = {**first, 'a': 15, **second}
print(f'common: {common}')

# Nested dictionary - vnořené slovníky
myfamily = {
  'child1' : {
    'name' : 'Emil',
    'year' : 2004
  },
  'child2' : {
    'name' : 'Tobias',
    'year' : 2007
  },
  'child3' : {
    'name' : 'Linus',
    'year' : 2011
  }
}
print(f'Nested dictionary myfamily: {myfamily}')

# ??? 4. cvičení ???
# a) Navrhněte vlastní vnořený slovník tvořený 3 reálnými objekty s aspoň 6 klíči tak, abyste kromě jednoduchých
# datových typů (čísla, řetězce, boolean) ve slovníku vhodně využili i všechny v tomto bloku probrané strukturované
# typy - tedy set, tuple a list.
# Volte příklad vycházející z reality - např. slovník aut, slovník filmů, slovník historických postav atd.
# b) Pomocí vhodných metod přidejte do slovníku nový prvek a nějaký starý naopak odstraňte
# c) Proveďte výpis obsahu slovníku tak, aby i v konzoli vytvořil hezky naformátovanou tabulku i s mezerami
# viz níže uvedený vzor.
'''
Slovník myfamily
---------------------------------------------
child           name                year
---------------------------------------------
child1          Emil                2004
child2          Tobias              2007
child3          Linus               2011
---------------------------------------------
Počet záznamů: 3
'''
films = {
  'film1' : {
    'name' : 'Star Wars A New Hope',
    'director' : 'George Lucas',
    'year' : 1977,
    'soundtrack' : ('Main Title','Imperial Attack','The Land of the Sand People'),
    'awards' : {'Oscar', 'Golden Globe'},
    'actors' : ['Mark Hamill', 'Carrie Fisher', 'Harrison Ford'],
    'sequel' : True
   },
  'film2' : {
      'name' : 'Gladiator',
      'director' : 'Ridley Scott',
      'year' : 2000,
      'soundtrack' : ('Progeny-Hans Zimmer','The Battle-Hans Zimmer','Am I Not Merciful-Hans Zimmer'),
      'awards' : {'Oscar', 'Golden Globe', 'BFCA'},
      'actors' : ['Russell Crowe', 'Joaquin Phoenix', 'Connie Nielsen'],
      'sequel' : False
   },
  'film3' : {
      'name' : 'Dune',
      'director' : 'Denis Villeneuve',
      'year' : 2021,
      'soundtrack' : ('Prologue','Trip To Arrakis','Final Dream'),
      'awards' : {"-"},
      'actors' : ['Timothée Chalamet', 'Rebecca Ferguson', 'Oscar Isaac'],
      'sequel' : False
   }
}

print("Původní:",films)

print(f'films.popitem(): {films.popitem()}')



films["film3"] = {'name': 'Example', 'director': 'Example', 'year': 2020, 'soundtrack': ('Example', 'Example', 'Example'), 'awards': {'Example', 'Example'}, 'actors': ['Example', 'Example', 'Example'], 'sequel': True}

print("Změna:", films)