# 영화감독과 대표작을 데이터로 표현
# 1. 리스트 2개

director = ['봉준호', '김기덕', '마틴 스콜세지', '크리스토퍼 놀란', '박찬욱']
masterpiece = ['옥자', '나쁜남자','카지노', '인셉션', '올드보이']


# 2. 이중리스트(이차원 리스트), list of list, two dimension list

mp_director = [['봉준호', '옥자'],
               ['김기덕', '나쁜남자'],
               ['마틴 스콜세지', '카지노'],
               ['크리스토퍼 놀란', '인셉션'],
               ['박찬욱', '올드보이']
               ]

# dictionary로 바꾸기 감독 key, 대표작 value로

mp_director_dic = {'봉준호':'옥자', '김기덕':'나쁜남자', '마틴 스콜세지': '카지노',
                   '크리스토퍼 놀란':'인셉션', '박찬욱':'올드보이','봉준호':'괴물'}

print(mp_director_dic.get('봉준호')) # 키가 두 개 있을 때는 하나는 무시가 됨.

# dictionary 키/값 아이템 삭제

del mp_director_dic['봉준호']
print(mp_director_dic)

# dictionary 키/값 아이템 추가
mp_director_dic.setdefault('류승완', '베테랑')
mp_director_dic.setdefault('류승완', '베를린')
print(mp_director_dic)

#
