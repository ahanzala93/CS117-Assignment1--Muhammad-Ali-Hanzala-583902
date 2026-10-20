Readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)
Count = 0
Highest = Readings[0]
Lowest = Readings[0]
Total = 0
for Voltage in Readings:
    if Voltage > 3.2:
        Count = Count + 1
    if Voltage > Highest:
        Highest = Voltage
    if Voltage < Lowest:
        Lowest = Voltage
    Total = Total + Voltage
Average = Total / 7
print("Readings above 3.2 V:", Count)
print("Highest:", Highest, "V")
print("Lowest:", Lowest, "V")
print("Average:", round(Average, 2), "V")
