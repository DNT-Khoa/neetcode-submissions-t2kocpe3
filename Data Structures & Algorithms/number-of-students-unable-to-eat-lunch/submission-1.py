class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = Counter(students)
        length = len(students)

        for sandwich in sandwiches:
            if cnt[sandwich] == 0:
                break
            else:
                length -= 1
                cnt[sandwich] -= 1
        return length
