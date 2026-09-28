no= input('quantity of salt'  'kg' )
if int(no)>10:
    print('in stock')
elif int(no)<10 and int(no) >0:
    print('low stock')
else:
    print('out of stock')

