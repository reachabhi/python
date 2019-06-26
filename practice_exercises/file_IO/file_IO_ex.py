
# {'lines': 172, 'words': 2145, 'characters': 11227}

def statistics(file):
    with open(file) as f:
        lines_list = f.readlines()
        return dict(lines = len(lines_list), words = sum(map(lambda x:len(x.split(' ')),
                    lines_list)), 
                    characters = sum(map(lambda x:len(x),lines_list)))
       
statistics('story.txt')