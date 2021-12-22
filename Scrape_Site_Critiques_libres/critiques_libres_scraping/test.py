import json

files=['babelio_reviews.json', 'critiques_libres_reviews.json']

def merge_JsonFiles(filenames):
    result = list()
    for f1 in filenames:
        with open(f1, 'r') as infile:
            result.extend(json.load(infile))

    with open('french_books_reviews', 'w') as output_file:
        json.dump(result, output_file)