# unruly_solver
Solver for Unruly on Simon Tatham's Portable Puzzle Collection website \
Link : https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/unruly.html

About Easy and Normal difficulty from solver pov \
\
Easy can be solved with simple deduction only. Which includes :
- Put the opposite color on both side of a line of two squares of same color (ie [0, 1, 1, 0])
- Put the opposite color between two cells of same color (ie [1, 0, 1])
- Put all the only missing color on a straight line (ie [1, 0, 1, 0, 1, 0, 1, 0])

\
Normal have to be sold with advanced deduction which includes :
- Deduce that on a delimited range there must be a specific color which gives a clue outside the range (ie [0, -1, 0, 0, 1, -1, 1, -1])
  With the exemple above you can deduce there must be a "-1" in range [2, 3], it means all 4 "-1" have been used, so cell at index 0 cannot be equal to -1
- Bruteforce lol
