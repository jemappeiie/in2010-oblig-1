import sys
from collections import defaultdict


def parse_stdin_data():
    input_stream = sys.stdin

    movies = {}
    actors = {}

    movie_to_actors = defaultdict()
    actor_to_movies = defaultdict()

    line = input_stream.readline()

    # Empty input
    if not line:
        return

    # Movies
    number_of_movies = int(line.strip())
    for _ in range(number_of_movies):
        id, title, rating = input_stream.readline().rstrip("\n").split("\t")
        movies[id] = (title, float(rating))

    # Actors
    number_of_actors = int(input_stream.readline().strip())
    for _ in range(number_of_actors):
        id, name = input_stream.readline().rstrip("\n").split("\t")
        actors[id] = name

    # Edges
    number_of_edges = int(input_stream.readline().strip)
    for _ in range(number_of_edges):
        movie_id, actor_id = input_stream.readline().rstrip("\n").split("\t")
        movie_to_actors[movie_id].append(actor_id)
        actor_to_movies[actor_id].append(movie_id)

    # Shortest ladder requests
    number_of_shortest_ladder_requests = int(
        input_stream.readline().rstrip("\n").split("\t")
    )
    shortest_ladder_requests = []
    for _ in range(number_of_shortest_ladder_requests):
        first_actor_id, second_actor_id = (
            input_stream.readline().rstrip("\n").split("\t")
        )
        shortest_ladder_requests.append((first_actor_id, second_actor_id))

    # Chillest ladder requests
    number_of_chillest_ladder_requests = int(
        input_stream.readline().rstrip("\n").split("\t")
    )
    chillest_ladder_requests = []
    for _ in range(number_of_chillest_ladder_requests):
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
