items = {
    "사과": {
        "type": "과일",
        "description": "사과는 맛있고 건강에 좋습니다.",
        "price": 2000,
    },
    "바나나": {
        "type": "과일",
        "description": "바나나는 에너지를 줍니다.",
        "price": 1500,
    },
    "체리": {
        "type": "과일",
        "description": "체리는 비타민이 풍부합니다.",
        "price": 3000,
    }
}

for i in items.keys():
    item = items[i]
    print(f"{i}({item['type']}): {item['price']}원")
    print(f"ㄴ {item['description']}")
    print()

