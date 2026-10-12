import sys
from collections import defaultdict


def debug(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    debug("Dette er et eksempel på å printe debug info. Du kan slette denne linjen")
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

    # Shortest ladder requests
    Qs = int(input_stream.readline().strip())
    shortest_ladder_requests = []
    for _ in range(Qs):
        first_actor_id, second_actor_id = (
            input_stream.readline().rstrip("\n").split("\t")
        )
        shortest_ladder_requests.append((first_actor_id, second_actor_id))

    # Chillest ladder requests
    Qc = int(input_stream.readline().strip())
    chillest_ladder_requests = []
    for _ in range(Qc):
        first_actor_id, second_actor_id = (
            input_stream.readline().rstrip("\n").split("\t")
        )
        chillest_ladder_requests.append((first_actor_id, second_actor_id))

    return (
        movies,
        actors,
        movie_to_actors,
        actor_to_movies,
        shortest_ladder_requests,
        chillest_ladder_requests,
    )


if __name__ == "__main__":
    (
        movies,
        actors,
        movie_to_actors,
        actor_to_movies,
        shortest_ladder_requests,
        chillest_ladder_requests,
    ) = main()
    for m in movies:
        print(m)
