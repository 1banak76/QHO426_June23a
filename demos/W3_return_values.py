def sum_weight(w1, w2):
    total_w = int(w1) + int(w2)
    return total_w


def calc_avg_weight(w1, w2):
    avg_w = ((int(w1)+int(w2))/2)
    return avg_w


def run():
    print("What is the weight of Beep ")
    w1 = input()
    print("What is the weight of Bop ")
    w2 = input()
    print("What would you like to calculate (sum or average)? ")
    choice = str(input())
    if choice == "sum":
        print(sum_weight(w1, w2))
    elif choice == "average":
        print(calc_avg_weight(w1, w2))
    else:
        print("incorrect selection")


run()

