from main import results_pso
import numpy as np
import pandas as pd

summary_records = []
for entry in results_pso:
    summary_records.append({
        'Función': entry['function'],
        'SwarmSize': entry['swarm_size'],
        'w': entry['w'],
        'c1': entry['c1'],
        'c2': entry['c2'],
        'Media_Mejor': np.mean(entry['best_values']),
        'Std_Mejor': np.std(entry['best_values'])
    })

df_summary = pd.DataFrame(summary_records)
print("\n=== Resumen de Resultados PSO (Media ± Desviación) ===")
print(df_summary.to_string(index=False))