import os

import axelrod as axl
import csv
from axelrod import *
C, D = Action.C, Action.D
genetic_algo = axl.MockPlayer([C, C, C, D, D, D, C, D, D, D, D, D, D, D, D, D, C, D, C, C, C, D, D, D, D, D, D, C, C, C,
                               D, D, D, D, C, C, C, D, D, D, C, D, D, C, D, D, C, D, D, C, D, C, C, D, D, C, D, D, D, D,
                               C, D, D, D])
genetic_algo.name = "GeneticAlgo0.1/0.99"

genetic_algo2 = axl.MockPlayer([D, D, D, D, D, D, C, C, D, C, D, C, D, D, C, C, D, C, D, C, D, D, D, D, D, D, C, D, D,
                                C, D, D, D, D, D, C, C, C, C, D, D, D, D, D, D, D, D, D, D, D, D, D, C, D, D, D, C, D,
                                D, D, D, D, D, C])
genetic_algo2.name = "GeneticAlgo0.6/0.05"

tabu_search_coop = axl.MockPlayer([D, C, D, C, C, C, C, C, D, D, C, C, C, C, C, C, C, D, D, D, D, D, C, D, D, C, D, C,
                                   C, C, C, C, C, D, D, D, C, D, C, C, D, D, D, C, C, D, C, C, C, D, C, D, C, C, C, D,
                                   C, C, C, C, C, D, C, C])
tabu_search_coop.name = "Tabu Search Cooperative"

tabu_search_defect = axl.MockPlayer([D, C, D, C, D, C, C, D, C, D, D, D, C, D, D, D, D, D, C, C, C, D, D, D, C, C, D, C,
                                     D, C, D, D, D, D, C, D, D, C, D, C, D, C, D, D, C, C, D, C, D, C, D, D, D, D, D, C,
                                     D, D, D, C, C, C, D, D])

tabu_search_defect.name = "Tabu Search Defect"

sim_anneal = axl.MockPlayer([C, D, C, C, C, D, C, C, D, D, D, D, D, C, C, D, C, D, D, C, C, D, D, D, D, D, C, C, C, C,
                             C, D, D, D, D, D, D, D, C, D, C, D, C, D, D, D, D, C, D, C, D, C, C, C, D, D, D, D, D, C,
                             D, D, D, D])
sim_anneal.name = "Simulated Annealing"

players = [axl.TitForTat(), axl.SpitefulTitForTat(), axl.Cooperator(), axl.Defector(),
           genetic_algo, tabu_search_coop, sim_anneal, genetic_algo2, axl.FirmButFair(), axl.Darwin(),
           tabu_search_defect]

game = axl.Tournament(players)

interaction = game.play()
interaction.write_summary('summary.csv')

with open('summary.csv', 'r') as outfile:
    csvreader = csv.reader(outfile)
    for row in csvreader:
        print(row)
print(interaction.ranked_names)

plot = axl.Plot(interaction)
p = plot.boxplot()
p.show()
plot.save_all_plots(f"{os.getcwd()}\\plots\\graph", "graphs", "pdf")
