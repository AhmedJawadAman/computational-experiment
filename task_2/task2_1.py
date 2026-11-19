import math

B = 1000000                # starting money: 1,000,000 rubles
r = 0.07                   # 7% per year
T = 365 * 24 * 3600        # seconds in one year
dt = 2                     # the Knight updates every 2 seconds
N = T // dt                # number of steps in one year

A = (1 + r) ** (dt / T)    # growth for one 2-second step

print("Steps in one year:", N)
print("A =", A)

# ----- The Knight's algorithm: New = A * Old -----
money = B
for step in range(1, N + 1):
    money = A * money                  # New = A * Old

    # check the result after 1 day, 1 month, half a year, 1 year
    if step in (N // 365, N // 12, N // 2, N):
        t = step * dt                          # time in seconds
        correct = B * (1 + r) ** (t / T)       # the exact answer
        print("Day", round(t / 86400),
              " Knight:", round(money, 6),
              " Correct:", round(correct, 6),
              " Error:", round(money - correct, 6))


# ----- The correct algorithm: y = B * exp(C * t) -----
C = math.log(1 + r) / T            # math.log = ln (natural logarithm)
print()
print("C =", C)

for t in (T // 365, T // 12, T // 2, T, 10 * T):
    y = B * math.exp(C * t)        # calculated directly from B
    print("Day", round(t / 86400), " Money:", round(y, 6))

print("Check 1 year:  ", B * 1.07)
print("Check 10 years:", B * 1.07 ** 10)
