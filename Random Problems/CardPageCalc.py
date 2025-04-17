def calculate_pages_needed(total_cards, cards_per_page=18):
    """
    Calculate the number of pages needed to store a given number of cards.

    Parameters:
    total_cards (int): The total number of cards.
    cards_per_page (int): The number of cards a single binder page can hold (default is 18).

    Returns:
    int: The number of pages needed.
    """
    return (total_cards + cards_per_page - 1) // cards_per_page


def main():
    """
    Main function to take input and display the result.
    """
    while True:
        total_cards = input("Enter the total number of cards in the set: ")

        if total_cards.isdigit():
            total_cards = int(total_cards)
            if total_cards > 0:
                break
            else:
                print("The number of cards must be a positive integer!")
        else:
            print("The number of cards must be a valid integer!")

    # Call the calculation function
    pages_needed = calculate_pages_needed(total_cards)

    # Display the result
    print(f"You will need {pages_needed} page(s) to store all the cards.")



# Execute the program
if __name__ == "__main__":
    main()
