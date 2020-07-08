class Solution(object):
    def validateStackSequences(self, pushed, popped):

        in_stack = []
        pos = 0
        while pos != len(pushed):
            curr = pushed[pos]
            while len(in_stack) > 0 and len(popped) > 0 and in_stack[-1] == popped[0]:
                in_stack.pop(-1)
                popped.pop(0)
            if len(popped) == 0:
                break
            if curr == popped[0]:
                popped.pop(0)
            else:
                in_stack.append(curr)
            pos += 1


        while len(in_stack) > 0 and len(popped) > 0 and in_stack[-1] == popped[0]:
            in_stack.pop(-1)
            popped.pop(0)
        if len(in_stack) == 0:
            return True
        return False


"""
自解醜解法：
- 有些會fail
"""
class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:

        pushed_trunc = []
        popped_trunc = []

        for i in range(len(pushed)):

            if pushed[i] != popped[i]:
                pushed_trunc.append(pushed[i])
                popped_trunc.append(popped[i])
                
        if len(pushed_trunc) == 0 and len(popped_trunc) == 0:
            return True

        return self.rec([pushed_trunc[0]], pushed_trunc[1:], popped_trunc)

    def rec(self, stack, pushed, popped):
        tmp_stack = [t for t in stack]

        if len(pushed) == 0 and len(popped) == 0:
            return True

        if len(pushed) == 0:
            while tmp_stack:

                if tmp_stack[-1] != popped[0]:
                    return False
                else:
                    tmp_stack.pop()
                    popped = popped[1:]
            return True

        tmp_stack.append(pushed[0])
        if self.rec(tmp_stack, pushed[1:], popped):
            return True
        else:

            tmp_stack.pop()

        if len(tmp_stack) == 0:
            return False

        if tmp_stack.pop() == popped[0]:
            return self.rec(tmp_stack, pushed, popped[1:])
        else:
            return False