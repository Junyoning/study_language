#문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)



#슬라이싱
jumin = "001127-3123456"

print("성별: " + jumin[7])
print("연: " + jumin[0:2]) # 0부터 2 직전까지 (0 ~ 1)
print("월: " + jumin[2:4])
print("일: " + jumin[4:6])

print("생년월일: " + jumin[0:6]) # jumin[0:6] 대신 jumin[:6] 가능, 처음부터 6 직전까지
print("뒤 7자리: " + jumin[7:14]) # jumin[7:], 7부터 끝까지
print("뒤 7자리 (뒤에부터): " + jumin[~7:])
# 맨 뒤에서 7번째부터 끝까지



#문자열 처리 함수
python = "Python is Amazing"
print(python.lower()) #소문자로 바꾸기
print(python.upper()) #대문자로 바꾸기
print(python[0].isupper()) #첫 번째 문자 대문자 여부 확인
print(len(python)) #문자열 길이 측정
print(python.replace("Python", "Java")) # 파이썬을 자바로 바꿈

index = python.index("n")
print(index) 
print(python.find("n")) #첫 번째 n의 위치 확인

index = python.index("n", index + 1)
print(index) #두 번째 n의 위치 확인

print(python.find("Java")) #-1 출력
#print(python.index("Java")) #에러 출력

print(python.count("n")) #n개수



#문자열 포맷
print("a" + "b") #ab
print("a", "b") #a b

print("나는 %d살입니다." % 20) #정수
print("나는 %s을 좋아해요." % "파이썬") #문자열 string
print("Apple은 %c로 시작해요." % "A") #한 글자 charater

print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨간"))

print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 25, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 25))

age = 24
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")



#탈출 문자
print("백문이 불여일견\n백견이 불여일타")

print("저는 \"준현\"입니다.") # \", \': 문장 내에서 따옴표 역할

print("c:\\Users\\dean1\\Desktop\\") # \\: 문장 내에서 \ 역할

print("Red Apple\rPine") # \r: 커서를 맨 앞으로 이동

print("Redd\bApple") # \b: 백스페이스(한 글자 삭제)

print("Red\tApple") # \t: 탭 키와 같은 역할


#############################################################################################


# QUIZ) 사이트 별로 비밀번호를 만들어 주는 프로그램을 작성하시오.
# 예)http://naver.com

# 규칙1: http:// 부분은 제외 ==> naver.com
# 규칙2: 처음 만나는 점(.) 이후 부분은 제외
# 규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

# 예) nav51!

#--------------내 오답-----------------------------------------

# site = "http://naver.com"

# site_name = site[7:12]
# print(site_name)

# name_len = str(len(site_name))
# e_num = str(site_name.find("e"))

# print(site_name.replace(("e", name_len), ("r", e_num))!)

#---------------------------------------------------------------

url = "http://naver.com"

my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(url, password))