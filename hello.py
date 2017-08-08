# 파이썬 예제 (3000불 환전 시 필요한 원화 계산)
# 1불에 1147원, 은행수수료 0.45%

how_much_dollar = 3000
won_for_a_dollar = 1147
bank_fee_percent = 0.45

won_needed_before_bank_fee = how_much_dollar * won_for_a_dollar
bank_fee = won_needed_before_bank_fee * (bank_fee_percent / 100)
won_needed = won_needed_before_bank_fee * bank_fee

# print how much won I need
print(bank_fee)
print(won_needed)

