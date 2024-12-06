import wikipedia

def get_wiki_page_details():
    """Prompt the user for a page title or search phrase and print details."""
    while True:
        # Prompt the user for input
        title = input("Enter page title: ").strip()

        # Exit the loop if the user enters a blank input
        if not title:
            print("Thank you.")
            break

        try:
            # Attempt to fetch the page
            page = wikipedia.page(title, autosuggest=False)

            # Print the page details: Title, Summary, and URL
            print(f"\n{page.title}")
            print(f"{page.summary[:500]}...")  # Limit summary output for readability
            print(page.url)

        except wikipedia.exceptions.DisambiguationError as e:
            # Handle ambiguous search queries
            print("\nWe need a more specific title. Try one of the following, or a new search:")
            print(e.options[:10])  # Display the first 10 suggestions

        except wikipedia.exceptions.PageError:
            # Handle cases where no page is found
            print(f"\nPage id \"{title}\" does not match any pages. Try another id!")

        except Exception as e:
            # Handle unexpected errors
            print(f"\nAn unexpected error occurred: {e}")


# Run the function to start the program
if __name__ == "__main__":
    get_wiki_page_details()
