import axelrod as axl
import csv
from axelrod import *
C, D = Action.C, Action.D
genetic_algo = axl.MockPlayer([C, D, D, C, D, C, D, D, D, D, D, D, D, D, D, D, C, D, C, D, D, D, C, C, C, D, C, D, D, D,
                               D, D, D, D, C, D, C, D, C, D, C, D, D, D, D, C, D, D, D, C, D, D, D, C, C, D, D, D, D, D,
                               D, D, C, D])

tabu_search = axl.MockPlayer([D, C, C, D, D, C, C, C, C, C, C, C, D, D, D, C, C, C, C, D, C, C, C, C, D, C, C, D, C, C,
                              C, C, C, C, C, D, D, C, C, C, C, D, D, C, C, D, D, C, C, C, C, D, C, D, C, C, D, C, D, C,
                              C, C, D, C])

sim_anneal = axl.MockPlayer([D, C, D, C, D, D, C, D, C, D, C, C, D, C, C, C, C, D, D, D, C, D, C, D, C, C, C, C, C, D,
                             D, C, D, C, C, C, D, C, D, D, C, C, D, D, D, D, C, D, D, C, D, D, D, C, C, D, D, D, D, D,
                             D, D, D, D])

players = [axl.TitForTat(), axl.Defector(), axl.SpitefulTitForTat(), axl.Cooperator(),
           axl.Cooperator(), axl.Prober(), axl.Grudger(), genetic_algo, tabu_search, sim_anneal]

game = axl.Tournament(players=players, turns=500, repetitions=5, seed=1)

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
plot.save_all_plots(f"C:\\Users\\xhorx\\PycharmProjects\\project1COMP3710\\plots\\graph", "graphs", "pdf")
