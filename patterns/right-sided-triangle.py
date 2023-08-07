word = "anything"
x = 0

for i in word:
    x += 1
    print(word[0:x])
for i in word:
    x = x - 1
    print(word[0:x])