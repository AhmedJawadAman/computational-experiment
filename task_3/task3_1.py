p2 = 0.5          # chance to lose the 2-ruble coin
p5 = 0.2          # chance to lose the 5-ruble coin
limit = 3         # stepmother gets angry if more than 3 rubles are lost

p_calm = 0        # chance that the stepmother stays calm

# try all 4 cases: each coin is lost (True) or not lost (False)
for lost2 in (False, True):
    for lost5 in (False, True):
        # chance of this case (coins are independent, so multiply)
        if lost2:
            chance2 = p2
        else:
            chance2 = 1 - p2
        if lost5:
            chance5 = p5
        else:
            chance5 = 1 - p5
        chance = chance2 * chance5

        lost = 2 * lost2 + 5 * lost5      # rubles lost in this case
        angry = lost > limit

        print("Lost 2:", lost2, " Lost 5:", lost5,
              " Rubles lost:", lost, " Chance:", round(chance, 2),
              " Angry:", angry)

        if not angry:
            p_calm = p_calm + chance

print()
print("Chance the stepmother stays calm:", round(p_calm, 2))
