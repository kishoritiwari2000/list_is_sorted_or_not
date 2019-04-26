def issorted(k):
    #logic here
    if k==sorted(k):
        return 'list is already sorted'
    else:
        return 'list is not sorted'
h=list(map(int,input('Enter the list').split()))
result=issorted(h)
print(result)
