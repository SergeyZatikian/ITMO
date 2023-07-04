import pandas

excel = pandas.read_excel('vegetable.xlsx', sheet_name='summer')

print(excel)