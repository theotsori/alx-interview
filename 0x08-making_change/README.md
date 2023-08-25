# Making Change Algorithm

The `makeChange` algorithm aims to find the fewest number of coins needed to meet a given total amount using the available coins of different values.

## Implementation

```python
def makeChange(coins, total):
    if total <= 0:
        return 0

    # Create a list to store the minimum number of coins needed for each total
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    return min_coins[total] if min_coins[total] != float('inf') else -1
```

## Explanation

1. The function `makeChange` takes two arguments: `coins`, a list of available coin values, and `total`, the target amount we want to achieve.

2. We start by checking if the `total` is less than or equal to 0. In this case, there's no need for any coins, so we return 0.

3. We create a list `min_coins` to store the minimum number of coins needed to achieve each possible total from 0 to the given `total`. We initialize all values in this list to positive infinity except for `min_coins[0]`, which is set to 0 since we need 0 coins to achieve a total of 0.

4. We use two nested loops to iterate over each possible total from 1 to `total` and each available coin value. For each total, we check if using the current coin value results in a valid total (i.e., `i >= coin`). If it's valid, we update `min_coins[i]` to the minimum value between its current value and `min_coins[i - coin] + 1`. This represents the minimum number of coins needed to achieve the current total if we use the current coin.

5. After the loops finish, we return `min_coins[total]` if it's not equal to positive infinity. If it is, it means the given `total` cannot be achieved using the available coins, so we return -1.

## Example

```python
print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
```

In the first example, using coin values [1, 2, 25], the algorithm can make up the total of 37 using 7 coins: 25 + 2 + 2 + 2 + 2 + 2 + 2.

In the second example, it's not possible to make up the total of 1453 using the provided coin values, so the algorithm returns -1.