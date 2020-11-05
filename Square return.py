import math

while True:
    def homework(a_,n_):
        k=math.log(n_)/math.log(a_)
        result=round(k)
        return result

    print("input a")
    a=int(input())

    if a==1:
        print("The program has ended.")
        break
    else:
        print("input n")
        n=int(input())

        h=homework(a,n)
        print("k is ",h)