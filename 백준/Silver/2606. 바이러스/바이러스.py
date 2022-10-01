import sys

computer_number = int(sys.stdin.readline())
line_number = int(sys.stdin.readline())
graph = [set() for _ in range(computer_number)]

for _ in range(line_number):
    start_node, end_node = map(int, sys.stdin.readline().split())
    graph[start_node - 1].add(end_node - 1)
    graph[end_node - 1].add(start_node - 1)

result = 0

visited = [False for _ in range(computer_number)]
progress_stack = []
progress_stack.append(0)
visited[0] = True
while progress_stack != []:
    next_idx = progress_stack.pop()
    for element in graph[next_idx]:
        if not visited[element]:
            progress_stack.append(element)
            visited[element] = True
            result += 1

print(result)