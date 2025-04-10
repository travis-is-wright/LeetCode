import requests
def get_book_details(book_name, api_key):
    """
    Fetches book details from the Google Books API.

    Parameters:
    book_name (str): The name of the book to search for.
    api_key (str): Your Google Books API key.

    Returns:
    list: A list of dictionaries containing book titles, page counts, and preview links.
    """
    url = f"https://www.googleapis.com/books/v1/volumes?q={book_name}&maxResults=10&key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "items" in data:
            books = []
            for item in data["items"]:
                book = item["volumeInfo"]
                books.append({
                    "title": book.get("title", "Unknown Title"),
                    "page_count": book.get("pageCount", "Unknown"),
                    "preview_link": book.get("previewLink", "No preview available"),
                })
            return books
        else:
            return None  # No books found
    else:
        return f"API request failed with status code {response.status_code}"


def main():
    """
    Main function to interact with the user.
    """
    api_key = "AIzaSyB8GZ7wFlGsCExG5Ccdz3pgwswjooO7zV0"
    book_name = input("Enter the name of the book: ")
    books = get_book_details(book_name, api_key)

    if isinstance(books, str):  # API request failed
        print(books)
        return

    if not books:
        print("No books found.")
        return

    # Check for an exact match
    exact_match = next((book for book in books if book_name.lower() == book["title"].lower()), None)

    if exact_match:
        # Display details of the exact match
        print(f"Exact Match Found:")
        print(f"Title: {exact_match['title']}")
        print(f"Page Count: {exact_match['page_count']}")
        print(f"Preview Link: {exact_match['preview_link']}")
    else:
        # Display the top 10 search results
        print(f"No exact match found. Showing the top {len(books)} results:")
        for idx, book in enumerate(books, 1):
            print(f"{idx}. Title: {book['title']}")
            print(f"   Page Count: {book['page_count']}")
            print(f"   Preview Link: {book['preview_link']}")
            print()


if __name__ == "__main__":
    main()
