#Movie Recommendation System
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def load_dataset():
    data = {
        "user": [1, 1, 2, 2, 3, 3, 4, 4],
        "movie": [
            "Inception", "Interstellar",
            "Inception", "The Dark Knight",
            "Interstellar", "Memento",
            "Inception", "Memento"
        ],
        "rating": [5, 4, 4, 5, 5, 4, 3, 5]
    }
    return pd.DataFrame(data)


def create_rating_matrix(ratings):
    return ratings.pivot_table(
        index="user",
        columns="movie",
        values="rating",
        fill_value=0
    )


def calculate_similarity(matrix):
    similarity = cosine_similarity(matrix)
    return pd.DataFrame(similarity, index=matrix.index, columns=matrix.index)


def recommend_movies(user_id, ratings_matrix, user_similarity):
    similar_users = user_similarity[user_id].sort_values(ascending=False).index[1:]
    recommendations = {}

    for similar_user in similar_users:
        for movie, rating in ratings_matrix.loc[similar_user].items():
            if ratings_matrix.loc[user_id, movie] == 0 and rating > 0:
                recommendations[movie] = recommendations.get(movie, 0) + rating

    return sorted(recommendations.items(), key=lambda x: x[1], reverse=True)

def main():
    print("Welcome to the Movie Recommendation System")

    ratings = load_dataset()
    ratings_matrix = create_rating_matrix(ratings)
    user_similarity = calculate_similarity(ratings_matrix)

    print(f"Available users: {list(ratings_matrix.index)}")

    user_id = int(input("Enter user ID: "))

    if user_id not in ratings_matrix.index:
        print("User ID not found. Please try again.")
        return

    recommendations = recommend_movies(user_id, ratings_matrix, user_similarity)

    print("\nRecommended Movies:")
    if recommendations:
        for movie, score in recommendations:
            print(f"- {movie} (score: {score})")
    else:
        print("No recommendations available.")

if __name__ == "__main__":
    main()
