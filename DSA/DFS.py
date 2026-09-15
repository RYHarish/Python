class RecursiveDFS:
    def dfs(self, node, graph, visited):
        if node not in graph:
            return

        visited.add(node)
        print(node, end=" ")

        for neighbor in graph.get(node, []):
            if neighbor in graph and neighbor not in visited:
                self.dfs(neighbor, graph, visited)


def main():
    graph = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 4],
        3: [1, 4],
        4: [2, 3],
    }

    visited = set()

    print("DFS traversal from node 0:")
    RecursiveDFS().dfs(0, graph, visited)
    print()


if __name__ == "__main__":
    main()