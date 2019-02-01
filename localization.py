#
# Localization for a self driving car
#
p = []  # p is the initial belief - PRIOR
n = 5  # n is number of elements or landmarks - len(p)
prob = 1 / n  # Equal probability initially
for i in range(n):
    p.append(prob)  # populate p
world = []  # empty blocks
pHit = 0.6  # if block matches with robots signal, increase its probability
pMiss = 0.2  # if block doesnot match, decrease its probability
# populate world
for i in range(n):
    if i == 1 or i == 2:
        world.append("red")
    else:
        world.append("green")
# world = ['green','red','red','green','green']
Z = ["red", "green"]  # robot's signal


# Function for sensing Single signal
def sense(x, Z):
    # Probability after receiving robot's signal
    for i in range(len(x)):
        hit = (Z == world[i])
        x[i] = x[i] * (hit * pHit + (1 - hit) * pMiss)
    # Normalize
    s = sum(x)
    for i in range(n):
        x[i] = x[i] / s  # POSTERIOR


q = []  # Changed probabilities after receiving multiple robots' signals
r = []  # Temp list
for i in range(len(Z)):
    x = list(p)
    sense(x, Z[i])
    q.append(x)
print(q)
