smallest = None
largest = None
while True:
    try:
        number = input("Give a number: ")
        if number == 'Done':
            break
        n = int(number)
        if largest < n or largest == None:
            largest = n
        elif smallest > n or smallest == None:
            smallest = n
    except:
        print( "Input is Invalid")
        continue
print( "Maximum is ", largest)
print("Minimum is ", smallest)
