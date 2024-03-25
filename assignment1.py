"""
Name: yunseo choi
Date started: march 21 2024
GitHub URL (of this assignment): https://github.com/cp1404-students/a1-movies2see-zzzczzzz/tree/feedback
Remember to NEVER make this assignment repo public
"""


MENU = """ Menu:
D - Display movies
A - Add new movie
W - Watch a movie
Q - Quit
"""


def main():
    print("Welcome to Movie Manager!")
    movies = load_movies()
    choice = input("Enter your choice: ").upper()
    while choice != "Q":
        print(MENU)

        if choice == "D":
            display_movies(movies)
        elif choice == "A":
            add_movie(movies)
        elif choice == "W":
            watch_movie(movies)
        else:
            print("Invalid input")
        choice = input("Enter your choice: ").upper()

    save_movies_to_csv(movies)
    print("Movies saved")


def load_movies:
    in_file = open('movies.csv', 'r')

main()
