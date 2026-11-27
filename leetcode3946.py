from typing import List
import ast
items = ast.literal_eval(input().strip())
budget = int(input())
def maximumSaleItems(items: List[List[int]], budget: int) -> int:
        n = len(items)
        
        # Bước 1: Tính giá trị nhận được khi mua bản sao đầu tiên của từng món
        first_buy_value = [1] * n
        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    first_buy_value[i] += 1
                    
        # Bước 2: 0/1 Knapsack cho lần mua đầu tiên của mỗi loại mặt hàng
        # dp[c] = số lượng món tối đa khi chi đúng c đồng cho các lần mua đầu
        dp = [-1] * (budget + 1)
        dp[0] = 0
        
        for i in range(n):
            price = items[i][1]
            val = first_buy_value[i]
            if price > budget:
                continue
            for c in range(budget, price - 1, -1):
                if dp[c - price] != -1:
                    dp[c] = max(dp[c], dp[c - price] + val)
                    
        # Bước 3: Dùng số tiền dư còn lại mua thêm mặt hàng rẻ nhất
        min_price = min(item[1] for item in items)
        ans = 0
        for c in range(budget + 1):
            if dp[c] != -1:
                extra_items = (budget - c) // min_price
                ans = max(ans, dp[c] + extra_items)
                
        return ans

print(maximumSaleItems(items,budget))