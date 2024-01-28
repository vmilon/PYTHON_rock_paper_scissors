print("***WELCOME TO ROCK-PAPER-SCISSORS***")
player1 = input("PLAYER 1 GIVE ME YOUR NAME:")
player2 = input("PLAYER 2 GIVE MY YOUR NAME:")
scoreboard = [0, 0]                                                                                                     #PLAYER SCORES
round = 1
while round <= 10:                                                                                                      #COUNTING ROUNDS. WHEN THE 10th ROUND FINISHES THE GAME IS OVER
    print("ROUND ", round, "!!!")
    print(player1, "PLEASE CHOOSE ONE\n")
    x = int(input("1. ROCK, 2. PENCIL, 3. SCISSOR, 4. PAPER, 5. EXIT : "))                                             # X IS PLAYER 1 CHOICE
    print("\n", player2, "PLEASE CHOOSE ONE\n")
    y = int(input("1. ROCK, 2. PENCIL, 3. SCISSOR, 4. PAPER, 5. EXIT : "))                                              # Y IS PLAYER 2 CHOICE

    if x == 1:                                                                                                          #USING IF/ELIF TO FIND WHO WINS THE ROUND
        if y == 2 | y == 3:
            print("WINNER IS ", player1)
            scoreboard[0] += 1
            round += 1
        elif y == 4:
            print("WINNER IS ", player2)
            scoreboard[1] += 1
            round += 1
        elif y == 1:
            print("IT'S A TIE. POINT FOR BOTH PLAYERS\n")
            scoreboard[0] += 1
            scoreboard[1] += 1
            round += 1
        elif y == 5:
            print(player2, " QUIT. WINNER IS", player1, "\n")
            scoreboard[0] = scoreboard[0] + 10
            round = round+10
        else:
            while (y != 1) & (y != 2) & (y != 3) & (y != 4) & (y != 5):                                                 #WHILE USER CHOOSES WRONG OPTIONS DISPLAY THIS MESSAGE
                print("PLEASE CHOOSE BETWEEN 1-5\n")
                y = int(input("1. ROCK, 2. PENCIL, 3. SCISSOR, 4. PAPER, 5. EXIT : "))   
                if y == 2 | y == 3:
                    print("WINNER IS ", player1)
                    scoreboard[0] += 1
                    round += 1
                elif y == 4:
                    print("WINNER IS ", player2)
                    scoreboard[1] += 1
                    round += 1
                elif y == 1:
                    print("IT'S A TIE. POINT FOR BOTH PLAYERS\n")
                    scoreboard[0] += 1
                    scoreboard[1] += 1
                    round += 1
                elif y == 5:
                    print(player2, "HAS QUIT. WINNER IS", player1, "\n")
                    scoreboard[0] = scoreboard[0] + 10
                    round = round+10

    elif x == 2:
        if y == 1 | y == 3:
            print("WINNER IS ", player2)
            scoreboard[1] += 1
            round += 1
        elif y == 4:
            print("WINNER IS ", player1)
            scoreboard[0] += 1
            round += 1
        elif y == 2:
            print("IT'S A TIE. POINT FOR BOTH PLAYERS\n")
            scoreboard[0] += 1
            scoreboard[1] += 1
            round += 1
        elif y == 5:
            print(player2, " HAS QUIT. WINNER IS", player1, "\n")
            scoreboard[0] = scoreboard[0] + 10
            round = round + 10
        else:
            while (y != 1) & (y != 2) & (y != 3) & (y != 4) & (y != 5):
                print("PLEASE CHOOSE BETWEEN 1-5\n")
                y = int(input('1. ROCK, 2. PENCIL, 3. SCISSOR, 4. PAPER, 5. EXIT : '))
                if y == 1 | y == 3:
                    print("WINNER IS ", player2)
                    scoreboard[1] += 1
                    round += 1
                elif y == 4:
                    print("WINNER IS ", player1)
                    scoreboard[0] += 1
                    round += 1
                elif y == 2:
                    print("IT'S A TIE. POINT FOR BOTH PLAYERS\n")
                    scoreboard[0] += 1
                    scoreboard[1] += 1
                    round += 1
                elif y == 5:
                    print(player2, " HAS QUIT. WINNER IS", player1, "\n")
                    scoreboard[0] = scoreboard[0] + 10
                    round = round + 10

    elif x == 3:
        if y == 2 | y == 4:
            print("WINNER IS ", player1)
            scoreboard[0] += 1
            round += 1
        elif y == 1:
            print("WINNER IS ", player2)
            scoreboard[1] += 1
            round += 1
        elif y == 3:
            print("IT'S A TIE. POINT FOR BOTH PLAYERS\n")
            scoreboard[0] += 1
            scoreboard[1] += 1
            round += 1
        elif y == 5:
            print(player2, " HAS QUIT. WINNER IS", player1, "\n")
            scoreboard[0] = scoreboard[0] + 10
            round = round + 10
        else:
            while (y != 1) & (y != 2) & (y != 3) & (y != 4) & (y != 5):
                print("PLEASE CHOOSE BETWEEN 1-5\n")
                y = int(input('1. ROCK, 2. PENCIL, 3. SCISSOR, 4. PAPER, 5. EXIT : '))
                if y == 2 | y == 4:
                    print("WINNER IS ", player1)
                    scoreboard[0] += 1
                    round += 1
                elif y == 1:
                    print("WINNER IS ", player2)
                    scoreboard[1] += 1
                    round += 1
                elif y == 3:
                    print("IT'S A TIE. POINT FOR BOTH PLAYERS\n")
                    scoreboard[0] += 1
                    scoreboard[1] += 1
                    round += 1
                elif y == 5:
                    print(player2, " HAS QUIT. WINNER IS", player1, "\n")
                    scoreboard[0] = scoreboard[0] + 10
                    round = round + 10

    elif x == 4:
        if y == 2 | y == 3:
            print("WINNER IS ", player2)
            scoreboard[1] += 1
            round += 1
        elif y == 1:
            print("WINNER IS ", player1)
            scoreboard[0] += 1
            round += 1
        elif y == 4:
            print("IT'S A TIE. POINT FOR BOTH PLAYERS\n")
            scoreboard[0] += 1
            scoreboard[1] += 1
            round += 1
        elif y == 5:
            print( player2, " HAS QUIT. WINNER IS", player1, "\n")
            scoreboard[0] = scoreboard[0] + 10
            round = round + 10
        else:
            while (y != 1) & (y != 2) & (y != 3) & (y != 4) & (y != 5):
                print("PLEASE CHOOSE BETWEEN 1-5\n")
                y = int(input('1. ROCK, 2. PENCIL, 3. SCISSOR, 4. PAPER, 5. EXIT : '))
                if y == 2 | y == 3:
                    print("WINNER IS ", player2)
                    scoreboard[1] += 1
                    round += 1
                elif y == 1:
                    print("WINNER IS ", player1)
                    scoreboard[0] += 1
                    round += 1
                elif y == 4:
                    print("IT'S A TIE. POINT FOR BOTH PLAYERS\n")
                    scoreboard[0] += 1
                    scoreboard[1] += 1
                    round += 1
                elif y == 5:
                    print(player2, " HAS QUIT. WINNER IS", player1, "\n")
                    scoreboard[0] = scoreboard[0] + 10
                    round = round + 10

    elif x == 5:
        print( player1, " HAS QUIT. WINNER IS", player2, "\n")
        scoreboard[1] = scoreboard[1] + 10
        round = round + 10
    else:
        while (y != 1) & (y != 2) & (y != 3) & (y != 4) & (y != 5):
            print("PLEASE CHOOSE BETWEEN 1-5\n")
            y = int(input('1. ROCK, 2. PENCIL, 3. SCISSOR, 4. PAPER, 5. EXIT : '))

if scoreboard[0] > scoreboard[1]:                                                                                       #COMPARING SCORES TO DECLARE WINNER
    print("*****GAME OVER. THANKS FOR PLAYING!!!!*****\n")
    print("*SCORE*\n")
    print(player1, ": ", scoreboard[0], "\n")
    print(player2, ": ", scoreboard[1], "\n")
    print("THE WINNER IS ", player1, "!!! CONGRATULATIONS")
elif scoreboard[1] > scoreboard[0]:
    print("*****GAME OVER. THANKS FOR PLAYING!!!!*****\n")
    print("*SCORE*\n")
    print(player1, ": ", scoreboard[0], "\n")
    print(player2, ": ", scoreboard[1], "\n")
    print("WINNER IS ", player2, "!!! CONGRATULATIONS")
else:
    print("*****GAME OVER. THANKS FOR PLAYING!!!!*****\n")
    print("*SCORE*\n")
    print(player1, ": ", scoreboard[0], "\n")
    print(player2, ": ", scoreboard[1], "\n")
    print("IT'S A TIE!!!!")                                                                                        #WILL ADD SUDDEN DEATH ROUND IN THE FUTURE
