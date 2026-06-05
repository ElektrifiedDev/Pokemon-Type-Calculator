TYPES = [
    "Normal", "Bug", "Dark", 
    "Dragon", "Electric", "Fairy", 
    "Fire", "Fighting", "Flying", 
    "Ghost", "Grass", "Ground", 
    "Ice", "Poison", "Psychic", 
    "Rock", "Steel", "Water"
    ]

DEF_TYPE_CHART = {
    "Normal" : {
        "Weak To" : [
            "Fighting"
            ],
        "Resistant To" : None,
        "Immune To" : [
            "Ghost"
            ],
        "Standard" : [
            "Normal", "Bug", "Dark", 
            "Dragon", "Electric", "Fairy", 
            "Fire", "Flying", "Grass", 
            "Ground", "Ice", "Poison", 
            "Psychic", "Rock", "Steel", 
            "Water"
            ]
    },
    "Bug" : {
        "Weak To" : [
            "Fire", "Flying", "Rock"
            ],
        "Resistant To" : [
            "Fighting", "Grass", "Ground"
            ],
        "Immune To" : None,
        "Standard" : [
            "Normal", "Bug", "Dark", 
            "Dragon", "Electric", "Fairy", 
            "Ghost", "Ice", "Poison", 
            "Psychic", "Steel", "Water"
            ]
    },
    "Dark" : {
        "Weak To" : [
            "Bug", "Fairy", "Fighting"
            ],
        "Resistant To" : [
            "Dark", "Ghost"
            ],
        "Immune To" : [
            "Psychic"
            ],
        "Standard" : [
            "Normal", "Dragon", "Electric", 
            "Fire", "Flying", "Grass", 
            "Ground", "Ice", "Poison", 
            "Rock", "Steel", "Water"
            ]
    },
    "Dragon" : {
        "Weak To" : [
            "Dragon", "Fairy", "Ice"
            ],
        "Resistant To" : [
            "Electric", "Fire", "Grass", 
            "Water"
            ],
        "Immune To" : None,
        "Standard" : [
            "Normal", "Bug", "Dark", 
            "Fighting", "Flying", "Ghost", 
            "Ground", "Poison", "Psychic", 
            "Rock", "Steel"
            ]
    },
    "Electric" : {
        "Weak To" : [
            "Ground"
            ],
        "Resistant To" : [
            "Electric", "Flying", "Steel"
            ],
        "Immune To" : None,
        "Standard" : [
            "Normal", "Bug", "Dark", 
            "Dragon", "Fairy", "Fire", 
            "Fighting", "Ghost", "Grass", 
            "Ice", "Poison", "Psychic", 
            "Rock", "Water"
            ]
    },
    "Fairy" : {
        "Weak To" : [
            "Poison", "Steel"
            ],
        "Resistant To" : [
            "Bug", "Dark", "Fighting"
            ],
        "Immune To" : [
            "Dragon"
            ],
        "Standard" : [
            "Normal", "Electric", "Fairy", 
            "Fire", "Flying", "Ghost", 
            "Grass", "Ground", "Ice", 
            "Psychic", "Rock", "Water"
            ]
    },
    "Fighting" : {
        "Weak To" : [
            "Fairy", "Flying", "Psychic"
            ],
        "Resistant To" : [
            "Bug", "Dark", "Rock"
            ],
        "Immune To" : None,
        "Standard" : [
            "Normal", "Dragon", "Electric", 
            "Fighting", "Fire", "Ghost", 
            "Grass", "Ground", "Ice", 
            "Poison", "Steel", "Water"
            ]
    },
    "Fire" : {
        "Weak To" : [
            "Ground", "Rock", "Water"
            ],
        "Resistant To" : [
            "Bug", "Fairy", "Fire", 
            "Grass", "Ice", "Steel"
            ],
        "Immune To" : None,
        "Standard" : [
            "Normal", "Dark", "Dragon", 
            "Electric", "Fighting", "Flying", 
            "Ghost", "Poison", "Psychic"
            ]
    },
    "Flying" : {
        "Weak To" : [
            "Electric", "Ice", "Rock"
            ],
        "Resistant To" : [
            "Bug", "Fighting", "Grass"
            ],
        "Immune To" : [
            "Ground"
            ],
        "Standard" : [
            "Normal", "Dark", "Dragon", 
            "Fairy", "Fire", "Flying", 
            "Ghost", "Poison", "Psychic", 
            "Steel", "Water"
            ]
    },
    "Ghost" : {
        "Weak To" : [
            "Dark", "Ghost"
            ],
        "Resistant To" : [
            "Bug", "Poison"
            ],
        "Immune To" : [
            "Fighting", "Normal"
            ],
        "Standard" : [
            "Dragon", "Electric", "Fairy", 
            "Fire", "Flying", "Grass", 
            "Ground", "Ice", "Psychic", 
            "Rock", "Steel", "Water"
            ]
    },
    "Grass" : {
        "Weak To" : [
            "Bug", "Fire", "Flying", 
            "Ice", "Poison"
            ],
        "Resistant To" : [
            "Electric", "Grass", "Ground", 
            "Water"
            ],
        "Immune To" : None,
        "Standard" : [
            "Normal", "Dark", "Dragon", 
            "Fairy", "Fighting", "Ghost", 
            "Psychic", "Rock", "Steel"
            ]
    },
    "Ground" : {
        "Weak To" : [
            "Grass", "Ice", "Water"
            ],
        "Resistant To" : [
            "Poison", "Rock"
            ],
        "Immune To" : [
            "Electric"
            ],
        "Standard" : [
            "Normal", "Bug", "Dark", 
            "Dragon", "Fairy", "Fighting", 
            "Fire", "Flying", "Ghost", 
            "Psychic", "Steel"
            ]
    },
    "Ice" : {
        "Weak To" : [
            "Fighting", "Fire", "Rock", 
            "Steel"
            ],
        "Resistant To" : [
            "Ice"
            ],
        "Immune To" : None,
        "Standard" : [
            "Normal", "Bug", "Dark", 
            "Dragon", "Electric", "Fairy", 
            "Flying", "Ghost", "Grass", 
            "Ground", "Poison", "Psychic", 
            "Water"
            ]
    },
    "Poison" : {
        "Weak To" : [
            "Ground", "Psychic"
            ],
        "Resistant To" : [
            "Bug", "Fairy", "Fighting", 
            "Grass", "Poison"
            ],
        "Immune To" : None,
        "Standard" : [
            "Normal", "Dark", "Dragon", 
            "Electric", "Fire", "Flying", 
            "Ghost", "Ice", "Rock", 
            "Steel", "Water"
            ]
    },
    "Psychic" : {
        "Weak To" : [
            "Bug", "Dark", "Ghost"
            ],
        "Resistant To" : [
            "Fighting", "Psychic"
            ],
        "Immune To" : None,
        "Standard" : [
            "Normal", "Dragon", "Electric", 
            "Fairy", "Fire", "Flying", 
            "Grass", "Ground", "Ice", 
            "Poison", "Rock", "Steel", 
            "Water"
            ]
    },
    "Rock" : {
        "Weak To" : [
            "Fighting", "Grass", "Ground", 
            "Steel", "Water"
            ],
        "Resistant To" : [
            "Fire", "Flying", "Normal", 
            "Poison"
            ],
        "Immune To" : None,
        "Standard" : [
            "Bug", "Dark", "Dragon", 
            "Electric", "Fairy", "Ghost", 
            "Ice", "Psychic", "Rock"
            ]
    },
    "Steel" : {
        "Weak To" : [
            "Fighting", "Fire", "Ground"
            ],
        "Resistant To" : [
            "Bug", "Dark", "Dragon", 
            "Fairy", "Flying", "Ghost", 
            "Grass", "Ice", "Normal", 
            "Psychic", "Rock", "Steel"
            ],
        "Immune To" : [
            "Poison"
            ],
        "Standard" : [
            "Electric", "Water"
            ]
    },
    "Water" : {
        "Weak To" : [
            "Electric", "Grass"
            ],
        "Resistant To" : [
            "Fire", "Ice", "Steel", 
            "Water"
            ],
        "Immune To" : None,
        "Standard" : [
            "Normal", "Bug", "Dark", 
            "Dragon", "Fairy", "Fighting", 
            "Flying", "Ghost", "Ground", 
            "Poison", "Psychic", "Rock"
            ]
    }
}

damageMultiplier = 1
defendingMonTypes = []

valid_AttackingMoveType = False
while valid_AttackingMoveType == False:
    attackingMoveType = input("Enter the type of the Attacking Move:   ")
    attackingMoveType = attackingMoveType.capitalize()
    if attackingMoveType in TYPES:
        valid_AttackingMoveType = True

valid_DefendingPrimaryType = False
while valid_DefendingPrimaryType == False:
    defendingPrimaryType = input("Enter the primary type of the Defending Pokemon:   ")
    defendingPrimaryType = defendingPrimaryType.capitalize()
    if defendingPrimaryType in TYPES:
        valid_DefendingPrimaryType = True
        defendingMonTypes.append(defendingPrimaryType)

valid_DefendingSecondaryType = False
while valid_DefendingSecondaryType == False:
    defendingSecondaryType = input("Enter the secondary type of the Defending Pokemon, if it exists. Else type 'N':   ")
    defendingSecondaryType = defendingSecondaryType.capitalize()
    if defendingSecondaryType in TYPES:
        valid_DefendingSecondaryType = True
        defendingMonTypes.append(defendingSecondaryType)
    elif defendingSecondaryType == "N":
        valid_DefendingSecondaryType = True
    
for pokemon_type in defendingMonTypes:
    # Get the defensive profile for the current type
    type_profile = DEF_TYPE_CHART[pokemon_type]
    
    # 1. Check if the type is Weak To the attacking move
    if type_profile["Weak To"] is not None and attackingMoveType in type_profile["Weak To"]:
        damageMultiplier *= 2
        
    # 2. Check if the type is Resistant To the attacking move
    elif type_profile["Resistant To"] is not None and attackingMoveType in type_profile["Resistant To"]:
        damageMultiplier *= 0.5
        
    # 3. Check if the type is Immune To the attacking move
    elif type_profile["Immune To"] is not None and attackingMoveType in type_profile["Immune To"]:
        damageMultiplier *= 0

# Print the final result to the user
print(f"\nThe move is {damageMultiplier}x effective against the defending Pokemon.")
input()