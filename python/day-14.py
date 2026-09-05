#Angle Between Hour and Minute Hand
import math
H = int(input("The hour hand is pointing: "))
M = int(input("The minute hand is pointing: "))

angle = 360-((H+M/60)*30)
print(math.floor(angle))
