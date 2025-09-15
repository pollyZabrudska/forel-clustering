import numpy as np
from forel import forel

if __name__ == "__main__":
    np.random.seed(42)
    T = np.random.rand(30, 2) * 10

    rho = 2.5

    clusters, centers = forel(T, rho, random_state=42)

    print("Кількість кластерів:", len(clusters))
    for i, (cl, c) in enumerate(zip(clusters, centers), 1):
        print(f"Кластер {i}: {cl}, центр = {c}")
