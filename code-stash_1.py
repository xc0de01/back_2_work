# project1-temperature-converter


temp_var = {'Celsius':'*C','Kelvin':'*K', 'Fahrenheit': '*F'}
key_list = []
for key in temp_var:
    key_list.append(key)
temp_unit = input("Enter the temperature unit measure:").title()
while True:
    if temp_unit not in temp_var:
        print('measure unknown')
        temp_unit = input(" Enter the temperature unit measure:").title()
    else:
        print('okay')
        break

t_value = eval(input("Enter the temperature value:"))
print(f"Final parameter: {t_value}{temp_var[temp_unit]}")



