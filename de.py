import numpy as np

def differential_evolution(func, bounds, population_size=20, F=0.8, CR=0.9, max_generations=100):
    dim = len(bounds)
    population = np.random.rand(population_size, dim)
    for i in range(dim):
        population[:, i] = bounds[i][0] + population[:, i] * (bounds[i][1] - bounds[i][0])
    
    fitness = np.apply_along_axis(func, 1, population)
    best_idx = np.argmin(fitness)
    best = population[best_idx].copy()
    best_fitness = fitness[best_idx]
    convergence = [best_fitness]

    for gen in range(max_generations):
        for i in range(population_size):
            idxs = [idx for idx in range(population_size) if idx != i]
            a, b, c = population[np.random.choice(idxs, 3, replace=False)]
            
            mutant = a + F * (b - c)
            mutant = np.clip(mutant, [bnd[0] for bnd in bounds], [bnd[1] for bnd in bounds])
            
            cross_idx = np.random.rand(dim) < CR
            if not np.any(cross_idx):
                cross_idx[np.random.randint(0, dim)] = True
            
            trial = np.where(cross_idx, mutant, population[i])
            f_trial = func(trial)
            
            if f_trial < fitness[i]:
                population[i] = trial
                fitness[i] = f_trial
                if f_trial < best_fitness:
                    best_fitness = f_trial
                    best = trial.copy()
        convergence.append(best_fitness)

    return best, best_fitness, convergence