import wikipedia
import warnings
warnings.filterwarnings("ignore")

search = input("Search Wiki: ")
while search is not '':
    try:
        summary = wikipedia.summary(search)
        print(summary)

    except wikipedia.exceptions.DisambiguationError as e:
        print("Please pick one of the following:\r\n")
        [print(option) for option in e.options]

    search = input("Search Wiki: ")
