import random
#=======================================ΔΗΛΩΣΗ ΣΥΝΑΡΤΗΣΕΩΝ========================================================================================
# Η συνάρτηση που καλείται κάθε φορά που εκτυπώνεται ο πίνακας.
def print_procedure():
    print("\n" + " " + board[0] + "|" + board[1] + "|" + board[2] + "\n-------\n" +\
                 " " + board[3] + "|" + board[4] + "|" + board[5] + "\n-------\n" +\
                 " " + board[6] + "|" + board[7] + "|" + board[8] + "\n")
# Η συνάρτηση που ελέγχει αν ο πίνακας έχει γεμίσει.
def all_filled():
    flag = True
    for i in range(0, 9):
        if (board[i] != 'o' and board[i] != 'x'):
            return False
    if flag == True:
        return True
# Η συνάρτηση που ελέγχει αν υπάρχει νικητής.
def winner():
    if (board[0] == board[1] == board[2] == 'x' or board[0] == board[1] == board[2] == 'o')\
    or (board[3] == board[4] == board[5] == 'x' or board[3] == board[4] == board[5] == 'o')\
    or (board[6] == board[7] == board[8] == 'x' or board[6] == board[7] == board[8] == 'o')\
    or (board[0] == board[3] == board[6] == 'x' or board[0] == board[3] == board[6] == 'o')\
    or (board[1] == board[4] == board[7] == 'x' or board[1] == board[4] == board[7] == 'o')\
    or (board[2] == board[5] == board[8] == 'x' or board[2] == board[5] == board[8] == 'o')\
    or (board[0] == board[4] == board[8] == 'x' or board[0] == board[4] == board[8] == 'o')\
    or (board[2] == board[4] == board[6] == 'x' or board[2] == board[4] == board[6] == 'o'):
        return True
    else:
        return False
#=====================================================================================================================================================
#=========================================ΕΝΑΡΞΗ ΠΑΙΧΝΙΔΙΟΥ===========================================================================================
# Ο παίκτης διαλέγει τον χαρακ΄τηρα του.
playerchar = input("You want to play with Xs or Os?\nEnter 'x' for choice 1 or 'o' for choice 2\n")
if playerchar == 'o':
    computerchar = 'x'
else:
    computerchar = 'o'
board = ['\t'.expandtabs(1),'\t'.expandtabs(1),'\t'.expandtabs(1),'\t'.expandtabs(1),'\t'.expandtabs(1),'\t'.expandtabs(1),'\t'.expandtabs(1),'\t'.expandtabs(1),'\t'.expandtabs(1)]
print("The way you play the game is by entering the\nnumber of the cell you want to place your 'x'\nor your 'o' starting the numbering from 0 to 8\nand wait for the computer to make it's move until\nyour turn comes again\n")
print(" 0 | 1 | 2 \n-----------\n 3 | 4 | 5\n-----------\n 6 | 7 | 8 \n")
# Ποιος παίζει πρώτος
start = random.randint(0,1)
if start == 0:
    print("The computer plays first!\n")
    turn = random.randint(0,8)
    board[turn] = computerchar
else:
    print("You play first!\n")
    turn = int(input("Enter the cell number.\n" + "\t".expandtabs(9)))
    while turn < 0 or turn > 8:
        turn = int(input("Enter the cell number.\n" + "\t".expandtabs(9)))
    board[turn] = playerchar
print_procedure()
# Ροή παιχνιδιού.
if board[turn] == computerchar:
    turn_switcher = 1
else:
    turn_switcher = -1
while all_filled() == False and winner() == False:
    if turn_switcher == -1:
        print("It's the computer's turn!\n")
        turn = random.randint(0,8)
        while board[turn] == 'o' or board[turn] == 'x':
            turn = random.randint(0,8)
        board[turn] = computerchar
    else:
        print("It's your turn!\n")
        turn = int(input("Enter the cell number.\n" + "\t".expandtabs(9)))
        while turn < 0 or turn > 8:
            turn = int(input("Enter the cell number.\n" + "\t".expandtabs(9)))
        board[turn] = playerchar
    print_procedure()
    # Εναλλαγή σειράς.
    turn_switcher *= -1
# Επιλογή νικητή.
if winner() == True and turn_switcher == 1:
    print("The computer wins!\n")
elif winner() == True and turn_switcher == -1:
    print("You win!\n")
elif all_filled() == True:
    print("Tie game!\n")
#============================================================================================================================================
