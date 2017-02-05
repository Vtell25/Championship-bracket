###############################################################################
# Programmers: Andrew Van Iderestine, Devon Dekker
# Description: Program takes input of players to make a roster and then makes a comptition bracket
# taking input from each win and loss
###############################################################################
import math
import random
def put_players_in_roster():
    roster = []
    infile = open("roster.txt", "r")
    for line in infile:
        line = line.strip()
        roster.append(line)
    infile.close()
    return roster
def find_bye(roster):
    if len(roster) % 2 != 0:
        bye = roster[random.randrange(len(roster))]
        roster.remove(bye)
    return roster, bye
def seat_players(roster):
    z = len(roster) / 2 
    matches = {}
    while z > 0:
        player1 = random.randrange(len(roster))
        player1 = roster.pop(player1)
        player2 = random.randrange(len(roster))
        player2 = roster.pop(player2)
        matches[player1] = player2
        z -= 1
    print(matches)
    return matches

def main():
    roster = put_players_in_roster()
    print(roster)
    roster, bye = find_bye(roster)
    print(roster)
    matches = seat_players(roster)
    print("matches are between %s, and %s has a bye this round" % (matches, bye))
    
    

main()
        
    