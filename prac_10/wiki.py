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
            print(f"\nPage Title: {page.title}")
            print(f"URL: {page.url}")
            print(f"Summary: {page.summary[:500]}...\n")  # Print only the first 500 characters of the summary

        except wikipedia.exceptions.DisambiguationError as e:
            print(f"\nDisambiguation error: '{title}' has multiple possible meanings.")
            print("Here are some suggestions:")
            print("\n".join(e.options[:10]))  # Show up to 10 suggestions
            print("\nTry refining your search.\n")
        except wikipedia.exceptions.PageError:
            print(f"\nPageError: The page '{title}' does not exist on Wikipedia.\n")
        except wikipedia.exceptions.HTTPTimeoutError:
            print("\nThe request timed out. Please check your connection and try again.\n")
        except wikipedia.exceptions.RedirectError:
            print(f"\nRedirectError: The page '{title}' redirects to another page. Please try a more specific title.\n")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}\n")

# Run the function to start the program
if __name__ == "__main__":
    get_wiki_page_details()
