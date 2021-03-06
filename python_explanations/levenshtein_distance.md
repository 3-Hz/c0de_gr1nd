# Compute the Levenshtein Distance
Given two strings _A_ and _B_, find the minimum number of edits needed to convert _A_ to _B_.

## Examples
```
 Input: A = 'racecar'
        B = 'honda'
Output: 6

 Input: A = 'kitten'
        B = 'sitting'
Output: 3
```

## Solution
```python
def levenshtein_distance(A, B):
    m, n = len(A), len(B)
    dp = [list(range(n + 1))] + [[i] + [0] * n for i in range(1, m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            insert = dp[i][j-1]
            delete = dp[i-1][j]
            replace = dp[i-1][j-1]
            if A[i-1] == B[j-1]:
                dp[i][j] = replace
            else:
                dp[i][j] = min(insert, delete, replace) + 1
    return dp[-1][-1]
```

## Explanation
There are 3 operations to perform on a string to convert it:
1. Insert character
2. Delete character
3. Replace character

* While using a DP table to store the distance:
    * If the last character in _A_ == last character in _B_, then nothing has changed and the distance is the same
    * Otherwise, get the minimum distance between insert, delete, and replace

## Code Dissection
1. Create a DP table to store the distance for each edit
    ```python
    m, n = len(A), len(B)
    dp = [list(range(n + 1))] + [[i] + [0] * n for i in range(1, m + 1)]
    ```
2. Loop over the length of _A_ and _B_ such that dp[_i_][_j_] stores the distance between the last character in _A_ and the last character in _B_
    ```python
    for i in range(1, m + 1):
        for j in range(1, n + 1):
    ```
3. Define the distances for each edit: insert, delete, and replace
    ```python
    insert = dp[i][j-1]
    delete = dp[i-1][j]
    replace = dp[i-1][j-1]
    ```
4. If the last character in _A_ and _B_ are the same, then ignore, otherwise, get the minimum distance of insert, delete, and replace
    ```python
    if A[i-1] == B[j-1]:
        dp[i][j] = replace
    else:
        dp[i][j] = min(insert, delete, replace) + 1
    ```
5. Return the levenshtein distance
    ```python
    return dp[-1][-1]
    ```