start= 'home'
dest= 'dornsheimer weg'
travel = 80 #time in minutes
time_h = int(input('How much time it took for walking from home to stop'))
walking_from_home = time_h

walking_from_dornsheimer=13

Total= walking_from_home + travel + walking_from_dornsheimer
print(Total)

cook_time=int(input('enter time taken for the cokking'))

cooking_day_time= Total + cook_time
print(cooking_day_time)
