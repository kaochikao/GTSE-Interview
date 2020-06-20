"""
We parse the content in the parentheses and evaluate it.
If the content is empty string then the value is 1.
Otherwise, the value is the value of the content multiply by 2
And we use the exact the same function to evaluate the value of the content (recursion).
We can know the start and the end of the parentheses (so we can extract the content) by `depth`, which is the level of parentheses.
Even though this looks efficient the time complexity is high. O(N^depth).
You can think of a case like this
```
(((((((((( ... content ... ))))))))))
```
Where in every level you have to go through the whole thing again.
The Space complexity is O(depth).
Even we only use O(1) in each function, but the recursion takes stack memory of O(depth).
"""
# "(()(()))"

"""
algo理解：
- iteration & recursion 並用; 因為會有多個同層的(), 也會有子層的()

實現技巧：
- [TODO] 快慢pointers?
"""
def scoreOfParentheses_rec(S):
    depth = 0
    start = 0
    score = 0

    for i in range(len(S)):
        s = S[i]

        if s == "(":
            depth += 1
        else:
            depth -= 1

        # depth = 0 即自己iterator所在的level
        if depth == 0:
            # 這裡start & i 是快慢pointers?
            content = S[start + 1: i]
            if content == '':  # *
                score += 1
            else:
                score += scoreOfParentheses_rec(content) * 2

            # ?
            start = i + 1

    return score

"""
If we take a closer look, we will notice that `()` are the only structure that provides value, the outer parentheses just add some multiplier.
So we only need to be concerned with `depth`.
For level we multiply the inner content by 2, so for each `()`, its value is `1 * 2**depth`
The time complexity is O(N).
The space complexity is O(1).
"""

"""
algo理解：
- 直接用iteration去做原本以為要用recursion的問題

實現技巧：
- 動態增減depth的技巧很不錯
"""
def scoreOfParentheses(S):

    score = 0
    depth = 0

    for i in range(len(S)):
        s = S[i]
        if s == '(':
            depth += 1
        else:
            depth -= 1
            if S[i - 1] == '(':
                score += 2 ** depth

    return score