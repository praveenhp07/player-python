try:
	c=0
	x=str(raw_input())
	a=[]
	m=str()
	for i in range (0,len(x)):
		a.append(x[i])
	if len(x)%2==0:
		j=len(x)
	else:
		j=len(x)-1
	while(c!=j):
		t=a[c]
		a[c]=a[c+1]
		a[c+1]=t
		c=c+2
	for i in range (0,len(a)):
		m=m+a[i]
	print m
except:
 print "Invalid"
