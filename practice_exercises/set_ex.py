n = int(input())
s = set(map(int, input().split()))
command_count = int(input())
commands=[]
for i in range(command_count):
    commands.append(input().split())
print(commands)
for i in commands:
    if i[0] == 'pop':
        s.pop()
        print(s)
    if i[0] == 'remove':
        s.remove(int(i[1]))
        print(s)
    if i[0] == 'add':
        s.add(int(i[1]))
        print(s)
    if i[0] == 'discard':
        s.discard(int(i[1]))

print(*s)
    

    

