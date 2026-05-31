import random
import time 

time.sleep(2)

print("Loading the list of games...")

points = [ "...", "..", "."]

for point in points:
    print(point)
    time.sleep(1.5)


games = ["Minecraft", "Roblox", "HOI4"]

print(f"You should play { random.choice(games)}!")