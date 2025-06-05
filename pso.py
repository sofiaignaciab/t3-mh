import numpy as np

def pso(function, bounds, swarm_size=30, w=0.7, c1=1.5, c2=1.5, max_generations=100):
    dim = len(bounds)

    positions = np.random.rand(swarm_size, dim)
    velocities = np.zeros((swarm_size, dim))

    for d in range(dim):
        lo, hi = bounds[d]
        positions[:, d] = lo + positions[:, d] * (hi - lo)
        v_range = hi - lo
        velocities[:, d] = (np.random.rand(swarm_size) * 2 - 1) * 0.1 * v_range

    fitness = np.apply_along_axis(function, 1, positions)

    pbest_pos = positions.copy()
    pbest_val = fitness.copy()

    gbest_idx = np.argmin(pbest_val)
    gbest_pos = pbest_pos[gbest_idx].copy()
    gbest_val = pbest_val[gbest_idx]

    convergence = [gbest_val]

    for gen in range(1, max_generations + 1):
       
        for i in range(swarm_size):
       
            r1 = np.random.rand(dim)
            r2 = np.random.rand(dim)
            velocities[i] = (
                w * velocities[i]
                + c1 * r1 * (pbest_pos[i] - positions[i])
                + c2 * r2 * (gbest_pos - positions[i])
            )

            positions[i] = positions[i] + velocities[i]

            for d in range(dim):
                lo, hi = bounds[d]
                if positions[i, d] < lo:
                    positions[i, d] = lo
                    velocities[i, d] = 0.0
                elif positions[i, d] > hi:
                    positions[i, d] = hi
                    velocities[i, d] = 0.0

            fval = function(positions[i])

            if fval < pbest_val[i]:
                pbest_val[i] = fval
                pbest_pos[i] = positions[i].copy()

                if fval < gbest_val:
                    gbest_val = fval
                    gbest_pos = positions[i].copy()

        convergence.append(gbest_val)

    return gbest_pos, gbest_val, convergence