# 알파벳 개수

chr_list = list(input())
count_list = [0 for _ in range(26)]

for each_chr in chr_list:
    count_list[ord(each_chr) - 97] += 1
    
print(*count_list)