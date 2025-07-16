print('kmh to mph')
for speed in range(0, 101,10):
    mph = speed *  0.62137
    print(speed, '\t', f"{mph:.1f}")

print('mph to kmh')
for speed in range(0, 101,10):
    kph = speed *  1.6093
    print(speed, '\t', f"{kph:.1f}")