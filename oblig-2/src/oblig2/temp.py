from collections import deque
import heapq


def reconstruct_path(parent, node):
    path = []
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path


def shortest_path(start_actor, goal_actor, actor_to_movies, movie_to_actors):
    """
    Return a shortest (unweighted) path between two actors.
    The result alternates: actor, movie, actor, ..., actor.
    Returns [] if no path exists.
    """
    if start_actor == goal_actor:
        return [start_actor]

    parent = {start_actor: None}
    queue = deque([start_actor])

    while queue:
        current = queue.popleft()

        # Pick the right neighbour list depending on node type.
        if current.startswith("nm"):
            neighbors = actor_to_movies[current]  # actor -> movies
        else:
            neighbors = movie_to_actors[current]  # movie -> actors

        for neighbor in neighbors:
            if neighbor in parent:  # already discovered
                continue
            parent[neighbor] = current
            if neighbor == goal_actor:  # reached the goal
                return reconstruct_path(parent, goal_actor)
            queue.append(neighbor)

    return []  # goal not reachable


def chillest_path(start_actor, goal_actor, movies, actor_to_movies, movie_to_actors):
    """
    Return the minimum-cost path between two actors, where entering a movie
    costs (10 - rating) and entering an actor costs 0.
    Returns [] if no path exists.
    """
    if start_actor == goal_actor:
        return [start_actor]

    dist = {start_actor: 0.0}
    parent = {start_actor: None}
    pq = [(0.0, start_actor)]  # (tentative distance, node)
    visited = set()  # nodes whose distance is final

    while pq:
        d, current = heapq.heappop(pq)

        if current in visited:  # stale entry
            continue
        visited.add(current)

        if current == goal_actor:
            return reconstruct_path(parent, goal_actor)

        if current.startswith("nm"):
            # actor -> movies: pay the movie's cost
            for movie in actor_to_movies[current]:
                weight = 10.0 - movies[movie][1]  # movies[id] = (title, rating)
                new_d = d + weight
                if new_d < dist.get(movie, float("inf")):
                    dist[movie] = new_d
                    parent[movie] = current
                    heapq.heappush(pq, (new_d, movie))
        else:
            # movie -> actors: free
            for actor in movie_to_actors[current]:
                if d < dist.get(actor, float("inf")):
                    dist[actor] = d
                    parent[actor] = current
                    heapq.heappush(pq, (d, actor))

    return []  # goal not reachable
