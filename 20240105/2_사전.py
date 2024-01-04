# 키 선언(?)
cabinet = {1:"안준현", 2:"안현진"}
print(cabinet[1])
print(cabinet[2])
print("\n")

# 키 정보 불러오기
print(cabinet.get(1))
print(cabinet.get(2))
print("\n")

# 키 추가
print(cabinet.get(5, "권민서"))
print("\n")

# 키 여부 롹인
print(1 in cabinet)
print(3 in cabinet)
print("\n")

# 값 변경
cabinet[1] = "ㅎㅇ"
print(cabinet)
print("\n")

# 새로운 값 추가
cabinet["A-1"] = "안녕"
print(cabinet)

# 값 지우기
del cabinet["A-1"]
print(cabinet)
print("\n")

#키들만 출력
print(cabinet.keys())
print(cabinet)
print("\n")

#키 값들만 출력
print(cabinet.values())
print(cabinet)
print("\n")

#키와 값 둘다 출력
print(cabinet.items())
print(cabinet)
print("\n")

#지우기
cabinet.clear()
print(cabinet)
print("\n")