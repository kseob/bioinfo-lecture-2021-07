import sys 

if len(sys.argv) != 2 : 
    print(f"#usage : python {sys.argv[0]} [num]") 
    sys.exit()


n = int(sys.argv[1]) 

val = 1
while n >0 : 
    val *=n 
    n -= 1

print (val)


