import numpy as np
import random

def forel(T: np.ndarray, rho: float, random_state: int = None):
    
    if random_state is not None:
        random.seed(random_state)
    
    U = set(range(len(T)))
    clusters = []
    centers = []

    while U:
        # Вибір випадкової точки з U - використовуємо random.choice
        t0_idx = random.choice(list(U))
        t0 = T[t0_idx].copy()

        while True:
            # Формування кластера C0 = {ti | d(ti, t0) ≤ ρ}
            distances = np.linalg.norm(T - t0, axis=1)
            C0_idx = np.where(distances <= rho)[0]

            # Новий центр – середнє значення точок кластера
            new_t0 = T[C0_idx].mean(axis=0)

            if np.allclose(new_t0, t0, atol=1e-3):
                break
            t0 = new_t0

        # Зберігання кластера та оновлення U
        clusters.append(C0_idx)
        centers.append(t0)
        U -= set(C0_idx)

    return clusters, centers