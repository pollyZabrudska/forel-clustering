import matplotlib.pyplot as plt
import numpy as np

def plot_clusters(points, clusters, centers, rho):
    colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray']
    
    plt.figure(figsize=(10, 8))
    
    for i, cluster in enumerate(clusters):
        color = colors[i % len(colors)]
        
        # точки кластера
        if isinstance(points, np.ndarray):
            x = points[cluster, 0]
            y = points[cluster, 1]
        else:
            x = [points[j][0] for j in cluster]
            y = [points[j][1] for j in cluster]
        
        plt.scatter(x, y, c=color, s=60, alpha=0.7, label=f'Кластер {i+1}')
        
        # центр кластера
        plt.scatter(centers[i][0], centers[i][1], c='black', s=150, marker='*')
        
        # коло радіусу rho
        circle = plt.Circle((centers[i][0], centers[i][1]), rho, 
                           fill=False, color=color, linestyle='--', alpha=0.5)
        plt.gca().add_patch(circle)
    
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.title('Результати кластеризації Форел')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

def compare_versions(data=None, rho=2.5):
    if data is None:
        np.random.seed(42)
        data = np.random.rand(30, 2) * 10
    
    from forel import forel
    from forel_manual import forel_manual
    
    data_list = data.tolist()
    
    # обидві версії з однаковим seed
    clusters1, centers1 = forel(data, rho, random_state=42)
    clusters2, centers2 = forel_manual(data_list, rho, seed=42)
    
    plt.figure(figsize=(14, 6))
    colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray']
    
    # numpy версія
    plt.subplot(1, 2, 1)
    for i, cluster in enumerate(clusters1):
        color = colors[i % len(colors)]
        plt.scatter(data[cluster, 0], data[cluster, 1], c=color, s=50)
        plt.scatter(centers1[i][0], centers1[i][1], c='black', s=100, marker='*')
    plt.title(f'NumPy версія ({len(clusters1)} кластерів)')
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    
    # ручна версія
    plt.subplot(1, 2, 2)
    for i, cluster in enumerate(clusters2):
        color = colors[i % len(colors)]
        x = [data_list[j][0] for j in cluster]
        y = [data_list[j][1] for j in cluster]
        plt.scatter(x, y, c=color, s=50)
        plt.scatter(centers2[i][0], centers2[i][1], c='black', s=100, marker='*')
    plt.title(f'Ручна версія ({len(clusters2)} кластерів)')
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    compare_versions()