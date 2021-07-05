import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [num]")
    sys.exit()


num = int(sys.argv[1]) 


if num%3 ==0 and num%7 == 0 : 
    print ('3','7')
elif  num%3 == 0 : 
    print ('3')
elif num%7 == 0 :
    print ('7')
else :
    print('not')
