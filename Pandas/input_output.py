# Нужни библиотеки за този урок.
# pip install sqlalchemy
# pip install lxml
# pip install html5lib
# pip install BeautifulSoup4
# pip install xlrd

import pandas as pd

# CSV

df = pd.read_csv('example.csv')

print(df)

df.to_csv('My_output.txt', index=False)

print(pd.read_csv('My_output.txt'))

# Excel

df2 = pd.read_excel('Excel_Example.xlsx', sheet_name='Sheet1')

print(df2)

df2.to_excel('Excel_output.xlsx', sheet_name='NewSheet')

# Html

df3 = pd.read_html('https://en.wikipedia.org/wiki/List_of_Mount_Everest_summiters_by_number_of_times_to_the_summit')

# print(type(df3))
print(df3[1])

df4 = pd.read_json('https://graduate.pythonanywhere.com/rest/699644c1-da21-4a8d-85a5-66bb18117c2f')
print('\nFrom json string - ' + df4.data[11]['Nutrient'])

# SQL

from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:')

df2.to_sql('my_table', engine)

sqldf = pd.read_sql('my_table', con=engine)

print(sqldf)
