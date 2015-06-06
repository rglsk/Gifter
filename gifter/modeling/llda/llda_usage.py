from gifter.modeling.data import lemmatized_frame


def count_words(lemmatized_words):
    return {word: lemmatized_words.count(word) for word in lemmatized_words}


def main():
    tweets = lemmatized_frame('../data/data.json')


if __name__ == '__main__':
    main()
