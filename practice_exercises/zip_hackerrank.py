#https://www.hackerrank.com/challenges/zipped/problem

student_count, subject_count = map(int, input().split())
subject = []
for i in range(subject_count):
    marks = list(map(float, input().split()))[:student_count] #even if user gives input more that student_count it is sliced till student_count
    subject.append(marks)
avg_scores = list(map(lambda x : sum(x)/len(x) ,zip(*subject)))
for i in avg_scores:
    print('{:.1f}'.format(i))