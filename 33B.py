
S1 = raw_input()
S2 = raw_input()

n = int(raw_input())

m = []
d = ''
m_index = 0

sum_waste = 0

for i in range(n):
    m.append(raw_input().split())


if len(S1) == len(S2):
    for i in range(len(S1)):
        if S1[i] != S2[i]:
            min_waste = 10**10
            for j in range(n):
                if S1[i] in m[j] and S2[i] in m[j]:
                    if int(m[j][2]) < min_waste:
                        min_waste = int(m[j][2])
                        m_index = j
                    
            if min_waste != 10**10:
                sum_waste += min_waste
                d += [S1[i],S2[i]][1- m[m_index].index(S1[i]) % 2]
        else:
            d += S1[i]
    print sum_waste
    print d

else:
    print -1
