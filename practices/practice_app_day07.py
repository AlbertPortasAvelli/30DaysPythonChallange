class MovieManager:
    def __init__(self):
        self.movies = {}  # Dictionary to store movies where keys are movie names and values are sets of genres

    def add_movie(self, movie, genres):
        # Add a movie to the list with associated genres
        self.movies[movie] = set(genres)
        print(f"Movie '{movie}' added with genres: {', '.join(genres)}")

    def add_genre(self, movie, new_genre):
        # Add a new genre to an existing movie
        if movie in self.movies:
            self.movies[movie].add(new_genre)
            print(f"Genre '{new_genre}' added to the movie '{movie}'.")
        else:
            print(f"Movie '{movie}' not found.")

    def view_movies_by_genre(self, genre):
        # View movies belonging to a specific genre
        matching_movies = [movie for movie, genres in self.movies.items() if genre in genres]
        if matching_movies:
            print(f"Movies in genre '{genre}': {', '.join(matching_movies)}")
        else:
            print(f"No movies found in genre '{genre}'.")

# Example usage
movie_manager = MovieManager()

movie_manager.add_movie("Inception", ["Sci-Fi", "Thriller"])
movie_manager.add_movie("The Shawshank Redemption", ["Drama"])
movie_manager.add_movie("The Dark Knight", ["Action", "Crime", "Drama"])

movie_manager.view_movies_by_genre("Sci-Fi")

movie_manager.add_genre("Inception", "Mystery")
movie_manager.view_movies_by_genre("Mystery")

movie_manager.view_movies_by_genre("Drama")

movie_manager.add_movie("Interstellar", ["Sci-Fi", "Adventure"])
movie_manager.view_movies_by_genre("Adventure")
