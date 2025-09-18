import numpy as np
import random

def forel(T, rho, random_state=None):
    
    if random_state is not None:
        np.random.seed(random_state)
        random.seed(random_state)
    
    # множина некластеризованих точок
    U = set(range(len(T)))
    clusters = []
    centers = []

    while U:
        # випадковий вибір точки з невикористаних
        t0_idx = random.choice(list(U))
        t0 = T[t0_idx].copy()

        # шукаємо стабільний центр
        while True:
            # відстані до невикористаних точок
            U_list = list(U)
            distances = np.linalg.norm(T[U_list] - t0, axis=1)
            nearby_mask = distances <= rho
            C0_idx = np.array(U_list)[nearby_mask]

            if len(C0_idx) == 0:
                break

            # новий центр
            new_t0 = T[C0_idx].mean(axis=0)

            # перевіряємо збіжності
            if np.allclose(new_t0, t0, atol=1e-3):
                break
            t0 = new_t0

        # зберігаємо кластер і видаляємо точки з U
        clusters.append(C0_idx)
        centers.append(t0)
        U -= set(C0_idx)

    return clusters, centers