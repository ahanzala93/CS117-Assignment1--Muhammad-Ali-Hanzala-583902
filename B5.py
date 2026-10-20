OnePercent = 0
FivePercent = 0
Reject = 0
Resistance = float(input("Enter resistance (0 to stop): "))
while Resistance != 0:
    if Resistance >= 99 and Resistance <= 101:
        OnePercent = OnePercent + 1
    elif Resistance >= 95 and Resistance <= 105:
        FivePercent = FivePercent + 1
    else:
        Reject = Reject + 1
    Resistance = float(input("Enter resistance (0 to stop): "))
print("1% tolerance:", OnePercent)
print("5% tolerance:", FivePercent)
print("Reject:", Reject)
