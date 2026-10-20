def rms_voltage(voltages):
    Total = 0
    for Voltage in voltages:
        Total = Total + Voltage * Voltage
    Average = Total / len(voltages)
    return Average ** 0.5
Readings = [10, 20, 30]
Result = rms_voltage(Readings)
print("RMS voltage =", round(Result, 2), "V")