def parse_input(input_network):
    return [[int(cost) if cost != '-' else float('inf') for cost in line.split(',')] for line in input_network.strip().split('\n')]

def find_min_edge(adj_matrix, visited):
    min_edge = float('inf')
    min_edge_index = None
    for i in range(len(adj_matrix)):
        if visited[i]:
            for j in range(len(adj_matrix)):
                if not visited[j] and adj_matrix[i][j] < min_edge:
                    min_edge = adj_matrix[i][j]
                    min_edge_index = (i, j)
    return min_edge_index, min_edge

def minimum_spanning_tree(adj_matrix):
    num_nodes = len(adj_matrix)
    visited = [False] * num_nodes
    visited[0] = True
    total_cost = 0

    while False in visited:
        min_edge, min_cost = find_min_edge(adj_matrix, visited)
        if min_edge is None:
            break
        total_cost += min_cost
        visited[min_edge[1]] = True

    return total_cost

def maximum_saving(input_network: str) -> int:
    adj_matrix = parse_input(input_network)
    original_cost = sum(cost for row in adj_matrix for cost in row if cost != float('inf'))
    minimum_spanning_cost = minimum_spanning_tree(adj_matrix)
    max_saving = original_cost - minimum_spanning_cost
    return max_saving

# Example usage:
input_network = '''-,14,10,19,-,-,-
14,-,-,15,18,-,-
10,-,-,26,,29,-
19,15,26,-,16,17,21
-,18,-,16,-,-,9
-,-,29,17,-,-,25
-,-,-,21,9,25,-
'''
max_saving = maximum_saving(input_network)
print(max_saving)
