# %%
import pandas as pd

# %%
df = pd.read_csv("final_data.csv")

# %%
df.columns
# %%
df_final = pd.DataFrame()

# %%
flat_names = []
def append_names(column_name):
    for x in df[column_name]:
        flat_names.append(x)

append_names("Full Name")
append_names("firstname")
append_names("lastname")
append_names("middlename")

flat_names
# %%
flat_phone = []
def append_names(flat, column_name):
    for x in df[column_name]:
        flat.append(x)

append_names(flat_phone, "Phone Number")
append_names(flat_phone, "phonenumber_w_code")
append_names(flat_phone, "phonenumber_brk")
append_names(flat_phone, "phonenumber_brk_cd")
append_names(flat_phone, "phonenumber_brk_cd_dsh")
append_names(flat_phone, "phonenumber_brk_cd_dsh_no_brk")
append_names(flat_phone, "phonenumber_dsh_no_brk")

# %%
df.columns

# %%
flat_sin = []
append_names(flat_sin, "Valid Fake SIN")
len(flat_sin)

# %%
flat_add = []
append_names(flat_add, "Address")
append_names(flat_add, "Address_short")
append_names(flat_add, "address_shrt")
len(flat_add)

# %%
flat_prov = []
append_names(flat_prov, "prov_postal")
append_names(flat_prov, "province_code")
len(flat_prov)

# %%
flat_postal = []
append_names(flat_postal, "prov_postal")
append_names(flat_postal, "postal_code")
len(flat_postal)

# %%
flat_email = []
append_names(flat_email, "email")
len(flat_email)

# %%
flat_id = []
append_names(flat_id, "claim_id")
append_names(flat_id, "policy_id")
len(flat_id)

# %%
flat_vin = []
append_names(flat_vin, "vin")
len(flat_vin)

# %%
flat_dob = []
append_names(flat_dob, "dob")
append_names(flat_dob, "dob_formatted")
append_names(flat_dob, "dob_formated_und")
len(flat_dob)

# %%
flat_sin = []
append_names(flat_sin, "Valid Fake SIN")
len(flat_sin)

# %%
from random_word import RandomWords
r = RandomWords()

# %%
flat_word = set()
while len(flat_word) < 60000:
    flat_word.add(r.get_random_word())

flat_wrd = list(flat_word)
len(flat_word)

# %%
category_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
data = list(
        zip(
            (flat_names, flat_phone, flat_sin, flat_add, flat_prov, flat_postal, flat_email, flat_id, flat_vin, flat_dob, flat_wrd),
            category_list
            )
        )
# %%
data
# %%
df_finalss = pd.DataFrame(data, columns=['features_1', 'Category'])
df_finalss = df_finalss.explode('features_1')
# %%
df_finalss
# %%
df_finalss.to_csv('final_labelled_data_100k.csv', index=False)
# %%
