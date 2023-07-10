# Minimum Operations

In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

## Prototype

```python
def minOperations(n):
    """
    Returns the minimum number of operations needed to achieve n H characters in the file.

    Args:
    - n: An integer representing the desired number of H characters.

    Returns:
    - An integer representing the minimum number of operations.
    """
```

## Approach

To solve this problem, we can use a greedy algorithm. We start with a single 'H' character in the file. We can consider this as the initial state. Then, we iteratively perform the following steps:

1. Check if n is divisible by the current number of characters in the file. If it is divisible, we can achieve n characters by copying all the existing characters and pasting them multiple times.
2. If n is not divisible by the current number of characters, we need to find a divisor of n that is less than the current number of characters. Let's call this divisor k.
3. We then divide n by k to find the number of times we need to paste the existing characters to reach n.
4. Add k - 1 (k-1 because we already have one character) to the number of operations, as we need to perform k - 1 additional paste operations.
5. Repeat the above steps until we reach n characters.

## Complexity Analysis

The time complexity of this approach is O(sqrt(n)), as we iterate up to the square root of n to find divisors.

## Example

Let's consider an example:

Input:
```python
n = 9
```

Output:
```python
minOperations(n) = 6
```

Explanation:
Starting with 'H', we perform the following operations:
- Copy All: 'H'
- Paste: 'HH'
- Paste: 'HHH'
- Copy All: 'HHH'
- Paste: 'HHHHHHH'
- Paste: 'HHHHHHHHH'
We have now achieved 9 'H' characters with a total of 6 operations.

## Conclusion

The `minOperations` method calculates the minimum number of operations needed to achieve exactly n 'H' characters in the file. By following the greedy algorithm described above, we can solve this problem efficiently.