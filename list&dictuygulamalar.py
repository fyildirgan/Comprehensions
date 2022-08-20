# List & Dict Comprehension Uygulamalar

# Bir veri setindeki değişken İsimlerini Değiştirmek
# before:
# ['total', 'speeding','alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']
#after:
# ['TOTAL', 'SPEEDİNG', 'ALCOHOL', 'NOT DİSTRACTED', 'NO_PREVİOUS', 'INS_PREMİUM', 'INS_LOSSES', 'ABBREV']

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns
print(df)
for col in df.columns:
    print(col.upper())

A =[]

for col in df.columns:
    A.append(col.upper())
    print(A)

df.columns = A
print(A)

df = sns.load_dataset("car_crashes")
df.columns = [col.upper() for col in df.columns]



