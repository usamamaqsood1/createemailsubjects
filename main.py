import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

excel_file = "test.xlsx"

# Load the Excel file into a DataFrame
df = pd.read_excel(excel_file)

df = df.dropna(subset=['Email address'], axis=0)

# If you want to reset the index after dropping rows


for x in range(339, 459):
    email = df['Email address'].iloc[x]

    at_index = email.index("@")
    dot_index = email.index(".")
    inside_value = email[at_index + 1:dot_index]
    inside_value = inside_value.capitalize()
    inside_value = inside_value.capitalize()
    # print(str(x) + email)
    # print(inside_value)
    title = "my girlfriend and your affiliates at " + inside_value
    company_name = inside_value
    print(email)
    print(title)
    print(x)






    # Print or use the formatted email
