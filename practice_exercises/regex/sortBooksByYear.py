import re
ls = []

def sortTitles(title):
	pattern = re.compile(r"(^[\w ]+) \((\b\d{4})\)$")
	
	for book in title:
		match=pattern.search(book)
		result = pattern.sub("\g<2> - \g<1>", book )
		ls.append(result)
	ls.sort()
	print(ls)
	


title = ["abc sdgsdf fsdf (1987)", "rtretrt  gd rewr e (1873)", "rtrtrtrw wer a ewr (1935)", "af asgffdshs (1840)"]

sortTitles(title)




