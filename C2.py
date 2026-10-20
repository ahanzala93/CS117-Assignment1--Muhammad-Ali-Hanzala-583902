def parallel_resistance(resistors):
    Total = 0
    for Resistance in resistors:
        Total = Total + 1 / Resistance
    return 1 / Total
print("parallel_resistance([10, 10]) =", parallel_resistance([10, 10]))
print("parallel_resistance([100, 200, 300]) =", round(parallel_resistance([100, 200, 300]), 2))