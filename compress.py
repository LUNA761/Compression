import json, os

os.chdir("static")

number_dict = { # just an easy way to avoid number problems, it replaces all numbers with codes.
    "1": "/no",
    "2": "/nt",
    "3": "/nth",
    "4": "/nf",
    "5": "/nfi",
    "6": "/ns",
    "7": "/nse",
    "8": "/ne",
    "9": "/nn",
    "0": "/nz"
}

# <--- funcs --->

def get_word_dict(string): # This function returns a dictionary of the words that are used more than once
    word_num = {}
    for part in list(set(string.split(' '))):
        if string.count(part) != 1:
            if len(part) > 2:
                word_num[part] = string.count(part)

    return word_num

def compress_string_with_word_dict(words, string): # This function will compress a string using the word dictionary returned by the funcion above.
    word_numbers = {}
    num = 0

    for word in words:
        num += 1
        word_numbers[str(num)] = word

    compressed_text = string

    for code in number_dict:
        compressed_text = compressed_text.replace(code, number_dict[code])

    for num in word_numbers:
        compressed_text = compressed_text.replace(word_numbers[num], str(num))

    return compressed_text, word_numbers

def read_file_and_remove_lines(file): # this will replace any line breaks with a code.
    with open(file) as f:
        lines = f.readlines()
        f.close()

    raw_text = ""
    num = 0

    for line in lines:
        num += 1

        if num == len(lines):
            raw_text += line
        else:
            raw_text += line+"/l"

    return ''.join(raw_text.splitlines())

# <--- run --->

while 1:
    file = input("File Path ~ ") # ask for a file path input

    print("Loading File...")

    filename, ext = file.split(".")[0], file.split(".")[1] # get the filename and extention from the path

    compressed_filename = filename+"-compressed."+ext # generate filenames
    words_filename = filename+"-words."+ext # generate filenames
    numbers_filename = filename+"-numbers.json" # generate filenames

    raw_data = read_file_and_remove_lines(file) # refer to the function

    print("Formatting File...")

    words = get_word_dict(raw_data) # refer to the function

    print("Loading words...")

    #with open(words_filename, "w+") as f:                      IGNORE THIS
    #    f.write(str(words))
    #    f.close()

    compressed_text, word_numbers = compress_string_with_word_dict(words, raw_data) # refer to the function

    print("Compressing File...")

    #with open(numbers_filename, "w+") as f:                    IGNORE THIS
    #    json.dump(word_numbers, f)
    #    f.close()

    output_file_data = { # i decided to format the output file (the compressed file) using json.
        "raw": str(compressed_text),
        "words": word_numbers
    }

    print("Loading Output...")

    with open(compressed_filename, "w+") as f: # write to the output file.
        json.dump(output_file_data, f)
        f.close()

    print("Saved...\n")
