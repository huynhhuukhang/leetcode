from typing import List

parent=list(map(int,input().split()))
s=input()
def findSubtreeSizes( parent: List[int], s: str) -> List[int]:
        n = len(parent)
        
        # 1. Dựng cây ban đầu
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        new_parent = list(parent)
        # Lưu các tổ tiên theo từng ký tự 'a' -> 'z'
        last_seen = {chr(c): [] for c in range(ord('a'), ord('z') + 1)}
        
        # DFS lần 1: Xác định cha mới dựa trên tổ tiên gần nhất cùng ký tự
        def dfs_find_parent(u: int):
            char = s[u]
            if last_seen[char]:
                new_parent[u] = last_seen[char][-1]
                
            last_seen[char].append(u)
            for v in adj[u]:
                dfs_find_parent(v)
            last_seen[char].pop()  # Quay lui (backtrack)
            
        dfs_find_parent(0)
        
        # 2. Dựng cây mới từ new_parent
        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)
            
        ans = [1] * n
        
        # DFS lần 2: Tính kích thước từng cây con
        def dfs_size(u: int) -> int:
            total = 1
            for v in new_adj[u]:
                total += dfs_size(v)
            ans[u] = total
            return total
            
        dfs_size(0)
        return ans


print(findSubtreeSizes(parent,s))