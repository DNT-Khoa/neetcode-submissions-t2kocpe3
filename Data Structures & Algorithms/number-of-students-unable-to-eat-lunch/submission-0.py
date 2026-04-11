class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_q = deque()
        sandwich_stack = []
        length = len(students)

        for i in range(length):
            student_q.append(students[i])
            sandwich_stack.append(sandwiches[length - i - 1])
        
        times_rotated = 0
        while student_q and times_rotated < length:
            if student_q[0] == sandwich_stack[-1]:
                student_q.popleft()
                sandwich_stack.pop()
                times_rotated = 0
            else:
                student_q.append(student_q.popleft())
                times_rotated += 1
        
        return len(student_q)
