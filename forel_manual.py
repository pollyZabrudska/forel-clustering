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
        # обираємо випадкову точку
        start_idx = random.choice(unused) 
        center = points[start_idx][:]
        
        # шукаємо стабільний центр
        for i in range(100):
            nearby = []
            for j in range(len(points)):
                if distance(points[j], center) <= rho:
                    nearby.append(points[j])
            
            new_center = get_center(nearby)
            if distance(center, new_center) < 0.001:
                break
            center = new_center
        
        # формуємо кластер з невикористаних точок
        cluster = []
        for i in unused[:]:
            if distance(points[i], center) <= rho:
                cluster.append(i)
                unused.remove(i)
        
        clusters.append(cluster)
        centers.append(center)
    
    return clusters, centers

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