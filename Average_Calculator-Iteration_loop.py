import itertools
total=0
numbers=[]

for i in itertools.count(1): # itertools.count(1) creates an infinite sequence: 1, 2, 3, 4, ...
    # It is useful when we want a loop with a continuously increasing counter.
    numbers.append(int(input ("Enter number:")))# input() returns text (string), int() converts it to an integer,
    # and append() adds the number to the list.

    print("You give" , i)

    s=str(input("If you want to stop press S:"))
    if s.lower() == "s":
        total = sum(numbers)/i
        print ("                            ")
        print ("                            ")
        print ("Average is", total)
        break