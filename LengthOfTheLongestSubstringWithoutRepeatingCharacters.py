# s = "bbbbb"
# demo = []
# max_length = 0
# start = 0
#
# for i in range(len(s)):
#     while s[i] in demo:
#         demo.pop(0)
#         start += 1
#     demo.append(s[i])
#     max_length = max(max_length, len(demo))
#
# print(max_length)


s = "welcome to python program"
x1 = s.split(" ")
max_unique_count = 0
longest_words = []

for word in x1:
    unique_chars = set(word)
    unique_count = len(unique_chars)

    if unique_count > max_unique_count:
        max_unique_count = unique_count
        longest_words = [word]
    elif unique_count == max_unique_count:
        longest_words.append(word)

print(f"The words with the most unique characters are: {longest_words}")






