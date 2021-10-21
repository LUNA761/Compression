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

file = input("file~ ") # ask for file path input

with open(file) as f: # load the file as a json object
    data = json.load(f)
    f.close()

raw_data, numbers = data["raw"], data["words"] # get the word dictionary and the raw compressed data
decompressed_text = raw_data.replace("/l", "\n") # replace the line break codes with line breaks

for number in reversed(numbers): # replace each number with the correct word in the dictionary (doing this reversed to avoid 1, 2 messing with a number like 100, 200)
    decompressed_text = decompressed_text.replace(number, numbers[number])

for code in number_dict: # replace number codes with numbers
    decompressed_text = decompressed_text.replace(number_dict[code], code)

with open("output.txt", "w+") as f:
    f.write(decompressed_text) # write the output data to the output file.
    f.close()
