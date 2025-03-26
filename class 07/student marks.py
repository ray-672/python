m = float(input('enter your math marks:'))
si = float(input('enter your science marks:'))
e = float(input('enter your english marks:'))
s = float(input('enter your sinhala marks:'))
f = float(input('enter your french marks:'))

tot = m+s+e+si+f
avg = tot/5

if avg>=90:
    print('grade A1')
elif avg >=80:
    print('A2')
elif avg >=70:
    print('B1')
elif avg >=60:
    print('B2')
elif avg >=50:
    print('C1')
else:
    print('D')

