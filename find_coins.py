coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(sum_, coins):
    count_coins = {}
    for coin in coins:
        count = sum_ // coin
        if count > 0:
            count_coins[coin] = count
        sum_ = sum_ - coin * count
    return count_coins


result = find_coins_greedy(113, coins)
print(f'Greedy algorithm    - {result}')

def find_min_coins(sum, coins):
    min_coins = [float('inf')] * (sum + 1)
    min_coins[0] = 0

    # Основний цикл динамічного програмування
    for i in range(1, sum + 1):
        for coin in coins:
            if coin <= i:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    # Перевірка, чи можливо сформувати задану суму
    if min_coins[sum] == float('inf'):
        return "Неможливо сформувати задану суму"

    # Побудова словника з результатами
    result = {}
    current_sum = sum
    while current_sum > 0:
        for coin in coins:
            if current_sum - coin >= 0 and min_coins[current_sum] == min_coins[current_sum - coin] + 1:
                result[coin] = result.get(coin, 0) + 1
                current_sum -= coin
                break

    return result

resultd = find_min_coins(113, coins)
print(f'Dynamic programming - {resultd}')
print('\n')
