# DOSYA 2: astar_acil.py
import heapq

def a_star_acil():
    """
    A* Arama Algoritması Uygulaması
    Başlangıç: 'S', Hedef: 'H'
    """
    # Graf tanımı (Düğümler ve komşuları ile aralarındaki mesafe/maliyet)
    graph = {
        'S': {'A': 2, 'B': 4},
        'A': {'S': 2, 'C': 2, 'D': 5},
        'B': {'S': 4, 'D': 1, 'E': 7},
        'C': {'A': 2, 'D': 2, 'F': 4},
        'D': {'A': 5, 'B': 1, 'C': 2, 'E': 2, 'F': 3, 'H': 7},
        'E': {'B': 7, 'D': 2, 'H': 3},
        'F': {'C': 4, 'D': 3, 'H': 4},
        'H': {'D': 7, 'E': 3, 'F': 4}
    }
    
    # Sezgisel değerler (h)
    heuristics = {
        'S': 9, 'A': 8, 'B': 5, 'C': 6, 'D': 4, 'E': 2, 'F': 3, 'H': 0
    }
    
    start = 'S'
    goal = 'H'
    
    # Priority Queue yapısı: (f_degeri, g_degeri, dugum_adi, yol)
    # Tie-breaking kuralı: f değerleri eşitse heapq 2. elemana (g_degeri) bakar, 
    # küçük g değeri tercih edilir. Eğer f ve g eşitse, 3. elemana (dugum_adi) 
    # bakarak alfabetik sıralamaya göre seçim yapar.
    g_start = 0
    f_start = g_start + heuristics[start]
    pq = [(f_start, g_start, start, [start])]
    
    # Sonsuz döngüleri önlemek için ziyareti tamamlanmış (genişletilmiş) düğümler kümesi
    visited = set()
    
    print("--- A*: Düğüm Genişletme Sırası ---")
    
    while pq:
        # Kuyruktan en düşük f değerine sahip düğümün çıkarılması (genişletilmesi)
        f_val, g_val, current_node, path = heapq.heappop(pq)
        
        # Eğer düğüm kapatıldıysa (visited listesinde varsa), tekrar işleme alma
        if current_node in visited:
            continue
            
        # Ziyaret edildi (kalıcı liste) olarak işaretle
        visited.add(current_node)
        current_h = heuristics[current_node]
        print(f"Genişletilen: {current_node} (f: {f_val}, g: {g_val}, h: {current_h})")
        
        # Hedef kontrolü sadece düğüm kuyruktan değerlendirilmek üzere çıkarıldığında yapılır
        if current_node == goal:
            print("\n--- Çözüm Bulundu ---")
            print(f"En İyi Yol: {' -> '.join(path)}")
            print(f"Toplam Maliyet: {g_val}")
            return
            
        # Mevcut düğümün komşularını genişlet
        for neighbor, weight in graph.get(current_node, {}).items():
            if neighbor not in visited:
                new_g = g_val + weight
                new_f = new_g + heuristics[neighbor]
                new_path = path + [neighbor]
                # Kuyruğa tie-breaking kurallarını destekleyen yapıda veri ekle
                heapq.heappush(pq, (new_f, new_g, neighbor, new_path))
                
    print("Hedefe ulaşılamadı!")

if __name__ == "__main__":
    a_star_acil()
