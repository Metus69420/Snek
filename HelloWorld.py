""""# An empty loop
a = 'geeksforgeeks'
i = 0

while i < len(a):
    i += 1
    pass

print('Value of i :', i)

calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"

print(calc(20))

dic = {"a": "b", "c": "d"}
print(dic.values())
print(10/2)


bool = bool()
print(bool)
"python"

import sys
a_list = []
a_tuple = ()
a_list = ["Geeks", "For", "Geeks"]
print(a_list.clear())


dic = {"a": "b", "c": "d"}
dic["a"] = "ab"
print(dic)
tuple = 1, 2
print(tuple)
tuple[1] = 2
# 슬라이싱
string_list = ["a", "b", "c", "d"]
number_list = [1, 2, 3, 4]

# 인덱싱
print(string_list[0]) # a
print(number_list[2]) # 3

print(string_list[2:]) # ['a', 'b']
print(string_list[0:2] + string_list[2:4])
print(number_list[0:3]) # [2, 3]
#print(number_list.index(777))
nl = []
nl.append(0)
print(nl)


print(~6)
a=1
b=3.14
print(a+b)
print(b:0.1f)
b = "a" in "applea"
print(b)
print("hello world?"); print("Nah")
a = 1.23
print(type(a))
name = "b"
print(name)
print(f"Hi, {name}")
a, b = 1, "a"
print(a, b)



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
    beverages.values("식혜")""
    beverages = {
    "사이다": 1700,
    "콜라": 1900,
    "식혜": 2500,
    "솔의눈": 3000
}
for key, value in beverages.items():
    print(key)

user_choice = input("음료를 선택해주세요")

coin = input("금액을 입력해주세요")
print(coin)
print(type(coin))

coin = int(coin)
print(coin)
print(type(coin))
print(beverages['콜라'])
print(beverages['사이다'])
print(beverages['식혜'])

print(beverages[user_choice])

if coin < beverages[user_choice]:
    # 실행 종료하기
    print("돈이 부족합니다")
else:
    remain = coin - beverages[user_choice]
    print(remain)
# 돈이 충분할 경우"""

#GPT의 도움
def solution(answers):
    # 수포자들의 패턴 정의
    patterns = [
        [1, 2, 3, 4, 5],  # 수포자 1
        [2, 1, 2, 3, 2, 4, 2, 5],  # 수포자 2
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 수포자 3
    ]

    scores = [0, 0, 0]  # 각 수포자가 맞힌 문제 수를 저장할 리스트

    # 각 수포자의 패턴을 반복하면서 맞춘 문제 개수 계산
    for i, pattern in enumerate(patterns):
        # 패턴을 반복하면서 answers와 비교
        for j, answer in enumerate(answers):
            if answer == pattern[j]:
                scores[i] += 1

    # 가장 많이 맞힌 문제 개수 구하기
    max_score = max(scores)

    # 가장 많은 점수를 맞힌 수포자들의 번호를 찾기
    result = [i + 1 for i, score in enumerate(scores) if score == max_score]

    return result
print(solution([1,2,3,4,5]))