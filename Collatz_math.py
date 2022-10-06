import matplotlib.pyplot as plt

C = {1:1}
T,J = [],[]
HighestNmb,Totali = 0,0


def between(int1, int2):
    "flow of the collatz conjecture"
    hailstorm, biggestnum, temp= 0,0,0
    for i in range(int1, int2):
        "running through all the numbers the user inputs"
        temp = Collatz(i)
        J.append(i)
        T.append(temp)
        if (temp > hailstorm):
            biggestnum = i
            hailstorm = temp
        elif (temp == -1):
            print("failure to compute hailstorm")
    print("biggest ", biggestnum, " with the number hailstorms: ", hailstorm)
    print ("Length : %d" % len (C))


def Collatz(n):
    "calculate collatz conjecture for n, with saving old calculations in a dictionary"
    if not n in C:
        tmp = n//2 if n%2==0 else 3*n+1
        C[n] = 1 + Collatz(tmp)
    return C[n]


def main():
    "main function"
    print("Calculating Collatz Conjecture")
    print("lower bound >")
    input1 = int(input())
    print("upper bound >")
    input2 = int(input())
    between(input1, input2)
    showgraph(input2)


def showgraph(MAX):
    "using Matplotlib to show a graph over the conjecture"
    plt.xlabel("$n$",fontsize=20)
    plt.ylabel("Steps to reach 1")
    plt.title("Collatz Conjecture")
    plt.plot(J,T,'o',color="black", ms=1)
    plt.xlim(xmax=MAX,xmin=-25)
    plt.ylim(ymin=0)
    plt.savefig("collatz_"+str(MAX)+".png",bbox_inches="tight",dpi=600)
    plt.show()


if __name__ == "__main__":
    main()