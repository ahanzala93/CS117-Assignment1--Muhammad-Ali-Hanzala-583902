Voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9,
            12.0, 11.8, 11.6, 11.5, 11.5, 11.2]
Count = 1
Longest = 1
Start = Voltages[0]
End = Voltages[0]
CurrentStart = Voltages[0]
for i in range(1, len(Voltages)):
    if Voltages[i] < Voltages[i - 1]:
        Count = Count + 1
        if Count == 2:
            CurrentStart = Voltages[i - 1]
        if Count > Longest:
            Longest = Count
            Start = CurrentStart
            End = Voltages[i]
    else:
        Count = 1
print("Longest continuous drop:", Longest, "readings")
print("Started at:", Start, "V")
print("Ended at:", End, "V")
