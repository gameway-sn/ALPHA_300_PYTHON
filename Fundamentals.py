# variables
# no need to say the type, python works it out from the value
keeper = "Dhoni"
jersey = 7
strike_rate = 135.6

# comments - anything after # is skipped, so i use it for notes like this

# datatypes
print(isinstance(keeper, str))         # True
print(isinstance(jersey, int))         # True
print(isinstance(strike_rate, float))  # True

is_captain = True
print(type(is_captain))    # <class 'bool'>

overs = range(1, 21)       # 1 to 20, the end number is not included
print(type(overs))         # <class 'range'>
print(list(overs)[:5])     # [1, 2, 3, 4, 5]
# complex, list, tuple, dict and set are further down

# arithmetic operators
partnership = 45 + 32            # 77
runs_needed = 181 - partnership  # 104
from_fours = 6 * 4               # 24
run_rate = 180 / 20              # 9.0  -> / always gives a float
print(partnership, runs_needed, from_fours, run_rate)

balls = 125
print(balls // 6, balls % 6)  # 20 5  -> 20 overs and 5 balls, // drops the decimal part
print(2 ** 5)                 # 32

# comparison operators - always give True or False
kohli = 82
rohit = 64
print(kohli == rohit, kohli != rohit)   # False True
print(kohli > rohit, kohli >= 82)       # True True
print(rohit < 50, rohit <= 64)          # False True

# logical operators
won_toss = True
bowling_first = False
print(won_toss and bowling_first)   # False
print(won_toss or bowling_first)    # True
print(not bowling_first)            # True

# or returns the first truthy value, and returns the first falsy value
# if it doesnt find one it just returns the last value
print(0 or 50, "" or "no ball", "wide" or "bye", [] or None, None or [])
# 50 no ball wide None []
print(0 and 50, 50 and 0, None and "out", "four" and "six", [] and None, None and [])
# 0 0 None six [] None

# bitwise operators - they work on the binary bits
a = 6    # 110
b = 3    # 011
print(a & b)    # 2  -> 010
print(a | b)    # 7  -> 111
print(a ^ b)    # 5  -> 101
print(~a)       # -7 -> ~x is always -(x+1)
print(a << 1)   # 12 -> left shift doubles it
print(a >> 1)   # 3  -> right shift halves it

# is / in
squad = ["Dhoni", "Jadeja", "Ashwin"]
same_squad = squad
new_squad = ["Dhoni", "Jadeja", "Ashwin"]
print(same_squad is squad)   # True  -> both point to the same list
print(new_squad is squad)    # False -> same values but a different list
print(new_squad == squad)    # True
print("Jadeja" in squad)     # True
print("Pant" not in squad)   # True

# strings
team = "sunrisers "
team += "hyderabad"
print(team)    # sunrisers hyderabad

"""
string methods i went through
isalpha() isalnum() isdecimal()
lower() islower() upper() isupper()
title() startswith() endswith()
replace() split() join() find()
"""

print(team.upper())              # SUNRISERS HYDERABAD
print(team.title())              # Sunrisers Hyderabad
print(team.islower())            # True
print("SRH".isupper())           # True
print("SRH".lower())             # srh
print("Dhoni".isalpha())         # True
print("Dhoni7".isalnum())        # True
print("2011".isdecimal())        # True
print(team.startswith("sun"))    # True
print(team.endswith("bad"))    # True
print("risers" in team)           # True
print(team.find("hyderabad"))    # 10
print(team.replace("sunrisers", "orange army"))   # orange army hyderabad
words = team.split()
print(words)                     # ['sunrisers', 'hyderabad']
print("-".join(words))           # sunrisers-hyderabad

# slicing [start:end:step], end is not included
print(team[:9])      # sunrisers
print(team[10:15])   # hyder
print(team[::-1])    # dabaredyh sresirnus

# complex numbers
z = complex(4, -2)
print(z)               # (4-2j)
print(z.real, z.imag)  # 4.0 -2.0

# built in functions
print(round(135.678, 2))   # 135.68
print(round(9.5))          # 10
print(len(squad))          # 3

# lists - can hold different types and can be changed
batting = ["Rohit", 45, "Gill", False, "Kohli", 82]

batting[2] = "Jaiswal"
batting += ["Pant"]

print(batting[2:4])    # ['Jaiswal', False]
print(batting)

batting.pop()           # removes the last one
batting.insert(1, "Rahul")
print(batting)

# tuples - like lists but cant be changed
openers = ("Rohit", "Gill")

print(openers.index("Gill"))   # 1
print(openers)

# dictionaries - key : value
scorecard = {"batter": "Kohli", "runs": 82}

scorecard["runs"] = 100

print(scorecard)   # {'batter': 'Kohli', 'runs': 100}

# sets - no duplicates, no fixed order
playing_xi = {"Rohit", "Kohli", "Bumrah"}
injured = {"Bumrah"}

fit_players = playing_xi - injured
print(fit_players)   # order can change every time i run it

# functions

def appeal():
    print("Howzat!")

appeal()
appeal()
appeal()
