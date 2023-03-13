import math
def squreroot(num_val,approx_sqrt):
    quotient = int(num_val) / approx_sqrt
   # print(quotient)
    mean = (approx_sqrt + quotient) / 2
   # print("Mean square Root is ", mean)

    if round(quotient, 6) == round(mean, 6) :
        print("Square root for ", num_val, " is :", mean)
        return mean
    else:
        return squreroot(num_val, mean)


if __name__ == '__main__':
    # Enter an integer as input
    print("Question-1")
    print("--------------------")
    Num = input('Enter an integer value: ')
    approx_sqrt = math.isqrt(int(Num))
    #print(approx_sqrt)
    squreroot(int(Num), approx_sqrt)

    #Question2
    print(f"\nQuestion-2")
    print("--------------------")
    numlist = [159, 3400, 67, 598, 8999]
    sqrtlist = []
    tupl_list = []
    for i in range(len(numlist)):
        retval = squreroot(int(numlist[i]), math.isqrt(int(numlist[i])))
        sqrtlist.append(retval)
        tupl = (numlist[i], retval)
        tupl_list.append(tupl)
    print(f"\nQuestion-1b")
    print("--------------------")
    print(f"New List of Squareroots:\n", sqrtlist) #Answer to question 1b
    print(f"\nQuestion-1c")
    print("--------------------")
    print(f"Tuple with value and squareroot:\n", tupl_list)  # Answer to question 1c



