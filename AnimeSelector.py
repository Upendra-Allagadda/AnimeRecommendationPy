import random
AnimeList = []
AnimeList = ["Naruto", "Boruto", "One Piece", "The Seven Deadly Sins", "Avatar-The last air bender", "Attack on Titans", "One Punch man", "Rick & Morth", "The Family Man"]

UserChoice = input("Do you need help selecting anime? [Y/N]:")

if(UserChoice in ["Y","y", "Yes", "YES","yes"]):
    print("Here is your anime to watch: " + random.choice(AnimeList))
elif UserChoice in ["N","n", "NO", "No", "no"]:
    print("Ok Bye!! Have a nice day!!")
else:
    print("Please enter a yes or no.")