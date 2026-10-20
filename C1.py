def ohms_current(v, r):
    return v / r
def power_dissipated(i, r):
    return i * i * r
Voltage = 12
Resistance = 6
Current = ohms_current(Voltage, Resistance)
Power = power_dissipated(Current, Resistance)
print("Current =", Current, "A")
print("Power =", Power, "W")