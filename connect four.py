# board for test
board = [[], [], [], [], [], [], []]

	# define function to display Connect Four board here. Board displays at 90 degrees from normal position, as if
	# gravity is on the left side pulling it towards the left.
def draw_board(board):
	for i in range(6):
		print(board[i])

	# write function to gather user input for their move here. Thinking use the del and append methods to ensure board
	# progresses nicely
def user_move(board):
	move = int(input("Enter your move(1-7 Top to Bottom): ")) - 1
	board[move].append("R")


# write function to check number of open spaces left.
def check_used_spaces(board):


# write function to check victory conditions.
def check_victory_conditions(board):


# write function to draw computer move. Start random.
def computer_move(board):


# call the creation of the board here and write code for the back and forth play of the game till victory is met.

# write code to declair winner/tie.


# Test lines of code. Modify to suit needs.


draw_board(board)
user_move(board)
draw_board(board)
user_move(board)
draw_board(board)
user_move(board)
draw_board(board)
user_move(board)
draw_board(board)
user_move(board)
draw_board(board)