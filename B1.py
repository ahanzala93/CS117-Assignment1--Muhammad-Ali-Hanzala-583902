
# Calculate current for voltages from 1 V to 10 V.

Resistance = 10

for Voltage in range(1, 11):
    Current = Voltage / Resistance
    print("V =", Voltage, "V, I =", Current, "A")
