# COMPREHENSİONS

# List Comprehensions: Birden fazla satır ve kod ile yapılabilecek işlemleri kolayca istediğiniz çıktı veri yapısına göre
# tek bir satırda gerçekleştirme imkanı sağlayan yapılardır.
from typing import List, Any

salaries = [1000, 2000, 3000, 4000, 5000]


def new_salary(x):
#    print(x * 20 / 100 + x)
    return x * 20 / 100 + x
    

null_list = []

for salary in salaries:
    null_list.append(new_salary(salary))
#    print(null_list)

null_list = []

for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary * 2))
#    print(null_list)

print([new_salary(salary *2) if salary < 3000 else new_salary(salary) for salary in salaries])

print([salary * 2 for salary in salaries])

print([salary * 2 for salary in salaries if salary < 3000])
# Eğer tek başına IF kullanıyorsak sağ tarafta yer alır, eğer IF ve ELSE birlikte kullanılıyorsak bu durumda for yapısı
# sağ tarafta yer alır.

print([salary * 2 if salary < 3000 else salary * 0 for salary in salaries])

print([new_salary(salary * 2) if salary < 3000 else new_salary(salary * 0.2) for salary in salaries])

students = ["John", "Mark", "Venessa", "Mariam"]

students_no = ["John", "Venessa"]

print([student.lower() if student in students_no else student.upper() for student in students])
# Yukarıda bulunan formülün anlaşılır şekilde açıklanışı;
# for student in student: öğrencilerde gez
# if student in students_no: yakaladığım her öğrenci "students"dan mı yoksa "students_no"dan mı eğer buradaysa buradaki isimleri
# küçült diyoruz(stundent.lower()) eğer burada yoksa else büyüt diyoruz(student.upper())

print([student.upper() if student not in students_no else student.lower() for student in students])





