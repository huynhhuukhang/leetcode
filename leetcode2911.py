
s=input()
k=int(input())
def minimumChanges(s: str, k: int) -> int:
        n = len(s)
        
        # Tiền xử lý danh sách các ước thực sự (1 <= d < L) cho mọi độ dài L từ 2 đến n
        divisors = [[] for _ in range(n + 1)]
        for length in range(2, n + 1):
            for d in range(1, length // 2 + 1):
                if length % d == 0:
                    divisors[length].append(d)
                    
        # Giai đoạn 1: Tính cost[i][j] cho mọi đoạn s[i..j]
        INF = float('inf')
        cost = [[INF] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                min_changes = INF
                
                for d in divisors[length]:
                    changes = 0
                    # Kiểm tra từng nhóm đồng dư mod d
                    for r in range(d):
                        left = i + r
                        right = j - (d - 1 - r)
                        while left < right:
                            if s[left] != s[right]:
                                changes += 1
                            left += d
                            right -= d
                    if changes < min_changes:
                        min_changes = changes
                        
                cost[i][j] = min_changes

        # Giai đoạn 2: Quy hoạch động chia k đoạn
        # dp[p][j]: chi phí nhỏ nhất chia j ký tự đầu tiên thành p đoạn
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        
        for p in range(1, k + 1):
            # Mỗi đoạn dài tối thiểu 2 nên p đoạn cần ít nhất 2*p ký tự
            for j in range(2 * p, n + 1):
                for i in range(2 * (p - 1), j - 1):
                    if dp[p - 1][i] + cost[i][j - 1] < dp[p][j]:
                        dp[p][j] = dp[p - 1][i] + cost[i][j - 1]
                        
        return dp[k][n]


print(minimumChanges(s,k))