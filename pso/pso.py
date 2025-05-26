import random

def pso(
    objective_function,
    dimensions,
    bounds,
    num_particles=30,
    iterations=100,
    w=0.5,
    c1=1.5,
    c2=1.5
):

    particles = []
    velocities = []
    personal_best = []
    personal_best_value = []

    global_best = None
    global_best_value = float('inf')
    history = []

    for _ in range(num_particles):
        position = [random.uniform(bounds[0], bounds[1]) for _ in range(dimensions)]
        velocity = [random.uniform(-1, 1) for _ in range(dimensions)]
        value = objective_function(position)

        particles.append(position)
        velocities.append(velocity)
        personal_best.append(position[:])
        personal_best_value.append(value)

        if value < global_best_value:
            global_best = position[:]
            global_best_value = value

    for _ in range(iterations):
        for i in range(num_particles):
            for d in range(dimensions):
                r1 = random.random()
                r2 = random.random()
                velocities[i][d] = (
                    w * velocities[i][d]
                    + c1 * r1 * (personal_best[i][d] - particles[i][d])
                    + c2 * r2 * (global_best[d] - particles[i][d])
                )
                particles[i][d] += velocities[i][d]

                particles[i][d] = max(bounds[0], min(particles[i][d], bounds[1]))

            value = objective_function(particles[i])

            if value < personal_best_value[i]:
                personal_best[i] = particles[i][:]
                personal_best_value[i] = value

                if value < global_best_value:
                    global_best = particles[i][:]
                    global_best_value = value

        history.append(global_best_value)

    return global_best, global_best_value, history