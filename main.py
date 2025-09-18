import numpy as np
import time

def check_results(clusters, data_size, version):
    total = sum(len(cluster) for cluster in clusters)
    print(f"{version}: {len(clusters)} кластерів, {total} точок")
    if total != data_size:
        print(f"Помилка: має бути {data_size} точок!")
        return False
    return True

def main():
    print("Тестування алгоритму Форел")
    print("-" * 40)
    
    # дані для тестування
    np.random.seed(42)
    data = np.random.rand(30, 2) * 10
    rho = 2.5
    
    print(f"Тестові дані: {len(data)} точок, радіус ρ = {rho}")
    print()
    
    # numpy версія
    from forel import forel
    
    start = time.time()
    clusters1, centers1 = forel(data, rho, random_state=42)
    time1 = time.time() - start
    
    print("NumPy версія:")
    check1 = check_results(clusters1, len(data), "")
    for i, (cl, c) in enumerate(zip(clusters1, centers1)):
        print(f"  Кластер {i+1}: {len(cl)} точок, центр ({c[0]:.2f}, {c[1]:.2f})")
    
    print()
    
    # ручна версія
    from forel_manual import forel_manual
    
    data_list = data.tolist()
    start = time.time()
    clusters2, centers2 = forel_manual(data_list, rho, seed=42)
    time2 = time.time() - start
    
    print("Ручна версія:")
    check2 = check_results(clusters2, len(data), "")
    for i, (cl, c) in enumerate(zip(clusters2, centers2)):
        print(f"  Кластер {i+1}: {len(cl)} точок, центр ({c[0]:.2f}, {c[1]:.2f})")
    
    print()
    
    # перевірка правильності
    if check1 and check2:
        print("Обидві версії працюють коректно!")
    else:
        print("Є помилки в реалізації")
    
    # швидкість
    print("\nЧас виконання:")
    print(f"NumPy: {time1:.5f} сек")
    print(f"Ручна: {time2:.5f} сек")
    if time2 < time1:
        print(f"Ручна швидша в {time1/time2:.1f} рази")
    else:
        print(f"NumPy швидша в {time2/time1:.1f} рази")
    
    # графіки
    try:
        from plot_results import plot_clusters, compare_versions
        print("\nВідображення графіків...")
        plot_clusters(data, clusters1, centers1, rho)
        compare_versions(data, rho)
    except ImportError:
        print("\nMatplotlib не встановлено - графіки недоступні")

if __name__ == "__main__":
    main()