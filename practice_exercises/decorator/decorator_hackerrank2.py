def person_lister(f):
    def inner(people):
        # complete the function
        print('###',people)
        sorted_people = sorted(people,key=lambda x : x[2])     
        
        return f(sorted_people)
    return inner

@person_lister
def name_format(person):
	print("@@@", person)
	return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(name_format(people), sep='\n')