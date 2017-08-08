# 함수 만들기 연습 1


def cube(number):
    return number ** 3


def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False

print (by_three(1))

# 함수 만들기 연습 2


def by_s(s):

    if s == 'yes':
        return 'shutting down'
    elif s == 'no':
        return 'shutting aborted'
    else:
        return 'sorry'

print(by_s('yes'))
print(by_s('no'))
print(by_s('hi'))

