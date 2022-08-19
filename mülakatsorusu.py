# Uygulama - Mülakat Sorusu

# Amaç: Çift sayıların karesi alınarak bir sözlüğe eklenmek istemektedir.
# Key'ler orjınal değerler value'ler ise değiştirilmiş değerler olacak.

numbers = range(10)
print(range(10))
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2
#   print(new_dict)

print({n: n ** 2 for n in numbers if n % 2 == 0})
