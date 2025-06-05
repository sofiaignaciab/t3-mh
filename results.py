import numpy as np
import pandas as pd
from pso import pso
from main import param_configs_pso, functions

output_path = 'pso_iterations_results_separated.xlsx'

with pd.ExcelWriter(output_path) as writer:
    for func_name, (function, bounds) in functions.items():
        iteration_results = []

        for run in range(10):  
            iteration_data = {'Iteración': run + 1}
            
            for cfg in param_configs_pso:
                best_x, best_f, fitness_values = pso(function, bounds, swarm_size=cfg['swarm_size'],
                                                     w=cfg['w'], c1=cfg['c1'], c2=cfg['c2'],
                                                     max_generations=200)

                iteration_data[f'Media_Mejor_{func_name}_s{cfg["swarm_size"]}_w{cfg["w"]}_c1{cfg["c1"]}_c2{cfg["c2"]}'] = np.mean(fitness_values)
                iteration_data[f'Std_Mejor_{func_name}_s{cfg["swarm_size"]}_w{cfg["w"]}_c1{cfg["c1"]}_c2{cfg["c2"]}'] = np.std(fitness_values)
                iteration_data[f'Rango_{func_name}_s{cfg["swarm_size"]}_w{cfg["w"]}_c1{cfg["c1"]}_c2{cfg["c2"]}'] = np.max(fitness_values) - np.min(fitness_values)
                iteration_data[f'Mediana_{func_name}_s{cfg["swarm_size"]}_w{cfg["w"]}_c1{cfg["c1"]}_c2{cfg["c2"]}'] = np.median(fitness_values)
                iteration_data[f'IQR_{func_name}_s{cfg["swarm_size"]}_w{cfg["w"]}_c1{cfg["c1"]}_c2{cfg["c2"]}'] = np.percentile(fitness_values, 75) - np.percentile(fitness_values, 25)

            iteration_results.append(iteration_data)

        df = pd.DataFrame(iteration_results)
        df.set_index('Iteración', inplace=True)

        df.to_excel(writer, sheet_name=func_name)

print(f"Archivo guardado en: {output_path}")
