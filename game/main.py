board = []
winScan = ["012", "345", "678", "036", "147", "258", "048", "642"]
turn = "o"
winner = "Nobody"
turnAmount = 1

for t in range(9):
    board.append(str(t + 1))

def display_board():
    print(board[0] + "|" + board[1] + "|"+ board[2] + "\n" + 
    board[3] + "|" + board[4] + "|"+ board[5] + "\n" + 
    board[6] + "|" + board[7] + "|"+ board[8])

def set_turn():
    global turn
    if turn == "x":
        turn = "o"
    else:
        turn = "x"

def take_turn():
    answer = ""
    while board.count(answer) == 0 or answer == "x" or answer == "y":
        if turn == "x":
            print("x's turn to choose a square (1-9): ")
        else:
            print("o's turn to choose a square (1-9): ")
        answer = input()
        if board.count(answer) == 0 or answer == "x" or answer == "y":
            print("invalid answer")
    board.insert(board.index(answer), turn)
    board.remove(answer)

def scan_board():
    global winner
    for rowScan in range(8):
        row = (board[int(winScan[int(rowScan)][0:1])] + board[int(winScan[int(rowScan)][1:2])] + board[int(winScan[int(rowScan)][2:3])])
        if row == "xxx":
            winner = "X"
        if row == "ooo":
            winner = "O"

display_board()
while winner == "Nobody" and turnAmount < 10:
    set_turn()
    take_turn()
    display_board()
    scan_board()
    turnAmount += 1
print(winner + " wins!\nGood game. Thanks for playing!")