# 여행경비 계산 프로그램


def hotel_cost(nights):
    return nights * 140


def flight_cost(city):
    if city == 'Cebu':
        return 483
    elif city == 'Singapore':
        return 620
    elif city == 'Bali':
        return 722
    elif city == 'Los Angeles':
        return 975
    else:
        return 0


def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
        return cost - 50
    elif days >= 3:
        return cost - 20
    else:
        return cost


def trip_cost(nights, city, days, spending_money):
    return hotel_cost(nights) + flight_cost(city) \
           + rental_car_cost(days) + spending_money


def main():
    print(trip_cost(3, 'Cebu', 4, 1000))

# 호출하기
main()


