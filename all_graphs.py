import matplotlib.pyplot as plt
import pandas as pd

output_path = 'pso_iterations_results_separated.xlsx'

df_f1 = pd.read_excel(output_path, sheet_name='f1')
df_f2 = pd.read_excel(output_path, sheet_name='f2')
df_f3 = pd.read_excel(output_path, sheet_name='f3')
df_f4 = pd.read_excel(output_path, sheet_name='f4')

def plot_iteration_results(df, func_name):
    iteration = df.index
    for column in df.columns:
        if "Media_Mejor" in column:
            plt.plot(iteration, df[column], label=column)

    plt.title(f"Fitness por Iteración para {func_name}")
    plt.xlabel("Iteración")
    plt.ylabel("Media del Mejor Fitness")
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=8)
    plt.grid(True)
    plt.tight_layout()
    plt.gcf().set_size_inches(10, 6) 
    plt.show()

plot_iteration_results(df_f1, "f1")
plot_iteration_results(df_f2, "f2")
plot_iteration_results(df_f3, "f3")
plot_iteration_results(df_f4, "f4")
