while True:
    try:
        i = int(input('''Units:
[1] pg/ml
[2] ng/ml
[3] ug/ml
[4] mg/ml
Enter choice: '''))
    except ValueError:
        print('invalid choice, not integer')
        continue
    if i < 1 or i > 4:
        print('invalid choice, wrong integer')
        continue
    else:
        break

if i == 1:
    print('Unit is pg/ml')
elif i == 2:
    print('Unit is ng/ml')
elif i == 3:
    print('Unit is ug/ml')
elif i == 4:
    print('Unit is mg/ml')
print('End')
