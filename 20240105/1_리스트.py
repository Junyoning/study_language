# 리스트

# 몇 번째인지
my_list = ["안준현", "이기혜", "한늘찬"]
print(my_list.index("이기혜"))

# 맨 뒤에 추가
my_list.append("문승재")
print(my_list)

# 값 사이에 추가
my_list.insert(2, "안준현")
print(my_list)

# 지우기(꺼냄) 
my_list.pop()
print(my_list)

# 같은 값 개수 찾기 
print(my_list.count("안준현"))

# 오름차수 정렬 
num_list = [4, 6, 2, 1, 3, 5]
num_list.sort()
print(num_list)

# 순서 뒤집기 
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 두개 리스트 합치기
my_list = ["안준현", "이기혜", "한늘찬"]
num_list = [4, 6, 2, 1, 3, 5]

my_list.extend(num_list)
print(my_list)