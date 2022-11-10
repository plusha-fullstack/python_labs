sentence = "Mary amore and adida Gogi go for await walk."
capacity = int(input("ЧИсло: "))
sentence = sentence[:len(sentence)-1]
sentence = sentence.split()
print(sentence)
i = 0
while i < len(sentence):
    ele = sentence[i]
    if len(ele) != capacity or ele[0] != 'a':
        sentence.remove(ele)
        continue
    i += 1

sentence.sort()
print(sentence)
