import random

def play_rps():
    user = input("What's your choice? 'r' for rock 'p' for paper 's' for scissors \n" )
    computer = random.choice(["r", "p", "s"])
    
    if user == computer:
        return "It's a tie"
    
    # r > s, s > p, p > r
    if is_win(user, computer):
        return "You won!"
    
    #we could use else here but the code will need to pass above two statements to run below return line so we don't need another extra condition.
    return "You lost!"
    
def is_win (player, opponent):
    #return true if player wins
    #r > s, s > p, p > r
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") \
        or (player == "p" and opponent == "r"):
            return True
        
print(play_rps())