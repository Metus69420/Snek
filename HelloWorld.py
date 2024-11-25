print("hello world?"); print("Nah")
a = 1.23
print(type(a))
name = "b"
print(name)
print(f"Hi, {name}")
a, b = 1, "a"
print(a, b)

"""

numbers2 = [10, 20, 30, 40, 50]
sum = 0
for number in numbers2:
    sum += number
print(sum)

numbers = [1, 2, 3, 4, 2, 2, 5, 2]
value_to_find = 2
count = 0
for number in numbers:
    if number == 2:
        count += 1
print(count)

f = 5
s = f
while f !=1:
    s *= f-1
    f -= 1
print(s)

import random

first_list = ["기철초풍", "멋있는", "재미있는"]
second_list = ["도전적인", "노란색의", "바보같은"]
third_list = ["돌고래", "개발자", "오랑우탄"]


def create_random_nickname():
    # 여기에 랜덤으로 닉네임을 만드는 코드를 적어주세요
    rn = first_list[random.randint(0,2)]
    rn += " " + second_list[random.randint(0,2)]
    rn += " " + third_list[random.randint(0,2)]

    return rn

my_nickname = create_random_nickname()
print(my_nickname)

beverages = {
		"사이다": 1700,
		"콜라": 1900,
		"식혜": 2500,
		"솔의눈": 3000
}

for key, value in beverages.items():
    print(key)
user_choice = input()
if user_choice in beverages.keys():
    consume = input("돈을 넣어주세요 ex)2000")
    beverages.values("식혜")"""""