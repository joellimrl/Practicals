import wikipedia

def main():
    choice = input("Enter a page title or search phrase: ")
    while choice != "":
        try:
            page = wikipedia.page(choice)
            print(page.title)
            print(page.summary)
            print(page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        choice = input("Enter a page title or search phrase: ")
main()