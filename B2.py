
Number = int(input("How many resistors? "))
Total = 0
for i in range(1, Number + 1):
    Resistance = float(input("Enter R" + str(i) + ": "))
    Total = Total + Resistance
print("Total resistance =", Total, "ohm")
