def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = f"Sorry, the file {filename} does not exist"
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words")

filenames = ['dogs.txt', 'cats.txt']
for filename in filenames:
    count_words(filename)