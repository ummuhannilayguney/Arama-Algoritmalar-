# DOSYA 1: ucs_kurye.py
import heapq

def ucs_kurye():
    """
    Uniform Cost Search (Tekdüze Maliyetli Arama) Algoritması Uygulaması
    Başlangıç: 'A', Hedef: 'F'
    """
    # Graf tanımı (Düğümler ve komşuları ile aralarındaki mesafe/maliyet)
    graph = {
        'A': {'B': 2, 'C': 5, 'D': 1},
        'B': {'A': 2, 'C': 2, 'E': 4},
        'C': {'A': 5, 'B': 2, 'D': 2, 'F': 7},
        'D': {'A': 1, 'C': 2, 'E': 3, 'F': 12},
        'E': {'B': 4, 'D': 3, 'F': 5},
        'F': {'C': 7, 'D': 12, 'E': 5}
    }
    
    start = 'A'
    goal = 'F'
    
    # Priority Queue yapısı: (maliyet (g), düğüm_adı, yol)
    # Python heapq tuple elemanlarını soldan sağa karşılaştırır.
    # Tie-breaking: Maliyetler eşitse heapq doğal olarak 2. elemana (düğüm adına) 
    # bakarak alfabetik sıralamaya göre seçim yapar.
    pq = [(0, start, [start])]
    
    # Sonsuz döngüleri önlemek için ziyareti tamamlanmış (genişletilmiş) düğümler kümesi
    visited = set()
    
    print("--- UCS: Düğüm Genişletme Sırası ---")
    
    while pq:
        # Kuyruktan en düşük maliyetli düğümün çıkarılması (genişletme sırası)
        cost, current_node, path = heapq.heappop(pq)
        
        # Eğer düğüm daha önce genişletilmiş ise tekrar işlememek için atlanır
        if current_node in visited:
            continue
            
        # Düğüm çıkarıldıktan sonra ziyaret edilenlere eklenir
        visited.add(current_node)
        print(f"Genişletilen: {current_node} (Maliyet: {cost})")
        
        # Hedef kontrolü kuyruğa eklenirken değil, kuyruktan çıkarılırken yapılır
        if current_node == goal:
            print("\n--- Çözüm Bulundu ---")
            print(f"En Düşük Maliyetli Yol: {' -> '.join(path)}")
            print(f"Toplam Maliyet: {cost}")
            return
            
        # Komşu düğümlerin incelenmesi ve kuyruğa eklenmesi
        for neighbor, weight in graph.get(current_node, {}).items():
            if neighbor not in visited:
                new_cost = cost + weight
                new_path = path + [neighbor]
                heapq.heappush(pq, (new_cost, neighbor, new_path))
                
    print("Hedefe ulaşılamadı!")

if __name__ == "__main__":
    ucs_kurye()
