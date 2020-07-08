"""
自解：no extra space, 純用pointer.
"""
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        def helper(A):
            i = 0
            while i < len(A) - 1:
                c = A[i]

                if c == "#":
                    if i == 0:
                        A = A[1:]
                    else:
                        A = A[:i - 1] + A[i + 1:]
                        i -= 1
                else:
                    i += 1

            if A[-1] == "#":
                if len(A) > 2:
                    A = A[:-2]
                else:
                    A = ""

            return A
        return helper(S) == helper(T)