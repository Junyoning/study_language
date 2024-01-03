#숫자 자료형
print(5)
print(-10)
print(3.14)
print(1000)

#문자 자료형
print('풍선')
print("풍선")
print("ㅋ"*9)

#참 / 거짓
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not(5 > 10))

#변수
name = "연탄이"
animal = "강아지"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리 집" + animal + "의 이름은 연탄이예요")
print(name + "는" + str(age) + "이며 " + hobby + "을 아주 좋아해요")
print(name + "은 어른일까요?", str(is_adult))
# print(name, "는", age, "이며 ", hobby, "을 아주 좋아해요")
# print(name, "는 어른일까요?", is_adult)

# Quiz) 변수를 이용하여 문장 출력
# 변수명: station
# 변수값: 사당, 신도림, 인천공항 순서
# XX행 열차가 돌아오고 있습니다.

station = "사당"
print(station, "행 열차가 들어오고 있습니다.")

station = "신도림"
print(station, "행 열차가 들어오고 있습니다.")

station = "인천공항"
print(station, "행 열차가 들어오고 있습니다.")