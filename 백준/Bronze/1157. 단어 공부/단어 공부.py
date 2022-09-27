from os import remove


word = input()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = list(alphabet)
output = []
for i in range(26) : # 알파벳별 사용횟수 정리
    output.append(0)
word_element = list(word)
word_ascii = [ord(i) for i in word_element]
for j in range(len(word_ascii)) : # 알파벳 맞춰 코드 정리
    if word_ascii[j] > 90 :
        word_ascii[j] = word_ascii[j] - 97
    else :
        word_ascii[j] = word_ascii[j] - 65
    number = int(word_ascii[j])
    output[number] = output[number] + 1
first_output = output
max_first = max(first_output)
index = output.index(max(output))
output[index] = 0
max_last = max(output)
if max_first == max_last : # 최대 사용 알파벳 다수 거름망
    print('?')
else :
    print(alphabet[index])