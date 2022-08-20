# Amaç key'i string, value'su aşağıdaki gibi bir liste olan sözlük oluşturmak.
# Sadece sayılar değişkenler için yapmak istiyoruz.


# Output:
# {'total': ['mean', 'min', "max", 'var'],
# 'speeding': ['mean', 'min', "max", 'var'],
# 'alcohol': ['mean', 'min', "max", 'var'],
# 'not_distacted': ['mean', 'min', "max", 'var'],
# 'no_previous': ['mean', 'min', "max", 'var'],
# 'ins_premium': ['mean', 'min', "max", 'var'],
# 'ins_losses': ['mean', 'min', "max", 'var']}

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns
#print(df.columns)
num_cols = [col for col in df.columns if df[col].dtype != "0"]
#print(num_cols)
soz = {}
agg_list = ["mean", "min", "max", "var"]
#print(agg_list)
for col in num_cols:
    soz[col] = agg_list
#print(soz)
# kısa yol
new_dict = {col: agg_list for col in num_cols}
#print(new_dict)
#print(df[num_cols].head())
print(df[num_cols].agg(new_dict))






