from matplotlib import pyplot as plt

time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

plt.plot(time, revenue)
plt.plot(time, costs)

plt.show()

print("Lets play a game\n\n")

x = "0"
while x :
    x = input("\nchoose a class ")
    if x == 'w':
        print("\nYour a wizard")
    if x == 's':
        print("\nYour a solder")
    if x == 'r':
        print("\nYour a rogue")