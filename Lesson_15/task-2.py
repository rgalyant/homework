from argparse import FileType
from io import TextIOWrapper


def longest_words(file):
    longest = [""]

    while True:
        line = file.readline()[:-1]
        if not line: break

        words = line.split()
        for word in words:
            if len(word) >= len(longest[0]) and word not in longest:
                if len(word) > len(longest[0]):
                    longest = []
                longest.append(word)
    
    if len(longest[0]) == 0:
        longest = []
    
    return longest

if __name__ == "__main__":
    with open("article.txt", "rt", encoding="utf-8") as file:
        print("Longest words:", ",".join(longest_words(file)))