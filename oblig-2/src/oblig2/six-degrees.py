import sys, heapq  # builtin priority queue
from collections import defaultdict, deque, Counter


def debug(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def parse_data():
    input_stream = sys.stdin

    movies = {}
    actors = {}

    movie_to_actors = defaultdict(list)
    actor_to_movies = defaultdict(list)

    line = input_stream.readline()

    # Empty input
    if not line:
        return

    # Movies
    M = int(line.strip())
    for _ in range(M):
        id, title, rating = input_stream.readline().rstrip("\n").split("\t")
        movies[id] = (title, float(rating))

    # Actors
    A = int(input_stream.readline().strip())
    for _ in range(A):
        id, name = input_stream.readline().rstrip("\n").split("\t")
        actors[id] = name

    # Edges
    E = int(input_stream.readline().strip())
    for _ in range(E):
        movie_id, actor_id = input_stream.readline().rstrip("\n").split("\t")
        movie_to_actors[movie_id].append(actor_id)
        actor_to_movies[actor_id].append(movie_id)

    # Shortest ladder queries
    Qs = int(input_stream.readline().strip())
    shortest_ladder_queries = []
    for _ in range(Qs):
        first_actor_id, second_actor_id = (
            input_stream.readline().rstrip("\n").split("\t")
        )
        shortest_ladder_queries.append((first_actor_id, second_actor_id))

    # Chillest ladder queries
    Qc = int(input_stream.readline().strip())
    chillest_ladder_queries = []
    for _ in range(Qc):
        first_actor_id, second_actor_id = (
            input_stream.readline().rstrip("\n").split("\t")
        )
        chillest_ladder_queries.append((first_actor_id, second_actor_id))

    return (
        movies,
        actors,
        movie_to_actors,
        actor_to_movies,
        shortest_ladder_queries,
        chillest_ladder_queries,
    )


def reconstruct_path(parent, node):
    path = []
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path


def shortest_path(start_actor, goal_actor, actor_to_movies, movie_to_actors):
    if start_actor == goal_actor:
        return [start_actor]

    parent = {start_actor: None}
    queue = deque([start_actor])

    while queue:
        current = queue.popleft()
        if current.startswith("nm"):
            neighbors = actor_to_movies[current]  # actor -> movies
        else:
            neighbors = movie_to_actors[current]  # movie -> actors

        for n in neighbors:
            if n in parent:  # already discovered
                continue
            parent[n] = current
            if n == goal_actor:  # reached the goal
                return reconstruct_path(parent, goal_actor)
            queue.append(n)

    return []


def chillest_path(start_actor, goal_actor, movies, actor_to_movies, movie_to_actors):
    if start_actor == goal_actor:
        return [start_actor]

    dist = {start_actor: 0.0}
    parent = {start_actor: None}
    pq = [(0.0, start_actor)]  # priority queue, (distance + current actor)
    visited = set()  # use set for final shortest path to prevent double checking

    while pq:
        d, current = heapq.heappop(pq)

        if current in visited:
            continue
        visited.add(current)

        if current == goal_actor:
            return reconstruct_path(parent, goal_actor)

        if current.startswith("nm"):
            # actor -> movies
            for m in actor_to_movies[current]:
                weight = 10.0 - movies[m][1]  # movies[id] = (title, rating)
                new_d = d + weight
                if new_d < dist.get(m, float("inf")):
                    dist[m] = new_d
                    parent[m] = current
                    heapq.heappush(pq, (new_d, m))
        else:
            # movie -> actors
            for a in movie_to_actors[current]:
                if d < dist.get(a, float("inf")):
                    dist[a] = d
                    parent[a] = current
                    heapq.heappush(pq, (d, a))

    return []


def find_components(actors, actor_to_movies, movie_to_actors):
    visited_movies = set()
    visited_actors = set()
    components = []

    for actor in actors:
        if actor not in visited_actors:
            current_component_movies = set()
            current_component_actors = {actor}

            # Add to global visited set
            visited_actors.add(actor)
            queue = deque([actor])

            # While queue is not empty
            while queue:
                current_id = queue.popleft()
                if current_id.startswith("nm"):
                    # Every movie with this actor
                    for movie_id in actor_to_movies[current_id]:
                        # We want to visit each node exactly once
                        if movie_id not in visited_movies:
                            visited_movies.add(movie_id)
                            current_component_movies.add(movie_id)
                            queue.append(movie_id)
                else:
                    # Every actor in this movie
                    for actor_id in movie_to_actors[current_id]:
                        # We want to visit each node exactly once
                        if actor_id not in visited_actors:
                            visited_actors.add(actor_id)
                            current_component_actors.add(actor_id)
                            queue.append(actor_id)

            components.append((current_component_movies, current_component_actors))

    return components


if __name__ == "__main__":
    # Parse data
    (
        movies,
        actors,
        movie_to_actors,
        actor_to_movies,
        shortest_ladder_queries,
        chillest_ladder_queries,
    ) = parse_data()

    # Find all components
    components = find_components(actors, actor_to_movies, movie_to_actors)
    # Count all components of unique sizes, where size is defined as the number of actors in a component.
    component_sizes = Counter(len(actors) for movies, actors in components)
    # Print the number of components with unique sizes
    print(len(component_sizes))
    for size, count in sorted(component_sizes.items()):
        print(f"There are {count} components of size {size}")

    # Print the answers to the queries about the shortest paths
    for a, b in shortest_ladder_queries:
        print("\t".join(shortest_path(a, b, actor_to_movies, movie_to_actors)))

    # Print the answers to the queries about the chillest paths
    for a, b in chillest_ladder_queries:
        print("\t".join(chillest_path(a, b, movies, actor_to_movies, movie_to_actors)))
