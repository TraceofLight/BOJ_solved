# Basketball One-on-One

score_log = list(input())

score_dict = {
    "A": 0,
    "B": 0,
}
for idx in range(len(score_log) // 2):
    score_dict[score_log[idx * 2]] += int(score_log[idx * 2 + 1])

if score_dict["A"] > score_dict["B"]:
    print("A")
else:
    print("B")
