count=0
j=0
a, b = raw_input().split()
if a==b:
    print "NO"
else:
    for i in a:
        if i==b[j]:
            j+=1
        else:
            j+=1
            count+=1
            if count>1:
                break
    if count==1:
        print "YES"
    else:
        print "NO"
