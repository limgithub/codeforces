score_table = {}
score_his = []

n = int(raw_input())

for i in xrange(n):
    name,score = raw_input().split()
    if name in score_table.keys():
        score_table[name] = score_table[name] + int(score)
    else:
        score_table[name] = int(score)
    
    score_his.append((name,score_table[name]))

max_value = max(score_table.values())

for name,score in score_his:
    if max_value == score:
        print name
        break

