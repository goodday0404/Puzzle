# Puzzle

![image](https://user-images.githubusercontent.com/28790865/117384528-32d20080-aeb1-11eb-9182-e90feb9f7991.png)

### The goal of the puzzle:

At the bottom center position of the region, there is an opening that is 2-space wide. That is the gate to escape. The goal of this puzzle is to move the pieces horizontally and/or vertically within the region until the 2×2 piece is right above the opening at the bottom. At this position, the 2 × 2 piece can slide down and “escape” through the gate. You may only move a piece either horizontally or vertically if possible. No piece can be rotated.

### The board arrangement:

The puzzle has a rectangle board of width 4 and height 5. We will consider the variant with ten pieces. The ten pieces are of four different kinds. There is exactly one 2 × 2 piece. There are five 1 × 2 pieces. Each such piece is placed horizontally or vertically. In addition, there are four single-space pieces. After placing the ten pieces on the board, there should be exactly two empty spaces. In this configuration, one of the 1 × 2 pieces is placed horizontally and the other four 1 × 2 pieces are placed vertically.

### Other initial configuration:

There are many other initial configurations for this puzzle. For example:
![image](https://user-images.githubusercontent.com/28790865/117385292-cfe16900-aeb2-11eb-95e9-f45874933abd.png)

### Counting the number of moves:

Every time a piece moves one space in any direction, we will count it as one move. For example, if I start by moving the single-space piece in the bottom left corner by two spaces to the right, we will count it as two moves. As a result, for the initial configuration shown above, the optimal solution based on our method of counting moves takes 116 steps. Make sure that your search problem formulation is consistent with our way of counting moves.

### Search Algorithms:

1. A* search
2. Depth-first search

### Input format:

The implementations are test with two different puzzle configurations:
puzzle1<br/> 
2113\ 
2113. 
4665. 
4775. 
7007. 

puzzle2
1122
1137
4537
4577
0660

The first configuration is the initial configuration given in the picture above. Note that all the single-space pieces are denoted by 7. The two puzzle configurations will be provided in two files named puzzle1.txt and puzzle2.txt. You can hard-code these files names in your program. 


### Output format:
Once the program finds a solution, save it in a file using the format described below. 
For A* search, its solution files are named as the files puzzle1sol astar.txt and puzzle2sol astar.txt. For DFS, the solution files are named as the files puzzle1sol dfs.txt and puzzle2sol dfs.txt.

Each file contains:
* The initial configuration of the puzzle.
* The cost of the solution.
* The number of states expanded by the search algorithm. 
* The solution.

See an example of a solution file below. In this example, the solution is incomplete and the details are left out with the three dots before the final state.

Initial State:
2113
2113
4665
4775
7007

Cost of the solution: 116

Number of states expanded: 438177

Solution:

0
2113
2113
4665
4775
7007

1
2113
2113
4665
4775
7070

2
2113
2113
4660
4775
7075

3
2113
2113
4660
4775
0775

...

116
3254
3254
6677
7110
7110
