#Negative Collatz Conjecture
#Iteration Counter
#Largest number identifier
#3n-1

i = 0
n = float(input("Enter negative Number: "))

n_Set = []

while n<-1:
    if n%2==0:
        n = n/2
        i+=1
        n_Set.append(n)
        print(n)
    elif n%2==1:
        n = (3*n)+1
        i+=1
        n_Set.append(n)
        print(n)

smallestNum = min(n_Set)

print ("Number of Iterations:\t", i)
print ("Smallest Number:\t", smallestNum)