# tp = ("사과","바나나", "체리")

# apple, banana, cherry = tp
# print(apple)
# print(banana)
# print(cherry)


# def two(a,b,c):
#     return (a*b,b*c)


# ab,bc = two(1,2,3)
# print(ab)
# print(bc)

tp = ("사과","바나나", "체리")
try:
    a = 2 / 0
    tp[0] = "포도"
except TypeError as e:
    print("오류1: ", e)
except ZeroDivisionError as e:
    print("오류2", e)
finally:
    print("예외 처리 완료!")
