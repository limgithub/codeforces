import ipdb

target_point = abs(int(raw_input()))

n = 0
while target_point > ((1 + n) * n / 2):
    n = n + 1
ipdb.set_trace()
n = n + 1
if target_point == ((n-1) * n / 2):
    print n - 1
else:
    if target_point < ((1 + n) * n / 2):
        if (((1 + n) * n / 2) - target_point) % 2 == 0:
            print n
        else:
            print n + 1
