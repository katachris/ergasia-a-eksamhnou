import random
# Εισαγωγή αριθμού ναρκών.
mines = int(input("Enter the number of mines\n you want to play with.\n\t"))
# Δημιουργία Board
board = [0] * 100
# Τυχαία τοποθέτηση ναρκών.
for i in range(mines):
    j = random.randint(0,99)
    board[j] = 'x'
print(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8],board[9],"\n",\
      board[10],board[11],board[12],board[13],board[14],board[15],board[16],board[17],board[18],board[19],"\n",\
      board[20],board[21],board[22],board[23],board[24],board[25],board[26],board[27],board[28],board[29],"\n",\
      board[30],board[31],board[32],board[33],board[34],board[35],board[36],board[37],board[38],board[39],"\n",\
      board[40],board[41],board[42],board[43],board[44],board[45],board[46],board[47],board[48],board[49],"\n",\
      board[50],board[51],board[52],board[53],board[54],board[55],board[56],board[57],board[58],board[59],"\n",\
      board[60],board[61],board[62],board[63],board[64],board[65],board[66],board[67],board[68],board[69],"\n",\
      board[70],board[71],board[72],board[73],board[74],board[75],board[76],board[77],board[78],board[79],"\n",\
      board[80],board[81],board[82],board[83],board[84],board[85],board[86],board[87],board[88],board[89],"\n",\
      board[90],board[91],board[92],board[93],board[94],board[95],board[96],board[97],board[98],board[99],"\n")
# Τοποθέτηση αριθμών που δείχνουν των αριθμό γειτονικών βομβών.
num = 0
i = 0
while i <= 99:
    if board[i] != 'x':
        # Ειδικές περιπτώσεις:
        # Γωνίες
        # Άνω αριστερά
        if i == 0:
            if board[1] == 'x':
                num = num + 1
            if board[10] == 'x':
                num = num + 1
            if board[11] == 'x':
                num = num + 1
        # Άνω δεξιά
        elif i == 9:
            if board[8] == 'x':
                num = num + 1
            if board[18] == 'x':
                num = num + 1
            if board[19] == 'x':
                num = num + 1
        # Κάτω αριστερά
        elif i == 90:
            if board[80] == 'x':
                num = num + 1
            if board[81] == 'x':
                num = num + 1
            if board[91] == 'x':
                num = num + 1
        # Κάτω δεξιά
        elif i == 99:
            if board[88] == 'x':
                num = num + 1
            if board[89] == 'x':
                num = num + 1
            if board[98] == 'x':
                num = num + 1
        # Πλευρές
        # Άνω
        elif i >= 1 and i <= 8:
            if board[i-1] == 'x':
                num = num + 1
            if board[i+1] == 'x':
                num = num + 1
            if board[i+9] == 'x':
                num = num + 1
            if board[i+10] == 'x':
                num = num + 1
            if board[i+11] == 'x':
                num = num + 1
        # Κάτω
        elif i >= 91 and i <= 98:
            if board[i-11] == 'x':
                num = num + 1
            if board[i-10] == 'x':
                num = num + 1
            if board[i-9] == 'x':
                num = num + 1
            if board[i-1] == 'x':
                num = num + 1
            if board[i+1] == 'x':
                num = num + 1
        # Αριστερή
        elif i % 10 == 0:
            if board[i-10] == 'x':
                num = num + 1
            if board[i-9] == 'x':
                num = num + 1
            if board[i+1] == 'x':
                num = num + 1
            if board[i+10] == 'x':
                num = num + 1
            if board[i+11] == 'x':
                num = num + 1
        # Δεξιά
        elif (i+1) % 10 == 0:
            if board[i-11] == 'x':
                num = num + 1
            if board[i-10] == 'x':
                num = num + 1
            if board[i-1] == 'x':
                num = num + 1
            if board[i+9] == 'x':
                num = num + 1
            if board[i+10] == 'x':
                num = num + 1
        # Κανονικές περιπτώσεις
        else:
            if board[i-11] == 'x':
                num = num + 1
            if board[i-10] == 'x':
                num = num + 1
            if board[i-9] == 'x':
                num = num + 1
            if board[i-1] == 'x':
                num = num + 1
            if board[i+1] == 'x':
                num = num + 1
            if board[i+9] == 'x':
                num = num + 1
            if board[i+10] == 'x':
                num = num + 1
            if board[i+11] == 'x':
                num = num + 1
        board[i] = num
    i += 1
    num = 0
print(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8],board[9],"\n",\
      board[10],board[11],board[12],board[13],board[14],board[15],board[16],board[17],board[18],board[19],"\n",\
      board[20],board[21],board[22],board[23],board[24],board[25],board[26],board[27],board[28],board[29],"\n",\
      board[30],board[31],board[32],board[33],board[34],board[35],board[36],board[37],board[38],board[39],"\n",\
      board[40],board[41],board[42],board[43],board[44],board[45],board[46],board[47],board[48],board[49],"\n",\
      board[50],board[51],board[52],board[53],board[54],board[55],board[56],board[57],board[58],board[59],"\n",\
      board[60],board[61],board[62],board[63],board[64],board[65],board[66],board[67],board[68],board[69],"\n",\
      board[70],board[71],board[72],board[73],board[74],board[75],board[76],board[77],board[78],board[79],"\n",\
      board[80],board[81],board[82],board[83],board[84],board[85],board[86],board[87],board[88],board[89],"\n",\
      board[90],board[91],board[92],board[93],board[94],board[95],board[96],board[97],board[98],board[99])
