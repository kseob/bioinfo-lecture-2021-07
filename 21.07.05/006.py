

import sys
if len(sys.argv) != 2 :
    print (f"#usage: python {sys.argv[0]} [num]")
    sys.exit()
 
print (sys.argv[0])
print (sys.argv[1])
print (len(sys.argv))

val = 1
for i in range(int(sys.argv[1])) : 
    val *= i 

print (val)
    
