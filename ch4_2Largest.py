size = int(input(" "))

scores_input = input(" ")

scores = [int(x) for x in scores_input.split()]
score = list(set(scores))
score.sort(reverse=True)

print(score[1])
