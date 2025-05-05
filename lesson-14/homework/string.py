import json
with open('student.json','r') as file:
    data=json.load(file)
for student in data['students']:
    print(f"Name:{student['name']},Age :{student['age']}, Grade:{student['grade']}")
import requests

# Replace with your actual OpenWeatherMap API key
API_KEY = 'your_api_key'
CITY = 'Tashkent'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

# Fetch weather data
response = requests.get(URL)
data = response.json()

# Check the status code and raw response
if response.status_code == 200:
    print("API request successful!")
    
    # Debugging: print the raw JSON response
    print("Raw data response:", data)
    
    # Now access the relevant fields if they exist
    try:
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']
        
        # Print weather details
        print(f"Weather in {CITY}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description}")
    except KeyError as e:
        print(f"KeyError: {e}. This might indicate a problem with the API response structure.")
else:
    print(f"Error fetching weather data: {response.status_code}")
    print("Response content:", data)

import json
import os

def load_books():
    if not os.path.exists("books.json"):
        return []
    with open("books.json", "r") as file:
        return json.load(file)

def save_books(books):
    with open("books.json", "w") as file:
        json.dump(books, file, indent=4)

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    year = input("Enter year: ")
    books = load_books()
    books.append({"title": title, "author": author, "year": year})
    save_books(books)
    print("Book added successfully.")

def update_book():
    title = input("Enter the title of the book to update: ")
    books = load_books()
    for book in books:
        if book["title"].lower() == title.lower():
            book["author"] = input("Enter new author: ")
            book["year"] = input("Enter new year: ")
            save_books(books)
            print("Book updated successfully.")
            return
    print("Book not found.")

def delete_book():
    title = input("Enter the title of the book to delete: ")
    books = load_books()
    updated_books = [book for book in books if book["title"].lower() != title.lower()]
    if len(books) == len(updated_books):
        print("Book not found.")
    else:
        save_books(updated_books)
        print("Book deleted successfully.")

def main():
    while True:
        print("\n1. Add Book\n2. Update Book\n3. Delete Book\n4. View All Books\n5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            books = load_books()
            for book in books:
                print(book)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

main()

import requests
import random

# Your OMDB API Key
API_KEY = 'your_api_key_here'  # Replace with your actual OMDb API key

# Function to search for movies using a genre keyword
def get_movies_by_genre(genre):
    url = f'http://www.omdbapi.com/?apikey={API_KEY}&s={genre}&type=movie'
    response = requests.get(url)
    data = response.json()

    if data.get('Response') == 'True':
        return data.get('Search', [])
    else:
        print(f"Error: {data.get('Error', 'Unknown error')}")
        return []

# Function to get detailed movie info using imdbID
def get_movie_details(imdb_id):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&i={imdb_id}&plot=short"
    response = requests.get(url)
    return response.json()

# Function to recommend a random movie
def recommend_movie(genre):
    movies = get_movies_by_genre(genre)
    if movies:
        random_movie = random.choice(movies)
        details = get_movie_details(random_movie['imdbID'])
        
        print(f"\n🎬 Here's a movie you might like from the '{genre}' genre:")
        print(f"Title       : {details.get('Title')}")
        print(f"Year        : {details.get('Year')}")
        print(f"Genre       : {details.get('Genre')}")
        print(f"IMDB Rating : {details.get('imdbRating')}")
        print(f"Plot        : {details.get('Plot')}")
    else:
        print("No movies found for that genre or search term.")

# Main function to run the script
def main():
    print("🎥 Welcome to the Movie Recommendation System!")
    genre = input("Enter a movie genre (e.g., action, comedy, drama): ").strip().lower()
    recommend_movie(genre)

if __name__ == '__main__':
    main()
