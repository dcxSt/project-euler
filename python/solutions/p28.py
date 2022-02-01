s = 1 # sum
for odd in range(3,1002,2):
    s += odd**2
    s += odd**2 - odd + 1
    s += odd**2 - 2*(odd - 1)
    s += odd**2 - 3*(odd - 1)

print(s)
