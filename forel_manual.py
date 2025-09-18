import random
import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def get_center(points):
    if not points:
        return [0, 0]
    x = sum(p[0] for p in points) / len(points)
    y = sum(p[1] for p in points) / len(points)
    return [x, y]

def forel_manual(points, rho, seed=42):
    random.seed(seed)
    
    unused = list(range(len(points)))
    clusters = []
    centers = []
    
    while unused:
        # обираємо випадкову точку з невикористаних
        start_idx = random.choice(unused) 
        center = points[start_idx][:]
        
        # шукаємо стабільний центр
        for iteration in range(100):  # максимум 100 ітерацій
            nearby = []
            
            # шукаємо точки тільки серед невикористаних
            for j in unused:
                if distance(points[j], center) <= rho:
                    nearby.append(points[j])
            
            if not nearby:
                break
                
            new_center = get_center(nearby)
            
            # перевіряємо чи центр стабілізувався
            if distance(center, new_center) < 0.001:
                break
            center = new_center
        
        # формуємо кластер - знаходимо індекси точок біля фінального центру
        cluster = []
        for i in unused[:]:  # копіюємо список для послідуючого безпечного видалення
            if distance(points[i], center) <= rho:
                cluster.append(i)
                unused.remove(i)
        
        if cluster:
            clusters.append(cluster)
            centers.append(center)
    
    return clusters, centers

# тестові дані
if __name__ == "__main__":
    test_data = [
        [1, 1], [1.2, 1.1], [2, 2], 
        [8, 8], [8.1, 7.9], [9, 9],
        [3, 8], [3.5, 8.2]
    ]
    
    clusters, centers = forel_manual(test_data, 2.0)
    
    print(f"Знайдено {len(clusters)} кластерів:")
    for i, (cl, c) in enumerate(zip(clusters, centers)):
        print(f"Кластер {i+1}: точки {cl}, центр ({c[0]:.2f}, {c[1]:.2f})")
    
    # перевіряємо чи всі точки враховані
    total_points = sum(len(cluster) for cluster in clusters)
    print(f"Всього точок у кластерах: {total_points} (має бути {len(test_data)})")