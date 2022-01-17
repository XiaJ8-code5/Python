print('-' * 40)
print('''*** For testing only ***
Stock solution preparation calculator
Refer to QAF 028 for more details
Ver: Jan 2022, by: Yi Wang''')
print('-' * 40)
input('Press Enter to continue...')

dn = str(input('Analyte: '))  # dn = drug name
ctrl_d = str.upper(input('Controlled substance, [Y/N]: '))  # ctrl_d = controlled drug
lp = str.upper(input('Light sensitivity, [Y/N]: '))  # lp = light protection
rp = float(input('Std ref purity: '))  # rp = ref purity
uc = int(input('Conc unit [1] ug/ml, [2] mg/ml: '))  # uc = unit choice
conc = float(input('Stock conc: '))  # conc = solution concentration
vol = float(input('Stock vol (ml): '))  # vol = solution volume
print('-' * 40)

slvt = int(input('''Solvent:
[1] MeOH/ACN/Ether 
[2] MeOH:B.P.water
[3] B.P.water
[4] DMSO
Enter choice: '''))  # slvt = solvent used
print('-' * 40)

if uc == 1:
    unit = 'ug/ml'
    tw = round(vol * conc / 1000, 5)  # tw = theoretical wt.
else:
    unit = 'mg/ml'
    tw = round(vol * conc, 5)

print('')
print('Please check preparation info below...')
print('-' * 40)
print(round(conc, 5), unit, dn, 'solution, volume:', vol, 'ml')
print('Using', dn, 'reference standard @', round(rp * 100, 5), '% purity')
if ctrl_d == 'Y':
    print('***:', dn, 'is a controlled substance !')
if lp == 'Y':
    print('***:', dn, 'is light sensitive !')
print('-' * 40)

input('Press Enter to continue...')

dw = round(tw / rp, 5)  # dw = desired weight
wf = round(dw * 0.005, 5)  # wf = weight factor (+/- 0.5% of dw)
w_ll = round(dw - wf, 5)  # w_ll = weight lower limit
w_ul = round(dw + wf, 5)  # w_ul = weight upper limit

print('-' * 40)
print('Theoretical wt (mg): ', tw)
print('Desired wt (mg): ', dw)
print('+/- 0.5 %: ', wf, 'mg')
print('Lower wt limit: ', w_ll)
print('Upper wt limit: ', w_ul)

if slvt == 1:
    print('Solution should be stored @ -20 freezer')
if slvt == 2 or slvt ==3:
    print("Solution should be stored @ 2 - 8 fridge")
if slvt == 4:
    print('Solution should be stored @ 25 incubator')
if ctrl_d == 'Y':
    print('***: Store in a secure location !')
if lp == 'Y':
    print('***: Under light protection !')

print('-' * 40)
print('End of calculation.')
