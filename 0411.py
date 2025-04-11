# def makeFishShapeBun(taste):
#     print(f"{taste}맛 붕어빵 완성!")
#     print("맛있게 드세요!")

# makeFishShapeBun("슈크림")

# x = 10

# def example():
#     x = 20
#     print(x)

# example()
# print(x)

# def for10(a):
#     for i in range(10):
#         print(a)

# for10("Hello World")

def sort(a, b, c):
    if a>b:
        if a>c:
            if b>c:
                return c, b, a
            else:
                return b, c, a
        else:
            return b, a, c
    else:
        if b>c:
            if a>c:
                return c, a, b
            else:
                return a, c, b
        else:
            return a, b, c

print(sort(3,1,2))
print(sort(123,123123,123123123))
