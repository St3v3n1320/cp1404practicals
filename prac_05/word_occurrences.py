text = input("Enter a string: ")
text_list = text.split()
text_count_dict = {}

for word in text_list:
    if word in text_count_dict:
        text_count_dict[word] += 1
    else:
        text_count_dict[word] = 1

for word in sorted(text_count_dict):
    print(f"{word} : {text_count_dict[word]}")