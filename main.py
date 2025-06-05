import numpy as np
from functions import f1, f2, f3, f4
from pso import pso
import pandas as pd

param_configs_pso = [
    {'swarm_size': 20, 'w': 0.7, 'c1': 1.5, 'c2': 1.5},
    {'swarm_size': 50, 'w': 0.5, 'c1': 1.5, 'c2': 1.5},
    {'swarm_size': 50, 'w': 0.7, 'c1': 1.5, 'c2': 1.5},
    {'swarm_size': 20, 'w': 0.5, 'c1': 2.0, 'c2': 1.5},
]

functions = {
    'f1': (f1, [(-5, 5), (-5, 5)]),
    'f2': (f2, [(0, 1)] * 6),
    'f3': (f3, [(-500, 500)] * 2),
    'f4': (f4, [(-2.001, 10)] * 10)
}

results_pso = []

for func_name, (function, bounds) in functions.items():
    for cfg in param_configs_pso:
        convs = []
        best_vals = []
        for run in range(10):
            best_x, best_f, conv = pso(
                function,
                bounds,
                swarm_size=cfg['swarm_size'],
                w=cfg['w'],
                c1=cfg['c1'],
                c2=cfg['c2'],
                max_generations=200
            )
            convs.append(conv)
            best_vals.append(best_f)
        
        results_pso.append({
            'function': func_name,
            'swarm_size': cfg['swarm_size'],
            'w': cfg['w'],
            'c1': cfg['c1'],
            'c2': cfg['c2'],
            'best_values': best_vals,
            'convergence': convs
        })

df_pso = pd.DataFrame([
    {
        'Función': entry['function'],
        'SwarmSize': entry['swarm_size'],
        'w': entry['w'],
        'c1': entry['c1'],
        'c2': entry['c2'],
        'Media_Mejor': np.mean(entry['best_values']),
        'Std_Mejor': np.std(entry['best_values'])
    }
    for entry in results_pso
])
print(df_pso.to_string(index=False))
