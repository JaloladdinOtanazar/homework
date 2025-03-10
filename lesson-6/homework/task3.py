import os
import string
from collections import Counter
def check(filename):
    if not os.path.exists(filename):
        print(f"{filename} not found and create one with new text")
        text = input("Enter text: ")
        with open(filename, "w") as f:
            f.write(text)
        return
def counting(filename):
    with open(filename, "r") as f:
        text = f.read()
    translator = str.maketrans("", "", string.punctuation)
    words = text.translate(translator).lower().split()
    word_count = Counter(words)
    return word_count
def save(word_count, new_file):
    total_words = sum(word_count.values())
    top_words = word_count.most_common(5)
    with open(new_file, "w") as f:
        f.write("word cound report\n")
        f.write(f"total words: {total_words}\n")
        f.write("top 5 words\n")
        for word, count in top_words:
            f.write(f"{word} - {count}\n")
def main():
    file = "sample.txt"
    new_file = "word_count_report.txt"
    check(file)
    word_count = counting(file)
    total_words = sum(word_count.values())
    top_words = word_count.most_common(5)
    print(f"total words: {total_words}\n")
    print(f"top 5 common words: {top_words}")
    for word, count in top_words:
        print(f" {word} and its occurence is {count}")
    save(word_count, new_file)
    print(f"report saved to {new_file}")
if __name__ == "__main__":
    main()


    