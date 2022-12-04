import ioh
from ioh import logger
from ioh import get_problem
from ioh import Experiment
from ioh import problem
import numpy as np


class SimulatedAnnealing:
    def __init__(self, budget):
        self.budget = budget
        self.algorithm_id = np.random.randint(100)

    def __call__(self, func: problem.PBO):
        func.state.evaluations
        self.f_opt = 0
        self.x_opt = None

        #variables:

        initialTemp = 1
        #exponential: alpha between 0 and 1
        #linear and quadratic: alpha above 0
        alpha = 0.5
        
        for i in range(self.budget):
            n = func.meta_data.n_variables
            x = np.random.choice([0,1],n)
            #COOLING SCHEDULES
            #Exponential multicplicative:
            temperature = initialTemp * pow(alpha, i)
            
            #Linear multiplicative:
            #temperature = initialTemp/(1+(alpha*i))
            
            #Quadratic multiplicative:
            #temperature = initialTemp/(a*pow(i,2))

            f = func(x)

            #deltaE
            deltaE = f-self.f_opt
            
            #If better, accept
            if deltaE > 0:
                self.f_opt = f
                self.x_opt = x
            
            #If not better but probability given temperature allows for
            else:
                tempProb = np.exp(deltaE*temperature)
                choice = np.random.choice([0,1], p=[(1-tempProb), tempProb])
                if choice == 1:
                    self.f_opt = f
                    self.x_opt = x



        return self.f_opt, self.x_opt

    def reset(self):
        self.algorithm_id = np.random.randint(100)

def main():
    #expermient setup for my algo     
    exp = Experiment(
        SimulatedAnnealing(10),   # instance of optimization algorithm
        [1,2,23],                    # list of problem id's
        [1,1,1],                 # list of problem instances
        [4,16,25,36,49,64],                    # list of problem dimensions
        problem_type = 'PBO',  # the problem type, function ids should correspond to problems of this type
        njobs = 2,              # the number of parrellel jobs for running this experiment
        reps = 10,      
        logged=True,         
        folder_name="IOH_Data",
        algorithm_name="SimulatedAnnealing",
        #logged_attributes = ['seed'],
        merge_output=True,
        zip_output=True,
        remove_data=True
    )
    exp.run()
if __name__=="__main__":
    main()
