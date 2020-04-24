from fleet import Fleet
from thing import Thing

fleet = Fleet()

# Töltsd fel a fleet példányt olyan módon, hogy a következő legyen a kimenet:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch

get_milk = Thing('Get milk')
fleet.add(get_milk)
remove_the_obstacles = Thing('Remove the obstacles')
fleet.add(remove_the_obstacles)
stand_up = Thing('Stand up')
stand_up.complete()
fleet.add(stand_up)
eat_lunch = Thing('Eat lunch')
eat_lunch.complete()
fleet.add(eat_lunch)

print(fleet)