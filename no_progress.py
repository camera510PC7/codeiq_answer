#  -*- codign: utf-8 -*-

value=input()

if value%2==0:
    print"invalid"
elif value==1:
    print "n"
else:
    
    n='n'
    d='.'
    nf=0
    
    
    for i in range(value):
        
        if i<1 or i>=value-1:
            nf=0
        else:
            nf=1
        
        print 'n'+d*(i-1)+n*nf+d*(value-i-2)+'n'

print "\n"