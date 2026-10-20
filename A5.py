R1 = float(input("Enter R1: "))
R2 = float(input("Enter R2: "))
R3 = float(input("Enter R3: "))
if R1 <= R2 and R1 <= R3:
    print("Smallest = ", str(R1), "ohm")
elif R2 <= R1 and R2 <= R3:
    print("Smallest = ", str(R2), "ohm")
else:
    print("Smallest = ", str(R3), "ohm")
if R1 >= R2 and R1 >= R3:
    print("Largest = ", str(R1), "ohm")
elif R2 >= R1 and R2 >= R3:
    print("Largest = ", str(R2), "ohm")
else:
    print("Largest = ", str(R3), "ohm")
