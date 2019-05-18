import pdb
midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']

student_grades = list(zip(students, finals, midterms))
pdb.set_trace()
zip_finmidterm = zip(finals,midterms)

print(student_grades)
#[('dan', 98, 80), ('ang', 89, 91), ('kate', 53, 78)]

print([max(pair) for pair in zip_finmidterm])
#[98, 91, 78]

print({i[0]:max(i[1],i[2]) for i in student_grades})
#{'dan': 98, 'ang': 91, 'kate': 78}

zip_finmidterm = zip(finals,midterms) #zip_finmidterm object can be accessed only once so we need to assign again
print(list(map(lambda x:max(x) , zip_finmidterm)))




