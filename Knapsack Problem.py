# def knapSack(weight_limit, items, weights, values):
#     n = len(items)
#     dp = [[0 for _ in range(weight_limit + 1)] for _ in range(n + 1)]
#
#     for i in range(1, n + 1):
#         for w in range(1, weight_limit + 1):
#             if weights[i - 1] <= w:
#                 dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
#             else:
#                 dp[i][w] = dp[i - 1][w]
#
#     return dp[n][weight_limit]
#
#
# # Example usage
# # items = ['laptop', 'headphones', 'book', 'snacks']
# # weights = [3, 1, 2, 1]
# # values = [1500, 100, 20, 50]
# # weight_limit = 5
#
# items = ['item1', 'item2', 'item3', 'item4', 'item5']
# weights = [3, 4, 2, 5, 1]
# values = [100, 200, 50, 75, 25]
# weight_limit = 10
#
# print(knapSack(weight_limit, items, weights, values))


def knapSack(weight_limit, items, weights, needs):
    n = len(items)
    dp = [[0 for _ in range(weight_limit + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, weight_limit + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(needs[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][weight_limit]


def get_user_input():
    items = []
    weights = []
    needs = []

    num_items = int(input("Enter the number of items: "))

    for i in range(num_items):
        item = input(f"Enter item {i + 1}: ")
        weight = float(input(f"Enter weight of {item} (in kg): "))
        need = int(input(f"Enter need ranking of {item} (1-10): "))

        items.append(item)
        weights.append(weight)
        needs.append(need)

    weight_limit = float(input("Enter the weight limit (in kg): "))

    return items, weights, needs, weight_limit


def main():
    items, weights, needs, weight_limit = get_user_input()
    max_need = knapSack(int(weight_limit * 100), items, [int(w * 100) for w in weights], needs)

    print(f"Maximum need that can be achieved: {max_need}")

    # Print the items that should be brought
    dp = [[0 for _ in range(int(weight_limit * 100) + 1)] for _ in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        for w in range(1, int(weight_limit * 100) + 1):
            if weights[i - 1] * 100 <= w:
                dp[i][w] = max(needs[i - 1] + dp[i - 1][w - int(weights[i - 1] * 100)], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    w = int(weight_limit * 100)
    for i in range(len(items), 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            print(f"Bring {items[i - 1]}")
            w -= int(weights[i - 1] * 100)


if __name__ == "__main__":
    main()
