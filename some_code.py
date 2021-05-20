from mastermind.board import board
from mastermind.solver import solver

mboard = board(4, 4)
mboard.set_secret([0,1,2,3])
msolver = solver()


msolver.solve(mboard)
print(mboard.try_list)





