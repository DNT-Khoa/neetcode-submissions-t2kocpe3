class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack, counter = [], 0

        for op in operations:
            if op == "+":
                sum_prev_two = stack[-1] + stack[-2]
                counter += sum_prev_two
                stack.append(sum_prev_two)
            elif op == "D":
                double_prev_score = stack[-1] * 2
                counter += double_prev_score
                stack.append(double_prev_score)
            elif op == "C":
                prev_score = stack.pop()
                counter -= prev_score
            else:
                num_int = int(op)
                stack.append(num_int)
                counter += num_int

        return counter