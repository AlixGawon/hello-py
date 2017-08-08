# create types
a = 5
b = 3.14
c = 'hello'
d = True

# int -> float
a = float(a)
print(a)

# float -> int
b = int(b)
print(b)

# int -> str
e = str('hi')
print(e)

# String -> int
i = int("50")
print(i)

a_list = list('hello')
print(type(a_list))
print(a_list)

a_str = 'hello world'
print(a_str[8])
print(a_str[1])

# 글자 자르기
a_mystr = 'It\'s very hot today!'
print(a_mystr[5:9])
print(a_mystr[0:9])
print(a_mystr[10:13])
print(a_mystr[-6:])
print(a_mystr[-10:-7])
print(a_mystr)

# list & index
color = ['black', 'white', 'blue', 'grey', 'purple']
print(color[0])
print(color[2])
print(color[4])

# list CRUD 데이터 추가 삭제 수정하기!
# 값 삭제
color.remove('black')
print(color)

# 인덱스 삭제
del color[2]
print(color)

# 값 추가( 리스트의 중간에 끼워넣기)
color.insert(0,'silver')
print(color)

# 값 수정 (마지막에 추가)
color.append('gold')
print(color)

# 값 수정 ( 인덱스 바꾸기)
color[2] = '블루'
print(color)

# 리스트와 리스트를 합치기
other_colors = ['royal blue', 'sky blue']
color = color + other_colors
print(color)

# 리스트 상에서 아이템 위치 이동
color.insert(3,color[6])
del color[6]

print(color)

# 리스트에서 가장 큰 숫자 찾기
ft = [3, 1, 5, 6, 10, 2, 4, 8, 7, 5, 9]

ft.sort(reverse=True)

print(ft[0])

# tuple 사용해보기! (List와 비교해보기)
a_tuple = ('red', 'blue')
c, d = a_tuple
print(c)
print(d)
other_tuple = 'red', 'blue'
print(other_tuple[1])
print(other_tuple[-1])







