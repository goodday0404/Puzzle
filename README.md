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

The implementations are test with two different puzzle configurations: <br/>
<br/>
puzzle1<br/> 
![image](https://user-images.githubusercontent.com/28790865/117387965-cdcdd900-aeb7-11eb-9837-7314dbfd78d0.png)

<br/> 
2113<br/>
2113<br/>
4665<br/>
4775<br/>
7007<br/>
<br/>

puzzle2<br/>
![image](https://user-images.githubusercontent.com/28790865/117387900-b131a100-aeb7-11eb-9193-df1628020119.png)
<br/>
1122<br/>
1137<br/>
4537<br/>
4577<br/>
0660<br/>

The first configuration is the initial configuration given in the picture above. Note that all the single-space pieces are denoted by 7. The two puzzle configurations will be provided in two files named puzzle1.txt and puzzle2.txt. You can hard-code these files names in your program. 


### Output format:
Once the program finds a solution, save it in a file using the format described below. 
For A* search, its solution files are named as the files puzzle1sol_astar.txt and puzzle2sol_astar.txt. For DFS, the solution files are named as the files puzzle1sol_dfs.txt and puzzle2sol_dfs.txt.

Each file contains:
* The initial configuration of the puzzle.
* The cost of the solution.
* The number of states expanded by the search algorithm. 
* The solution.

See an example of a solution file below. In this example, the solution is incomplete and the details are left out with the three dots before the final state.<br/>
<br/>
Initial State:<br/>
2113<br/>
2113<br/>
4665<br/>
4775<br/>
7007<br/>
<br/>
Cost of the solution: 116 <br/>

Number of states expanded: 438177 <br/>
<br/>
Solution: <br/>
<br/>
0 <br/>
2113<br/>
2113<br/>
4665<br/>
4775<br/>
7007<br/>
<br/>
1<br/>
2113<br/>
2113<br/>
4665<br/>
4775<br/>
7070<br/>
<br/>
2<br/>
2113<br/>
2113<br/>
4660<br/>
4775<br/>
7075<br/>
<br/>
3<br/>
2113<br/>
2113<br/>
4660<br/>
4775<br/>
0775<br/>
<br/>
...<br/>
<br/>
116<br/>
3254<br/>
3254<br/>
6677<br/>
7110<br/>
7110<br/>
