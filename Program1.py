from p1_support import load_level, show_level
from math import sqrt
from heapq import heappush, heappop


def dijkstras_shortest_path(src, dst, graph, adj):
    queue = []
    dist = {}
    prev = {}
    sequence = []

    dist[src] = 0
    prev[src] = None
    heappush(queue, [0, src])

    while queue:
        curr_dist, curr_state = heappop(queue)

        if curr_state == dst:
            break
        elif curr_dist > dist[curr_state]:
            continue
        else:
            neighbors = adj(graph, curr_state)
            for next_node in neighbors:
                alt = curr_dist + next_node[1]
                if next_node[0] not in dist or alt < dist[next_node[0]]:
                    dist[next_node[0]] = alt
                    prev[next_node[0]] = curr_state
                    heappush(queue, (alt, next_node[0]))

    if curr_state == dst:
        while prev[curr_state] is not None:
            sequence.append(curr_state)
            curr_state = prev[curr_state]
        sequence.append(src)
        sequence.reverse()
        return sequence
    else:
        return []


def navigation_edges(level, cell):
    steps = []
    x, y = cell
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            next_cell = (x + dx, y + dy)
            dist = sqrt(dx * dx + dy * dy)
            if dist > 0 and next_cell in level['spaces']:
                steps.append((next_cell, dist))
    return steps


def test_route(filename, src_waypoint, dst_waypoint):
    level = load_level(filename)

    show_level(level)

    src = level['waypoints'][src_waypoint]
    dst = level['waypoints'][dst_waypoint]

    path = dijkstras_shortest_path(src, dst, level, navigation_edges)

    if path:
        show_level(level, path)
    else:
        print
        "No path possible!"


if __name__ == '__main__':
    import sys

    _, filename, src_waypoint, dst_waypoint = sys.argv
    test_route(filename, src_waypoint, dst_waypoint)
__author__ = 'Alec Noble and Nathan Irwin'