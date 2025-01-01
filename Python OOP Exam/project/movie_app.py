from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def finding_user(self, username: str):
        user = [u for u in self.users_collection if u.username == username]
        if user:
            return user[0]

    def check_if_movie_exists(self, title):
        for movie in self.movies_collection:
            if movie.title == title:
                return True
        return False

    def register_user(self, username: str, age: int):
        searched_user = self.finding_user(username)
        if searched_user:
            raise Exception("User already exists!")

        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        searched_user = self.finding_user(username)

        if not searched_user:
            raise Exception("This user does not exist!")

        if searched_user != movie.owner:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        self.movies_collection.append(movie)
        searched_user.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        searched_user = self.finding_user(username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if searched_user != movie.owner:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for k, v in kwargs.items():
            setattr(movie, k, v)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        searched_user = self.finding_user(username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if searched_user != movie.owner:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        searched_user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        searched_user = self.finding_user(username)

        if searched_user == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        liked_movie = [m for m in searched_user.movies_liked if m.title == movie.title]
        if liked_movie:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        searched_user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        searched_user = self.finding_user(username)
        liked_movie = [m for m in searched_user.movies_liked if m.title == movie.title]

        if not liked_movie:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        searched_user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        result = sorted(self.movies_collection, key=lambda m: (-m.year, m.title))
        return '\n'.join([m.details() for m in result])

    def __str__(self):
        if not self.users_collection:
            result = "All users: No users.\n"
        else:
            result = f"All users: {', '.join([u.username for u in self.users_collection])}" + "\n"

        if not self.movies_collection:
            result += "All movies: No movies."

        else:
            result += f"All movies: {', '.join([m.title for m in self.movies_collection])}"

        return result







