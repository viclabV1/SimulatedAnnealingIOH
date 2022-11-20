import ioh
from ioh import logger
from ioh import get_problem
from ioh import Experiment
from ioh import problem
import numpy as np


class SimulatedAnnealing:
    def __init__(self) -> None:
        print('init called')
    def __call__(prob) -> Any:
        pass

#expermient setup for my algo     
exp = Experiment(
    SimulatedAnnealing(),   # instance of optimization algorithm
    [1,2,23],                    # list of problem id's
    [1,1,1],                 # list of problem instances
    [4,9,16,25,36,49,64,81,100],                    # list of problem dimensions
    problem_type = 'PBO',  # the problem type, function ids should correspond to problems of this type
    njobs = 2,              # the number of parrellel jobs for running this experiment
    reps = 10,      
    logged=True,         
    folder_name="IOH_Data",
    algorithm_name="SimulatedAnnealing",
    logged_attributes = ['seed'],
    merge_output=True,
    zip_output=True,
    remove_data=True
)
exp.run()
#Example from https://iohprofiler.github.io/IOHexperimenter/python.html
# class RandomSearch:
#     def __init__(self, budget):
#         #Note that we should re-initialize all dynamic variables if we want to run the same algorithm multiple times
#         self.budget = budget

#         # A parameter static over the course of an optimization run of an algorithm
#         self.algorithm_id = np.random.randint(100)

#         # A dynamic parameter updated by the algorithm
#         self.a_tracked_parameter = None

#     def __call__(self, func):
#         self.f_opt = np.Inf
#         self.x_opt = None
#         for i in range(self.budget):
#             n = func.meta_data.n_variables
#             x = np.random.choice([0,1],n)

#             # Update the tracked parameter
#             self.a_tracked_parameter = i ** 10

#             f = func(x)
#             if f < self.f_opt:
#                 self.f_opt = f
#                 self.x_opt = x

#         return self.f_opt, self.x_opt

#     @property
#     def a_property(self):
#         return np.random.randint(100)

#     def reset(self):
#         self.algorithm_id = np.random.randint(100)

# exp = Experiment(
#     RandomSearch(10_000),   # instance of optimization algorithm
#     [1],                    # list of problem id's
#     [1, 2],                 # list of problem instances
#     [5],                    # list of problem dimensions
#     problem_type = 'BBOB',  # the problem type, function ids should correspond to problems of this type
#     njobs = 2,              # the number of parrellel jobs for running this experiment
#     reps = 2,               # the number of repetitions for each (id x instance x dim)
#     logged_attributes = [   # list of the tracked variables, must be available on the algorithm instance (RandomSearch)
#         "a_property",
#         "a_tracked_parameter"
#     ]
# )
# exp.run()
