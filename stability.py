from datetime import datetime, timedelta, date

ss_data = int(input('''Is SS data available:
[1] yes, according to a SOP
[2] yes, but will extent from VP
[3] no, waiting for SS data from VP
[4] n/a, solution used for MD
Enter choice: '''))

while ss_data != 1 and ss_data != 2 and ss_data != 3 and ss_data != 4:
    print('!! Invalid choice, please enter again !!')
    ss_data = int(input('Enter 1, 2, 3 or 4: '))

if ss_data == 2 or ss_data == 3:
    print('''Plz remember to update new expiry date on QAF 028.
    Plz remember to relabel expiry date on brown bottle.''')

if ss_data == 4:
    print('''Plz label n/a on QAF 028 and on brown bottle.
    Used for method development only.''')

if ss_data == 1:
    today = date.today()
    shlf = int(input('Stock solution stable for # days, \n # = '))  # shlf = shelf life
    shlf_bl = isinstance(shlf, int)
    if shlf_bl and shlf >= 1:
        expiry_date = today + timedelta(days=shlf)
        print('Today is'+today)
        print('Solution will expire on'+expiry_date)
    else:
        print('invalid ss data, plz re-enter: ')

print('Today is: \n', today)
