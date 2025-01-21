import random

#Dice options using list() and range()
diceOptions = list(range(1, 7))

#Weapons array
weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear Bomb']

print("Available Weapons:", ', '.join(weapons))

# Inputs comnbat strength hero
combatStrength = int(input("Enter your combat strength (1-6): "))
if combatStrength < 1 or combatStrength > 6:
    print("Invalid input! Combat strength should be between 1 and 6. ")
    combatStrength = 1 #Default value for invalid inpit

# Inputs combat strength for monster
mCombatStrength = int(input("Enter monster's combat strength (1-6): "))
if mCombatStrength < 1 or combatStrength > 6:
    print("Invalid input! Monster combat strength should be between 1 and 6. ")
    combatStrength = 1 #Default value for invalid inpit

#simulate battle rounds
for j in range(1, 21, 2): #simulate of 20 rounds, stoppimg by2
    #dice rolls for hero and monster
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    # Calculate the weapons
    heroTotal = weapons[heroRoll - 1]
    monsterTotal = weapons[monsterRoll - 1]

    # Calculate total stregth
    heroTotal = combatStrength + heroRoll
    monsterTotal = combatStrength + monsterRoll

#print round details
    print("\nRound {j} hero rolled {heroRoll}, Monster rolled {monsterRoll} " )
    print("Gero selected: {heroTotal}, Monster selected: {monsterTotal}")
    print("Hero total strength: {heroTotal}, Monster total strength: {monsterTotal}")