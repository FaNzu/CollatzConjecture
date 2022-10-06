import matplotlib.pyplot as plt, mpld3

C = {1:1}
T,J = [],[]
Totali = 0


def between(int1, int2):
    "flow of the collatz conjecture"
    Iterations, biggestnum, temp = 0,0,0
    for i in range(int1, int2):
        "running through all the numbers the user inputs"
        temp = collatz(i)
        J.append(i)
        T.append(temp)
        if (temp > Iterations):
            biggestnum = i
            Iterations = temp
        elif (temp == -1):
            print("failure to compute the conjecture")
    print("biggest ", biggestnum, " with the number interations: ", Iterations)
    print ("Total calculations: %d" % len (C))


def collatz(n):
    "calculate collatz conjecture for n, with saving old calculations in a dictionary"
    if not n in C:
        tmp = n // 2 if n % 2 == 0 else 3 * n + 1
        C[n] = 1 + collatz(tmp)
    return C[n]


def showgraph(MAX):
    "using Matplotlib to show a graph over the conjecture"
    fig = plt.figure(figsize = (14, 8))
    ax = fig.gca()
    ax.scatter(J,T, color = 'xkcd:lightish blue', s = 1)
    plt.xlim(xmax = MAX, xmin =- 25)
    plt.ylim(ymin = 0)
    plt.savefig("collatz_" + str(MAX) + ".png", bbox_inches = "tight", dpi = 600)
    mpld3.show(fig)


def main():
    "main function"
    print("Calculating Collatz Conjecture")
    print("lower bound > ")
    input1 = int(input())
    print("upper bound > ")
    input2 = int(input())
    between(input1, input2)
    showgraph(input2)


if __name__ == "__main__":
    main()
