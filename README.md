# Project Name

This project aims to employ various search algorithms and other optimization methods to find a strategy for the iterated prisoners’ dilemma. In this project, we employ a variety of search algorithms, namely the genetic algorithm, tabu search, and simulated annealing. Within these algorithms, we used a variety of criteria to assess the success of each. For example, in tabu search, we used an algorithm that would favor a more cooperative approach and one which would favor a more uncooperative approach. Similarly, in the genetic algorithm, we implemented various memory depths, population sizes, crossover, and mutation rates. The genetic algorithm was the strategy that yielded the most success as it pertained to the average score, and even win percentage, however other strategies while not as successful in terms of the median score, could be assessed as it pertained to their cooperation or defection ratings, to determine whether a more cooperative strategy or a more uncooperative strategy would be successful. Our findings led us to conclude that a good strategy must have these four characteristics. It must be forgiving, yet retaliatory but also be nice and non-envious.  


## Installation

To get started, follow these instructions:

1. Clone this repository to your local machine by running the following command in your terminal:

```git clone https://github.com/Aleksa-Vig/PrisonersDilemaOptimization-.git```

2. Open the project in PyCharm by navigating to File -> Open, selecting the project folder, and clicking "Open".

3. In PyCharm, navigate to File -> Settings -> Project: project-name -> Python Interpreter.

4. Click the "+" button to add a new package.

5. Search for the Axelrod package and click "Install Package".

## Usage

Once you've installed the necessary packages, you can either run the optimization Python files to create optimizations for the problem or run the `strategy.py` file to run the Axelrod tournament.

### Running optimization Python files

To run the optimization Python files, follow these steps:

1. Open the `[optimization].py` file in PyCharm.

2. Update the parameters to reflect your desired optimization scenario.

3. Run the `[optimization].py` file 

To run the `strategy.py` file, follow these steps:

1. Open the `strategy.py` file in PyCharm.

2. Update parameters (this includes players, and the encodings for the optimizations found in the parameters of the MockPlayer objects) to reflect your desired tournament scenario.

3. Run the `strategy.py` file 
