# Chapter 7 - Graphs Homework
# Machine Communication Network


class MachineNetwork:

    def __init__(self):
        self.machine_links = {}

    # Exercise 1
    def add_machine(self, machine):
        if machine not in self.machine_links:
            self.machine_links[machine] = []

    def add_link(self, m1, m2):
        self.add_machine(m1)
        self.add_machine(m2)
        if m2 not in self.machine_links[m1]:
            self.machine_links[m1].append(m2)
        if m1 not in self.machine_links[m2]:
            self.machine_links[m2].append(m1)

    def print_network(self):
        print("=== Machine Network ===")
        for machine, connections in self.machine_links.items():
            print(f"  {machine} -> {connections}")

    def print_connected_machines(self, machine):
        if machine not in self.machine_links:
            print(f"Error: '{machine}' not found in the network.")
            return
        print(f"Machines directly connected to {machine}:")
        for neighbor in self.machine_links[machine]:
            print(f"  - {neighbor}")

    # Exercise 2: BFS

    def bfs(self, start):
        if start not in self.machine_links:
            print(f"Error: '{start}' does not exist in the network.")
            return []

        visited = []
        queue = [start]
        seen = {start}

        while queue:
            current = queue.pop(0)
            visited.append(current)

            for neighbor in self.machine_links[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)

        return visited

    # Exercise 3: DFS

    def dfs(self, start):
        if start not in self.machine_links:
            print(f"Error: '{start}' does not exist in the network.")
            return []

        visited = []
        stack = [start]
        seen = set()

        while stack:
            current = stack.pop()
            if current in seen:
                continue
            seen.add(current)
            visited.append(current)

            for neighbor in reversed(self.machine_links[current]):
                if neighbor not in seen:
                    stack.append(neighbor)

        return visited


# --- Build the network ---

network = MachineNetwork()

network.add_link("Machine_A", "Machine_B")
network.add_link("Machine_A", "Machine_C")
network.add_link("Machine_B", "Machine_D")
network.add_link("Machine_C", "Machine_D")
network.add_link("Machine_C", "Machine_E")

# Exercise 1 output
network.print_network()
print()
network.print_connected_machines("Machine_A")
print()

# Exercise 2 output
print("BFS from Machine_A:")
print(network.bfs("Machine_A"))
print()

# Exercise 3 output
print("DFS from Machine_A:")
print(network.dfs("Machine_A"))