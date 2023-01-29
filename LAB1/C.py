from collections import deque
a,b = input().split()
stack, stack2 = deque(), deque()

for i in range(len(a)):
    if a[i] != '#':
        stack.append(a[i])
    else:
        stack.pop()
for j in range(len(b)):
    if b[j] != '#':
        stack2.append(b[j])
    else:
        stack2.pop()

if stack == stack2:
  print("Yes")
else:
  print("No")