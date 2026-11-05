sum = 0

tuloy = True

while tuloy == True:
    num = int(input("Type a number --> "))
    print("--------------------------------")

    if num == 0:
        print("Loop Terminated")
        break
    else:
        print("Loop Continues")
        sum += num
        print("The sum is, ", sum)
        continue
