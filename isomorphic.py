try:
	st1=str(raw_input())
	st2=str(raw_input())
	a=[]
	b=[]
	d=[]
	c=0
	n=len(st1)
	for i in range(0,n):
		if st1[i] in a :
			b.append(i)
			c=i
		else:
			a.append(st1[i])
	for i in range(0,n):
		if(st1[i]==st1[c]):
			d.append(i)
		else: 
			pass
	x=len(d)-1
	while(x!=0):
		i=d[x]
		j=d[x-1]
		if (st2[i]==st2[j]):
			print "yes"
		else:
			print "no"
		x=x-1
except:
 print "Invalid"
