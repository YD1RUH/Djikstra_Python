import heapq

# Fungsi Dijkstra dengan pelacakan jalur
def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    previous_nodes = {node: None for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        curr_distance, curr_node = heapq.heappop(pq)
        if curr_distance > distances[curr_node]:
            continue

        for neighbor, weight in graph[curr_node].items():
            distance = curr_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = curr_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous_nodes

# Fungsi visualisasi ASCII
def draw_ascii_graph(graph):
    print("\n=== Visualisasi Graph (ASCII) ===")
    for node in graph:
        connections = []
        for neighbor, weight in graph[node].items():
            connections.append(f"{neighbor}({weight})")
        connections_str = " --> ".join(connections)
        print(f"{node} --> {connections_str}")
    print("="*40)

# Fungsi pelacakan rute
def get_path(prev_nodes, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = prev_nodes[current]
    path.reverse()
    return path

# Input Dinamis
def input_graph():
    graph = {}
    nodes = input("Masukkan daftar node (pisahkan dengan spasi): ").split()
    
    for node in nodes:
        graph[node] = {}
    
    print("Masukkan edge (format: asal tujuan bobot), ketik 'done' jika selesai:")
    while True:
        edge = input("> ")
        if edge.lower() == 'done':
            break
        try:
            asal, tujuan, bobot = edge.split()
            graph[asal][tujuan] = int(bobot)
            # Jika ingin undirected graph, uncomment:
            # graph[tujuan][asal] = int(bobot)
        except ValueError:
            print("Format salah. Coba lagi.")
    
    return graph

# Main Program
if __name__ == "__main__":
    graph = input_graph()
    draw_ascii_graph(graph)
    
    start = input("Masukkan node awal: ")
    distances, prev_nodes = dijkstra(graph, start)

    print(f"\nJarak dan Jalur Terpendek dari {start}:")
    for node in graph:
        if distances[node] == float('infinity'):
            print(f"{start} -> {node}: tidak terjangkau")
        else:
            path = get_path(prev_nodes, start, node)
            path_str = " -> ".join(path)
            print(f"{start} -> {node} = {distances[node]} | Jalur: {path_str}")
