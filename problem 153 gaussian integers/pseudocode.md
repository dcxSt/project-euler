# Problem 153 gaussian integers problem

Thinking this would only take me an afternoon I have had some difficulty debugging my script which I thought was correct and then it just kept getting uglier so i'm gonna fair ca proprement et structure everything and organise it.

### The slow way 
*cannot possible do the actual problem this way, it's just for checking*
init list1 - a list of the sums of the positive real parts of each factor of all the ks
for each k in range(1,n)
find all the positive integer factors of k
find all the positive gauseeian factors of k:
* initiate list of gaussian factors for k
* for each a + ib st a <= sqrt n and b <= a (think triangle)
* for each a+ib that divides k s.t. (a+ib) (c+id) = k
* add the following to the list of gaussian factors if they are not already on the list: (a+ib),(c+id),(a-ib),(c-id),(b+ia),(b-ia),(-d+ic),(-d-ic)
* sum all the real parts of the gaussian ints on the list with the positive integer factors and add this as the k'th entry of list1


### The fast way
*though this is the fast way, when I wrote it the first time I kept track of nothing, was done in 30 mins, but there were logic errors that I could not solve because it was too messy*
$\forall \{a+ib \in \C | a\in (0,\sqrt{n}+1), \quad b\in (0,a], \quad a,b\in \N}$ and $a^2+b^2<=n$
if gcd(a,b)=1
* find all paris of gaussian ints associated with $\pm \theta = arg(a+ib)$:
    * the smallest of which is (a+ib)(a+ib), lets call all the others $(a+ib)\cdot \alpha (a+ib)$
    * for each pair 


