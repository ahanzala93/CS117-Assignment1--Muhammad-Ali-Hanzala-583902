# Convert star resistance values to delta resistance values.

def star_to_delta(ra, rb, rc):
    Total = ra * rb + rb * rc + rc * ra

    R1 = Total / rc
    R2 = Total / ra
    R3 = Total / rb

    return round(R1, 2), round(R2, 2), round(R3, 2)

Result = star_to_delta(10, 20, 30)

print("Delta resistances =", Result)