a = ['lia','mia','taila','matt']
marks = [87,90,80,76]
c = zip(marks,a)
print(list(c))

x = [10,20,30,40,50]
y= [100,200,300,400,500]

z = zip(x,y[::-1])
print(list(z))

stocks = ['r','t','e']
prices =[200, 300, 400]

d = {stock :value for stock,value in zip(stocks,prices)}

print(d)