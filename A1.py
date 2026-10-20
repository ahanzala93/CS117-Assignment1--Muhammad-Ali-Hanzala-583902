# Calculate current and check the fuse.

Voltage = input("Enter the voltage (in volts): ")
Resistance = input("Enter the resistance (in ohms): ")
if float(Resistance) <= 0:
     print("Invalid resistance")
else:
    Current = float(Voltage) / float(Resistance)
    if Current > 2:
        print("Current= " + str(Current) + " A")
        print("Fuse will blow")
    else:
        print("Current= " + str(Current) + " A")
        print("Circuit is safe")
