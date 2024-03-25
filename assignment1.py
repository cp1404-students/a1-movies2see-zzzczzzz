"""
Name: yunseo choi
Date started: march 21 2024
GitHub URL (of this assignment): https://github.com/cp1404-students/a1-movies2see-zzzczzzz/tree/feedback
Remember to NEVER make this assignment repo public
"""

"""
MENU = D - Display movies
A - Add new movie
W - Watch a movie
Q - Quit

main
    function load file, store as list of lists and sort
    
    choice input, d, a, w, or q others considered error, do error check
    
    if choice is d
        display function
        display movies, with symbols following wathced, print number of unwatched moves and watched
    
    if choice is a
    add movie functoin, ask user for information on movies
    do error check on each variable, do error check to get valid input
    add the new movie to list of lists
    
    if choice is w
    ask user input for which movie to watch, do error check to get valid input, cannot watch whatced one
    mark unwatched as watched if user input is certain unwatched movie
    
    if choice is q
    save the movie list to movies.csv, overwrite it
    print bye
"""

MENU = """
D - Display movies
A - Add new movie
W - Watch a movie
Q - Quit
"""

from operator import itemgetter


def main():
    """main function structures the program, directs to functions in each option"""
    movies = load_movies()
    print("Welcome to Movie Manager, my name is Yunseo Choi")
    print(f"{len(movies)} movies loaded")
    print(MENU)
    choice = input("Enter your choice: ").upper()
    while choice != "Q":

        if choice == "D":
            display_movies(movies)
        elif choice == "A":
            add_movie(movies)
        elif choice == "W":
            watch_movie(movies)
        else:
            print("Invalid input")

        print(MENU)

        choice = input("Enter your choice: ").upper()

    save_movies(movies)
    print(f"{len(movies)} saved")


def load_movies():
    """Load file from csv, save as list sorted by year"""
    movies = []
    in_file = open('movies.csv', 'r')
    for line in in_file:
        movie = line.strip().split(',')
        movie[1] = int(movie[1])
        movies.append(movie)

    in_file.close()
    movies.sort(key=itemgetter(1))
    return movies


def display_movies(movies):
    """display movies, count number of unwatched and watched, display them"""
    watched_count = 0
    unwatched_count = 0

    maximum_title_length = max(len(movie[0]) for movie in movies)

    for i, movie in enumerate(movies):
        if movie[3] == 'w':
            watched_count += 1
            watch_symbol = " "
        else:
            unwatched_count += 1
            watch_symbol = "*"

        print(f"{i}. {watch_symbol} {movie[0]:<{maximum_title_length}} - {movie[1]} ({movie[2]})")

    print(f"{watched_count} movies watched, {unwatched_count} movies still to watch")


def add_movie(movies):
    """Gets input about movies, performs error checks, and stores them as a list of lists."""

    movie_title = input("Title : ").strip().title()
    while movie_title == "":
        print("Title cannot be empty.")
        movie_title = input("Title: ").strip().title()

    movie_year = input("Year: ").strip()
    while movie_year == "" or not movie_year.strip('-').isdigit() or int(movie_year) < 0:
        if movie_year == "":
            print("Year cannot be empty.")
        elif not movie_year.strip('-').isdigit():
            print("Year must be an integer.")
        elif int(movie_year) < 0:
            print("Year must be positive")
        movie_year = input("Year: ").strip()

    movie_category = input("Category: ").strip()
    while movie_category == "":
        print("Category cannot be empty.")
        movie_category = input("Category: ").strip()

    new_movie = [movie_title, movie_year, movie_category, 'u']
    movies.append(new_movie)

    print(f"{movie_title} ({movie_category} from {movie_year}) added to the movie list")


def watch_movie(movies):
    """Ask the user for valid input, mark selected movie as watched, and print error if all movies have been watched."""
    unwatched_movies = [movie for movie in movies if movie[3] == 'u']

    if unwatched_movies:
        movie_number = get_valid_input_watch("Enter the number of a movie to mark as watched : ", movies)
        if movie_number < len(movies):
            selected_movie = movies[movie_number]
            if selected_movie[3] == 'u':
                print(f"{selected_movie[0]} from {selected_movie[1]} watched")
                selected_movie[3] = 'w'
            else:
                print(f"{selected_movie[0]} from {selected_movie[1]} already watched")
    else:
        print("No more movies to watch!")


def save_movies(movies):
    """save movies to file movies.csv"""
    out_file = open('movies.csv', 'w')
    for movie in movies:
        movie_str = [str(item) for item in movie]
        out_file.write(','.join(movie_str) + '\n')
    out_file.close()


def get_valid_input_watch(prompt, movies):
    """Get a valid movie input"""
    user_input = input(prompt)
    while user_input != "":
        if not user_input.strip('-').isdigit():
            print("Input must be an integer.")
        elif int(user_input) < 0:
            print("Input must be a positive integer.")
        elif int(user_input) >= len(movies):
            print("Invalid movie number")
        else:
            return int(user_input)

        user_input = input(prompt)


main()
