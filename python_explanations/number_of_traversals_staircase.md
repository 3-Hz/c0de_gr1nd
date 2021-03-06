# Count the Number of Moves to Climb Stairs
You are climbing a set of stairs that takes _n_ steps to reach the top. You can climb 1 to _k_ steps at a time. How many ways can you reach the top?

## Examples
```
 Input: n = 7
        k = 2
Output: 21

 Input: n = 11
        k = 7
Output: 1004
```

## Solution
```python
def number_of_ways_to_top(n, k):
    def helper(n, k):
        dp = [1, 1] + [0] * (n - 2)
        for i in range(2, n):
            j = 1
            while j <= k and j <= i:
                dp[i] += dp[i-j]
                j += 1
        return dp[-1]

    return helper(n + 1, k)
```

## Explanation
* Recursive formula: _moves_(_n_, _k_) = _moves_(_n_ - 1, _k_) + _moves_(_n_ - 2, _k_) + ..._moves_(_n_ - _k_, _k_)

## Code Dissection - number_of_ways_to_top
1. Return the number of ways to reach the _n_-th stair
    ```python
    return helper(n + 1, k)
    ```

## Code Dissection - helper
1. Create the DP table
    ```python
    dp = [1, 1] + [0] * (n - 2)
    ```
2. Climb the stairs from 1 to _k_ steps at a time to the _n_-th stair
    ```python
    for i in range(2, n):
        j = 1
        while j <= k and j <= i:
            dp[i] += dp[i-j]
            j += 1
    ```
3. Return the number of ways to reach the top
    ```python
    return dp[-1]
    ```