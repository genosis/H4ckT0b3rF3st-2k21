
import functools

	
def LargSubSet(S,lensub):
    
   greatest_product=0 
   
   length=len(S)

   for i in range(length-lensub+1):
	
        result=functools.reduce(lambda x,y:x*y,S[i:i+lensub])
		
        greatest_product=max(greatest_product,result)

   return greatest_product   


S="""73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
"""


S=S.replace("\n","")

S=[int(i) for i in S]

print(LargSubSet(S,13))