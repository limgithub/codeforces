
experiments = int(raw_input())
brokens = []
for index in range(experiments):
    broken = []
    f_x,f_y,r1_x_t,r1_y_t,r2_x_t,r2_y_t = map(int,raw_input().split())
    r1_x = r1_x_t - min(r1_x_t,r2_x_t) + 1
    r1_y = r1_y_t - min(r1_y_t,r2_y_t) + 1
    r2_x = r2_x_t - min(r1_x_t,r2_x_t) + 1
    r2_y = r2_y_t - min(r1_y_t,r2_y_t) + 1
    for j in range(f_y - max(r1_y,r2_y) + 1):
        for i in range(f_x - max(r1_x,r2_x) + 1):
            if [r1_x + i,r1_y + j] not in broken:
                broken.append([r1_x + i,r1_y + j])
            if [r2_x + i,r2_y + j] not in broken:
                broken.append([r2_x + i,r2_y + j])

    print f_x * f_y - len(broken)
