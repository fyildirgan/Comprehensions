# İsminde "INS" olan değişkenlerin başına Flag diğerlierine No_Flag eklemek istiyoruz.
# before:
#['TOTAL',
# 'SPEEDİNG',
# 'ALCOHOL',
# 'NOT_DİSTRACTED',
# 'NO_PREVİOUS',
# 'INS_PREMİUM',
# 'INS_LOSSES',
# 'ABBREV']

# after:
# ['NO_FLAG_TOTAL',
# 'NO_FLAG_SPEEDİNG',
# 'NO_FLAG_ALCOHOL',
# 'NO_FLAG_NOT_DİSTRACTED',
# 'NO_FLAG_NO_PREVİOUS',
# 'NO_FLAG_INS_PREMİUM',
# 'NO_FLAG_INS_LOSSES',
# 'NO_FLAG_ABBREV']

import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns
for col in df.columns:
    print(col.upper())

A = []
for col in df.columns:
    A.append(col.upper())
    print(A)

df = sns.load_dataset("car_crashes")
df.columns = [col.upper() for col in df.columns]

print([col for col in df.columns if "INS" in col])
print(["FLAG_"+ col for col in df.columns if "INS" in col])
print(["FLAG_"+ col if "INS" in col else "NO_FLAG_" + col for col in df.columns ])
df.columns = ["FLAG_"+ col if "INS" in col else "NO_FLAG_" + col for col in df.columns ]
pring(df.columns)