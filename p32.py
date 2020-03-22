def finddigit(x): #This function receives the number and if it had digit 8,the function would return 'yes'.
    while(x!=0):
        r=x%10
        if r==8:
            return 'yes'
            break
        x=int(x/10)
        
count=0
for i in range(5):
    a=int(input('Enter the number '))
    z=finddigit(a)
    if z=='yes':
        count+=1
print('The number of numbers which have digit 8 is',count)   

        
