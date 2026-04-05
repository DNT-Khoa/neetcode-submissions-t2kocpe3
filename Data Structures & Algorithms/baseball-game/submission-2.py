class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        counter = 0

        for op in operations:
            if op == "+":
                sum_prev_two = int(stack[-1]) + int(stack[-2])
                stack.append(str(sum_prev_two))
                counter += sum_prev_two
            elif op == "D":
                double = int(stack[-1]) * 2
                counter += double
                stack.append(str(double))
            elif op == "C":
                prev = stack.pop()
                counter -= int(prev)
            else:
                stack.append(op)
                counter += int(op)

        return counter