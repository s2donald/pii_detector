# %%
import pandas as pd

# %%
df = pd.read_csv("generated_data.csv")
df
# %%
splitted = df['Full Name'].str.split()
df['firstname'] = splitted.str[0]
df['lastname'] = splitted.str[-1]
df['middlename'] = splitted.str[1]
df['middlename'] = df['middlename'].mask(df['middlename'] == df['lastname'], '')
# %%
df

# %%
df["Phone Number"] = df["Phone Number"].str.replace(r'\D',"")
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
    return luhn_checksum(card_number) == 0

def generate_fake_sin():
    while True:
        first_digit = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        remaining_digits = random.sample(range(10), 8)
        fake_sin = f"{first_digit}{''.join(map(str, remaining_digits))}"
        if is_luhn_valid(fake_sin):
            break
        print(fake_sin)
    return fake_sin

# Generate 1300 valid fake SINs
fake_sins = set()
while len(fake_sins) < 1300:
    fake_sins.add(generate_fake_sin())

# Create a DataFrame with these fake SINs
df["Valid Fake SIN"] = list(fake_sins)
df["Valid Fake SIN"] = df["Valid Fake SIN"].astype(str)

# %%
df.to_csv('generated_data_1.csv', index=False)



# %%
df = pd.read_csv("generated_data_1.csv", nrows=1) # Just take the first row to extract the columns' names
col_str_dic = {column:str for column in list(df)}
# %%
df = pd.read_csv("generated_data_1.csv", dtype=col_str_dic)
# %%
df
# %%
from faker import Faker
fake = Faker("en_CA")

# %%
# Generate 1300 valid fake SINs
fake_address = set()
while len(fake_address) < 1300:
    fake_address.add(fake.address())

# Create a DataFrame with these fake SINs
df["Address"] = list(fake_address)
df["Address"] = df["Address"].astype(str)

# %%
df

# %%
df["Address"] = df["Address"].replace(r'\n',' ', regex=True)

# %%
df.to_csv('generated_data_3.csv', index=False)

# %%
splitted = df['Address'].str.split(',')
df['Address_short'] = splitted.str[0]
df['prov_postal'] = splitted.str[1]

# %%
df
# %%
splitted = df['prov_postal'].str.split()

# %%
splitted
# %%
df['province_code'] = splitted.str[0]

# %%
splitted.str[1:]
# %%
postal_cd = splitted.str[1:].apply(lambda x: " ".join(x))

# %%
df["postal_code"] = postal_cd
# %%
df
# %%
df.to_csv('generated_data_4.csv', index=False)
# %%
def get_list_of_email():
    return [fake.email() for _ in range(1300)]
# %%
fake_email = get_list_of_email()
fake_email

# %%
import random
domains = ['gmail', 'yahoo', 'hotmail', 'aviva', 'example', 'domain', 'outlook', 'test']
# %%
random.choice(domains)
fake_emails = []
# %%
for i in fake_email:
    dom = random.choice(domains)
    x = i.replace('example', dom)
    fake_emails.append(x)

fake_emails
# %%
df['email'] = fake_emails
df
# %%
df.to_csv('generated_data_5.csv', index=False)
# %%
def generate_fake_policy_claim_id(type: str):
    first_digit = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
    remaining_digits = random.sample(range(10), 4)
    fake_type = f"{type}{first_digit}{''.join(map(str, remaining_digits))}"
    print(fake_type)
    return fake_type

# %%
fake_claims = set()
while len(fake_claims) < 1300:
    fake_claims.add(generate_fake_policy_claim_id("CLM"))

# %%
fake_policy = set()
while len(fake_policy) < 1300:
    fake_policy.add(generate_fake_policy_claim_id("PLA"))
# %%
df["claim_id"] = list(fake_claims)
df["policy_id"] = list(fake_policy)

# %%
df
# %%
df.to_csv('generated_data_6.csv', index=False)
# %%
import random
import time
    
def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y', prop)


print(random_date("1/1/1956", "1/1/2017", random.random()))

# %%
fake_dob = set()
while len(fake_dob) < 1300:
    fake_dob.add(random_date("1/1/1956", "1/1/2017", random.random()))

fake_dob
# %%
df["dob"] = list(fake_dob)
# %%
df.to_csv('generated_data_7.csv', index=False)
# %%

import random
LETTERS = "ABCDEFGHJKLMNPRSTUVWXYZ"
NUMBERS = "1234567890"

def generate_random_char(charset):
    idx = random.randint(0, len(charset) - 1)
    return charset[idx]
def generate_vin():
    vin = ""
    # First 3 characters of the VIN
    for i in range(3):
        vin += generate_random_char(LETTERS)
    # Characters 4-8 of the VIN
    for i in range(3, 8):
        vin += generate_random_char(NUMBERS)
    # Characters 9-17 of the VIN
    for i in range(8, 17):
        vin += generate_random_char(LETTERS)
    return vin


# %%
fake_vin = set()
while len(fake_vin) < 1300:
    fake_vin.add(generate_vin())

fake_vin
# %%
df["vin"] = list(fake_vin)
# %%
df.to_csv('generated_data_8.csv', index=False)
# %%
df
# %%
df["phonenumber_w_code"] = '+1' + df["Phone Number"].astype(str)

# %%
test = '(' + df["Phone Number"].str[:3]+')'+df["Phone Number"].str[3:6] + '-' + df["Phone Number"].str[6:]
df["phonenumber_brk"] = test
# %%
test = '+1(' + df["Phone Number"].str[:3]+')'+df["Phone Number"].str[3:6] + '-' + df["Phone Number"].str[6:]
df["phonenumber_brk_cd"] = test

# %%
test = '+1(' + df["Phone Number"].str[:3]+')'+df["Phone Number"].str[3:]
df["phonenumber_brk_cd_dsh"] = test
# %%
df
# %%
test = '+1' + df["Phone Number"].str[:3]+'-'+df["Phone Number"].str[3:6] + '-' + df["Phone Number"].str[6:]
df["phonenumber_brk_cd_dsh_no_brk"] = test
# %%
test = '' + df["Phone Number"].str[:3]+'-'+df["Phone Number"].str[3:6] + '-' + df["Phone Number"].str[6:]
df["phonenumber_dsh_no_brk"] = test
# %%
df
# %%
df.to_csv('generated_data_9.csv', index=False)
# %%
splitted = df['Address_short'].str.split()

# %%
splitted

# %%
splitted.str[:3]
# %%
add_short = splitted.str[:3].apply(lambda x: " ".join(x))
# %%
df
# %%
df['address_shrt'] = add_short
# %%
df
# %%
df.columns
# %%
df["dob"]
# %%
dob_formated = df["dob"].str.replace(r'/', '')
# %%
dob_formated
# %%
df["dob_formatted"] = dob_formated
# %%
dob_formated_und = df["dob"].str.replace(r'/', '-')
# %%
dob_formated_und
# %%
df["dob_formated_und"] = dob_formated_und
# %%
df
# %%
df.to_csv('final_data.csv', index=False)
# %%
