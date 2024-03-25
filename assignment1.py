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

MENU ="""
D - Display movies
A - Add new movie
W - Watch a movie
Q - Quit
"""

from operator import itemgetter


def main():
    print("Welcome to Movie Manager, my name is Yunseo Choi")
    print(MENU)
    movies = load_movies()
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

    save_movies_to_csv(movies)
    print("Movies saved")


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


main()
