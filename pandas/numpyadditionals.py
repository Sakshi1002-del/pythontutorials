import numpy as np
'''
#create identity matrix
im = np.eye(4)
print(im)
temparr = np.array([
    [31.8,36.4,11.5],
    [30.2,31.4,0]
    ])
temparri = temparr.astype('int')
temparrb = temparr.astype('bool')
    
print(temparrb)

print("*"*60)

list_of_numbers = [x for x in range(0,101,2)]
arr =np.array(list_of_numbers).reshape(17,3)
print(arr)

print("*"*60)

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([1,3,4,2,5])
print(np.where(arr1==arr2))

print("*"*60)

arr =np.full((2,3),5)
print(arr)

print("*"*60)

arr = np.array([
    [1,2,3],
    [4,5,5]
    ])
newarr = np.tile(arr,10)

print(newarr)

print("*"*60)

#print(np.random.seed(123))
randarr = np.random.randint(0,10,size=(5,5))
randnormal = np.random.normal(size=(5,5))

print(randarr)
print(randnormal)

print("*"*60)

array = np.array([10,1,5,2])
indexes = np.argsort(array)
print(indexes)

arr = np.array([
    [1,2,3],
    [4,5,5]
    ])
print(np.all(arr>4))

print("*"*60)
'''

'''
def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")
def check_winner(board, player):
    """Checks if the current player has won."""
    win_conditions = [
        [0, 1, 2],  # Row 1
        [3, 4, 5],  # Row 2
        [6, 7, 8],  # Row 3
        [0, 3, 6],  # Column 1
        [1, 4, 7],  # Column 2
        [2, 5, 8],  # Column 3
        [0, 4, 8],  # Diagonal 1
        [2, 4, 6]   # Diagonal 2
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False
def is_board_full(board):
    """Checks if the board is full."""
    return all(space in ['X', 'O'] for space in board)
def tic_tac_toe():
    """Main function to play Tic-Tac-Toe."""
    board = [' '] * 9  # Initialize the board
    current_player = 'X'
    
    while True:
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = current_player
                if check_winner(board, current_player):
                    print_board(board)
                    print(f"Player {current_player} wins!")
                    break
                if is_board_full(board):
                    print_board(board)
                    print("It's a tie!")
                    break
                current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("The chosen position is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")
if __name__ == "__main__":
    tic_tac_toe()
'''

import numpy as np

print(np.__version__)
np.show_config()
print("*"*60)

Z = np.zeros(10)
print(Z)
print("*"*60)

Z = np.zeros((10,10))
print("%d bytes" % (Z.size * Z.itemsize))
print("*"*60)

Z = np.zeros(10)
Z[4] = 1
print(Z)
print("*"*60)

Z = np.arange(10,50)
print(Z)
print("*"*60)

Z = np.arange(50)
Z = Z[::-1]
print(Z)
print("*"*60)

Z = np.arange(9).reshape(3, 3)
print (Z)
print("*"*60)

nz = np.nonzero([1,2,0,0,4,0])
print(nz)
print("*"*60)

Z = np.eye(3)
print(Z)
print("*"*60)

Z = np.random.random((3,3,3))
print(Z)
print("*"*60)

Z = np.random.random((10,10))
Zmin, Zmax = Z.min(), Z.max()
print(Zmin, Zmax)
print("*"*60)

Z = np.random.random(30)
m = Z.mean()
print(m)
print("*"*60)

Z = np.ones((10,10))
Z[1:-1,1:-1] = 0
print(Z)
print("*"*60)

Z = np.ones((5,5))
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
print(Z)
print("*"*60)

Z[:, [0, -1]] = 0
Z[[0, -1], :] = 0
print(Z)
print("*"*60)

0 * np.nan
np.nan == np.nan
np.inf > np.nan
np.nan - np.nan
np.nan in set([np.nan])
0.3 == 3 * 0.1

print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(np.nan in set([np.nan]))
print(0.3 == 3 * 0.1)
print("*"*60)

Z = np.diag(1+np.arange(4),k=-1)
print(Z)
print("*"*60)

Z = np.zeros((8,8),dtype=int)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)
print("*"*60)

print(np.unravel_index(99,(6,7,8)))
print("*"*60)

Z = np.tile( np.array([[0,1],[1,0]]), (4,4))
print(Z)
print("*"*60)


Z = np.random.random((5,5))
Z = (Z - np.mean (Z)) / (np.std (Z))
print(Z)
print(Z)
print("*"*60)

color = np.dtype([("r", np.ubyte),
                  ("g", np.ubyte),
                  ("b", np.ubyte),
                  ("a", np.ubyte)])

Z = np.dot(np.ones((5,3)), np.ones((3,2)))
print(Z)
print("*"*60)

# Alternative solution, in Python 3.5 and above
Z = np.ones((5,3)) @ np.ones((3,2))
print(Z)
print("*"*60)

Z = np.arange(11)
Z[(3 < Z) & (Z < 8)] *= -1
print(Z)
print("*"*60)

print(sum(range(5),-1))
from numpy import *
print(sum(range(5),-1))

# Author: Jake VanderPlas

print(sum(range(5),-1))
from numpy import *
print(sum(range(5),-1))
print("*"*60)

Z = np.random.uniform(-10,+10,10)
print(np.copysign(np.ceil(np.abs(Z)), Z))


# More readable but less efficient
print(np.where(Z>0, np.ceil(Z), np.floor(Z)))
print("*"*60)

Z1 = np.random.randint(0,10,10)
Z2 = np.random.randint(0,10,10)
print(np.intersect1d(Z1,Z2))
print("*"*60)

defaults = np.seterr(all="ignore")
Z = np.ones(1) / 0

# Back to sanity
_= np.seterr(**defaults)
 #Equivalently with a context manage
with np.errstate(all="ignore"):
    np.arange(3) / 0

yesterday = np.datetime64('today') - np.timedelta64(1)
today     = np.datetime64('today')
tomorrow  = np.datetime64('today') + np.timedelta64(1)

Z = np.arange('2016-07', '2016-08', dtype='datetime64[D]')
print(Z) 
print("*"*60)

Z = np.arange('2016-07', '2016-08', dtype='datetime64[D]')


A = np.ones(3)*1
B = np.ones(3)*2
np.add(A,B,out=B)
np.divide(A,2,out=A)
np.negative(A,out=A)
np.multiply(A,B,out=A)
print(Z)
print("*"*60)

Z = np.random.uniform(0,10,10)

print(Z - Z%1)
print(Z // 1)
print(np.floor(Z))
print(Z.astype(int))
print(np.trunc(Z))

print("*"*60)

Z = np.zeros((5,5))
Z += np.arange(5)
print(Z)

# without broadcasting
Z = np.tile(np.arange(0, 5), (5,1))
print(Z)
print("*" *60)

def generate():
    for x in range(10):
        yield x
Z = np.fromiter(generate(),dtype=float,count=-1)
print(Z)
print("*"*60)

Z = np.linspace(0,1,11,endpoint=False)[1:]
print(Z)
print("*"*60)

Z = np.random.random(10)
Z.sort()
print(Z)
print("*"*60)

Z = np.arange(10)
np.add.reduce(Z)
print("*"*60)

A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)

# Assuming identical shape of the arrays and a tolerance for the comparison of values
equal = np.allclose(A,B)
print(equal)

# Checking both the shape and the element values, no tolerance (values have to be exactly equal)
equal = np.array_equal(A,B)
print(equal)


