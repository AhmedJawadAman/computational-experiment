import math                 # gives us cos(), pi, tan()

alf1 = 15                   # angle in degrees
m1 = 9                      # mass in grams
g1 = 9.81                   # gravity in Moscow

alf = math.pi * alf1 / 180  # degrees → radians
F = m1 * g1 * math.cos(alf) / 1000   # /1000 = grams → kg

print("Force F =", F, "N")

# ----- error of the result -----

# relative error of each input
dm = 0.5 / m1          # mass:    0.5 g out of 9 g
dg = 0.02 / g1         # gravity: 0.02 out of 9.81
dalf = 0.5 / alf1      # angle:   0.5 degrees out of 15

print("Mass error:   ", round(dm * 100, 2), "%")
print("Gravity error:", round(dg * 100, 2), "%")
print("Angle error:  ", round(dalf * 100, 2), "%")

# teacher's formula: dF = dm + dg + tan(alf) * dalf
dF = dm + dg + math.tan(alf) * dalf

print("Relative error of F:", round(dF * 100, 2), "%")
print("Absolute error of F:", round(F * dF, 5), "N")
print("Answer: F =", round(F, 4), "+/-", round(F * dF, 4), "N")
