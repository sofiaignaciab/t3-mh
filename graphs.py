import matplotlib.pyplot as plt
from main import results_pso

def plot_convergence(func_name: str, cropped: bool):
    xlim_map = {
        'f1': (0, 5),
        'f2': (0, 5),
        'f3': (0, 5),
        'f4': (0, 25)
    }

    example = next(
        item for item in results_pso
        if item['function'] == func_name
           and item['swarm_size'] == 20
           and item['w'] == 0.7
           and item['c1'] == 1.5
           and item['c2'] == 1.5
    )

    plt.figure(figsize=(8, 5))
    for conv_curve in example['convergence']:
        plt.plot(conv_curve, alpha=0.6)

    if cropped:
        lo, hi = xlim_map[func_name]
        plt.xlim(lo, hi)

    plt.title(f"Convergencia para {func_name} ")
    plt.xlabel("Generación")
    plt.ylabel("Mejor Fitness")
    plt.grid(True)
    plt.show()


def main():
    func_map = {
        '1': 'f1',
        '2': 'f2',
        '3': 'f3',
        '4': 'f4',
        '5': None 
    }

    while True:
        print("\n¿Qué gráfico quieres ver?")
        print("1. f1")
        print("2. f2")
        print("3. f3")
        print("4. f4")
        print("5. Salir")
        choice = input("Ingresa el número de la función (1-5): ").strip()

        if choice not in func_map:
            print("Opción inválida. Intenta de nuevo.")
            continue

        if choice == '5':
            print("Saliendo. ¡Hasta luego!")
            break

        func_name = func_map[choice]

        print("\n¿Quieres ver la versión recortada?")
        print("1. Sí")
        print("2. No")
        crop_choice = input("Ingresa 1 para 'Sí' o 2 para 'No': ").strip()

        if crop_choice == '1':
            cropped = True
        elif crop_choice == '2':
            cropped = False
        else:
            print("Opción inválida para recorte. Se mostrará sin recorte.")
            cropped = False

        plot_convergence(func_name, cropped)


if __name__ == "__main__":
    main()
