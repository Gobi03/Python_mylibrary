## 小さい順にソート
import heapq

pq = []
heapq.heappush(pq, 1) # 1をpush
heapq.heappush(pq, 2) # 2をpush

heapq.heappop(pq)

not pq  # 空判定

pq.clear() # reset
