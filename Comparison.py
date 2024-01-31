import timeit
from find_coins import find_coins_greedy
from find_coins import find_min_coins

coins = [50, 25, 10, 5, 2, 1]
large_sum = 102134

if __name__ == '__main__':
    greedy_time = timeit.timeit(lambda:find_coins_greedy(large_sum, coins), number=10)
    dp_time = timeit.timeit(lambda:find_min_coins(large_sum, coins), number=10)

    print(f"{'|Algoritms': <20} | {'Time': <20}")
    print(f"{'-'*60}")
    print(f"{'|Greedy algorithm': <20} | {greedy_time: <20.5f}")
    print(f"{'|Dynamic programming': <20} | {dp_time: <20.5f}")
