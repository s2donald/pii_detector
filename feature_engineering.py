# %%
import pandas as pd

# %%
df = pd.read_csv("final_labelled_data_100k.csv")
# %%
col_str_dic = {column:str for column in list(df)}
df = pd.read_csv("final_labelled_data_100k.csv", dtype=col_str_dic)
# %%
df_final = pd.DataFrame()
df_final["category"] = df.Category
# %%
df_final["countLength"] = df["features_1"].str.len()
# %%
df_final["countLength"]
# %%
df_final["countUpper"] = df["features_1"].str.findall(r'[A-Z]').str.len()
# %%
df_final["countUpper"]
# %%
df_final["countLower"] = df["features_1"].str.findall(r'[a-z]').str.len()

# %%
df_final["countNumerical"] = df["features_1"].str.findall(r'\d').str.len()

# %%
df_final
# %%
df_final["countSpace"] = df["features_1"].str.findall(r' ').str.len()

# %%
df_final["countDashBrackPlus"] = df["features_1"].str.findall(r'-|\(|\)|\+|\+1').str.len()
# %%
df_final["countDashSlash"] = df["features_1"].str.findall(r'[-/]').str.len()
# %%
df_final["countVowels"] = df["features_1"].str.findall(r'[aeiouAEIOU]').str.len()

# %%
df_final["countConsonants"] = df["features_1"].str.findall(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]').str.len()

# %%
import pandas as pd
import random

def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def is_luhn_valid(card_number):
    try:
        if luhn_checksum(card_number) == 0:
            return 1
        else:
            return 0
    except:
        return 0
# %%
df_final["isLuhn"] = df["features_1"].apply(is_luhn_valid)
# %%
df_final["countCountry"] = df["features_1"].str.findall(r'^(?:\+1|1)').str.len()
# %%
df_final
# %%
df_final["countEmail"] = df["features_1"].str.findall(r'[@\.]').str.len()

# %%
df_final
# %%
df_final.to_csv("final_training_data.csv", index=False)
# %%
df_final = df_final[df_final['countLength'].notna()]
# %%
df_final
# %%
df_final.to_csv("final_training.csv", index=False)
# %%
def is_pii(value):
    if value=="11":
        return 0
    else:
        return 1
    
df_final["is_pii"] = df_final["category"].apply(is_pii)

# %%
df_final
# %%
df_final.to_csv("final_training_w_pii.csv", index=False)
