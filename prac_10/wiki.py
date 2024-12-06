import wikipedia

def get_wiki_page_details():
    """Prompt the user for a page title or search phrase and print details."""
    while True:
        # Prompt the user for input
        title = input("Enter a Wikipedia page title or search phrase (or press Enter to quit): ")

        # Exit the loop if the user enters a blank input
        if not title:
            print("Exiting program.")
            break

        try:
            # Search and fetch the Wikipedia page using the provided title
            page = wikipedia.page(title, autosuggest=False)

            # Print the title, URL, and summary of the page
            print(f"Page Title: {page.title}")
            print(f"URL: {page.url}")
            print(f"Summary: {page.summary}\n")

        except wikipedia.exceptions.DisambiguationError as e:
            print(f"Disambiguation error: There are multiple options for '{title}'.")
            print(f"Suggestions: {e.options}\n")
        except wikipedia.exceptions.HTTPTimeoutError:
            print("The request timed out. Please try again.")
        except wikipedia.exceptions.RedirectError:
            print(f"The title '{title}' redirects to another page.")
        except wikipedia.exceptions.PageError:
            print(f"Page '{title}' does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}\n")

# Run the function to start the program
if __name__ == "__main__":
    get_wiki_page_details()
