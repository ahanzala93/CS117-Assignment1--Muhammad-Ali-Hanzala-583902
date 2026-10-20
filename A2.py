Current = float(input("Enter the current (in amperes): "))
if Current > 0:
    print("Current flows from A to B")
elif Current < 0:
    print("Current flows from B to A")
else:
    print("No current flows")
