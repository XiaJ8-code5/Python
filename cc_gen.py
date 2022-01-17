import os
os.system('cls' if os.name == 'nt' else 'clear')  # or use os.system('cls||clear')

print('-' * 30)
print('''| FOR TESTING ONLY !!
| Std curve generator
| Ver. Jan 2022, by: Yi''')

print('-' * 30)
qt = str.upper(input('''| Press Enter to continue, Enter Q to quit.: '''))
if qt == 'Q':
    quit()

print('-' * 30)
Number_of_cc = int(input('| How many points: '))
lloq = float(input('| LLOQ: '))

print('-' * 30)
unit_choice = int(input('''| Concentration unit:
|  [1] pg/ml
|  [2] ng/ml
|  [3] ug/ml
|  [4] mg/ml
| Enter unit choice: '''))

if unit_choice == 1:
    unit = 'pg/ml'
elif unit_choice == 2:
    unit = 'ng/ml'
elif unit_choice == 3:
    unit = 'ug/ml'
elif unit_choice == 4:
    unit = 'mg/ml'

x = 1

print('-' * 30)
while x <= Number_of_cc:
    if x == Number_of_cc - 1:
        print(f'| std {str(x)}: {str(lloq * 0.9)} {unit}')
        x += 1
        continue
    print(f'| Std {str(x)}: {str(lloq)} {unit}')
    x += 1
    lloq = lloq * 2
print('-' * 30)
print('''
Done, please double check calculation.
''')
