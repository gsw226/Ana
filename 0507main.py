# class Hello:
#     def func(self):
#         print("Hello World!")

# a = Hello()
# a.func()


# class Star:
#     def printstar(self):
#         for i in range(1,11):
#             for j in range(i):
#                 print("*",end="")
#             print()


# s = Star()
# s.printstar()   

# class Member:
#     def __init__(self,name,size):
#         self.name = name
#         self.size = size
#     def member_me(self):
#         print(f"제 이름은 {self.name}입니다.")
#         print(f"제 사이즈는 {self.size}입니다.")

# a = Member("돌재준", 3)
# a.member_me()


# class Member:
#     def __init__(self,name,size,home):
#         self.name = name
#         self.size = size
#         self.home = home
#     def member_me(self):
#         print(f"제 이름은 {self.name}입니다.")
#         print(f"제 사이즈는 {self.size}입니다.")
#         print(f"제 고향은 {self.home}입니다.")

# a = Member("돌재준", 3, "켈리포니아")
# a.member_me()

class Bakery:
    def __init__(self, name,stock):
        self.name = name
        self.stock = stock

    def buy(self):
        if self.stock <= 0:
            print(f"{self.name}재고 없어")
        else:
            print(f"{self.name}구매 감사")
            self.stock -= 1

    def bake(self):
        print(f"{self.name}굽기 완료")
        self.stock += 1

class Bun(Bakery):
    def __init__(self, name, stock, inside):
        super().__init__(name,stock)
        self.inside = inside

    def buy(self, num):
        super().buy()

    def bake(self, stock):
        print("실패")



d=Bakery("도넛", 5)
d.bake(5)
for i in range(5):
    d.buy()

b = Bun("소보로", 5,"앙금")
b.bake(5)
for i in range(5):
    b.buy()
