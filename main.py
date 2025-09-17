import numpy as np
import time

def main():
    print("Тестування алгоритму Форел")
    print("-" * 30)
    
    # генеруємо дані один раз
    np.random.seed(42)
    data = np.random.rand(30, 2) * 10
    rho = 2.5
    
    # оригінальна numpy версія
    from forel import forel
    
    clusters, centers = forel(data, rho, random_state=42)
    
    print("NumPy версія:")
    print(f"Знайдено кластерів: {len(clusters)}")
    for i, (cl, c) in enumerate(zip(clusters, centers)):
        print(f"  {i+1}: {len(cl)} точок, центр ({c[0]:.2f}, {c[1]:.2f})")
    
    print()
    
    # ручна версія
    from forel_manual import forel_manual
    
    data_list = data.tolist()
    clusters2, centers2 = forel_manual(data_list, rho, seed=42)
    
    print("Ручна версія:")
    print(f"Знайдено кластерів: {len(clusters2)}")
    for i, (cl, c) in enumerate(zip(clusters2, centers2)):
        print(f"  {i+1}: {len(cl)} точок, центр ({c[0]:.2f}, {c[1]:.2f})")
    
    print()
    
    # порівняння швидкості
    print("Тест швидкості:")
    
    start = time.time()
    forel(data, rho, random_state=42)
    time1 = time.time() - start
    
    start = time.time()
    forel_manual(data_list, rho, seed=42)
    time2 = time.time() - start
    
    print(f"NumPy: {time1:.4f} сек")
    print(f"Ручна: {time2:.4f} сек")
    if time1 > time2:
        print(f"Ручна версія швидша в {time1/time2:.1f} разів")
    else:
        print(f"NumPy версія швидша в {time2/time1:.1f} разів")
    
    # малюємо якщо можна
    try:
        from plot_results import plot_clusters, compare_versions
        print("\nПоказуємо графіки...")
        plot_clusters(data, clusters, centers, rho)
        compare_versions(data, rho)
    except ImportError:
        print("\nMatplotlib недоступний для візуалізації")

if __name__ == "__main__":
    main()