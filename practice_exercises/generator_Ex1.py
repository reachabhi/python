def week():
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday' , 'Saturday' , 'Sunday']
    for i in weekdays:
        yield i

days = week()
for i in days:
	print(i)

print(next(days)) #throws StopIteration Error since i is already pointing to the last item in the generator so it cna generate no more