def loaded_divider(vs, r1, r2, rl):
    Unloaded = vs * r2 / (r1 + r2)

    Parallel = (r2 * rl) / (r2 + rl)
    Loaded = vs * Parallel / (r1 + Parallel)

    return Unloaded, Loaded

Result = loaded_divider(12, 1000, 1000, 500)

print("Unloaded voltage =", Result[0], "V")
print("Loaded voltage =", Result[1], "V")