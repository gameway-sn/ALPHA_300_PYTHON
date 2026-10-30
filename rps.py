import random

def get_moves():
    user_move = input("rock, paper or scissors? ").strip().lower()

    moves = ["rock", "paper", "scissors"]
    bot_move = random.choice(moves)
    return {"user": user_move, "bot": bot_move}

def decide(user, bot):
    if user not in ["rock", "paper", "scissors"]:
        return "thats not a move, try rock, paper or scissors"

    print(f"you played {user}, bot played {bot}")
    if user == bot:
        return "draw"
    elif user == "rock":
        if bot == "scissors":
            return "you win"
        else:
            return "you lose"
    elif user == "paper":
        if bot == "rock":
            return "you win"
        else:
            return "you lose"
    elif user == "scissors":
        if bot == "paper":
            return "you win"
        else:
            return "you lose"

moves = get_moves()

outcome = decide(moves["user"], moves["bot"])

print(outcome)
