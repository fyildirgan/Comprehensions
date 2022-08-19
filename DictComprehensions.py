# Dict Comprehension: Listelere benzer şekilde tek bir satırda görece karmaşık olarak kabul edilebilecek ve birden
# fazla satırda ifade edilmesi gerekebilecek olan işlemleri ifade etme imkanı sunar.
dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
print({k: v ** 2 for (k, v) in dictionary.items()})
print({k.upper(): v for (k, v) in dictionary.items()})
print({k.upper(): v * 2 for (k, v) in dictionary.items()})