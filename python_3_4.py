## 3 ##
Array1 = [1,2,1,3,5,6,4] 
Array2 = [5,2,1,3,4] 
Array3 = [1,2,1,3,7,3,1,5,4,4,5,6,4] 

def FindMax(A):
    Max = 0
    for i in range(len(A)):
        if A[i] > A[i - 1]:
            Max = i
    return print(Max)


## 4 ##
def facttorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return str(fact)

def FindZeroInFact(A):
    num = facttorial(A)
    count = 0
    for i in range(1, len(num)+1):
        if num[-i] == "0":
        count += 1
        elif num[-i] != "0":
        break;
    return count