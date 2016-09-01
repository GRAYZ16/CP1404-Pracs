input_text = input("Text: ")

while input_text == "":
    print("Invalid Input")
    input_text = input_text = input("Text: ")

formatted_input = input_text.strip().lower().split()
word_counts = {}

for word in formatted_input:
    word_counts[word] = formatted_input.count(word)

print(word_counts)

longest_word_length = 0

for key in word_counts:
    if len(key) > longest_word_length:
        longest_word_length = len(key)


for key, value in sorted(word_counts.items()):
    print("{:{}} : {}".format(key, longest_word_length, value))