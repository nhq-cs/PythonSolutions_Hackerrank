if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum = 0
    for name in student_marks:
        if name == query_name:
            for item in student_marks[query_name]:
                sum += item
    print('%.2f'%(sum/len(student_marks[query_name])))
