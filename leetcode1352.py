class ProductOfNumbers:
    def __init__(self):
        self.prefix=[1]

    def add(self,num:int)->None:
        if num==0:
            self.prefix=[1]
        else:
            self.prefix.append(self.prefix[-1]*num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-1 - k]


if __name__== "__main__":
    obj = ProductOfNumbers()
    obj.add(3)                    # [3]
    obj.add(0)                    # [3, 0] -> reset
    obj.add(2)                    # [2]
    obj.add(5)                    # [2, 5]
    obj.add(4)                    # [2, 5, 4]
    
    print(obj.getProduct(2))      # 5 * 4 = 20
    print(obj.getProduct(3))      # 2 * 5 * 4 = 40
    print(obj.getProduct(4))      # 0 * 2 * 5 * 4 = 0
    
    obj.add(8)                    # [2, 5, 4, 8]
    print(obj.getProduct(2))