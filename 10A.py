n,P1,P2,P3,T1,T2 = map(int,raw_input().split())

time_periods = []
energy_cons = 0
begin_now = 0
end_last = 100 ** 100

for i in range(n):
    time_periods.append(map(int,raw_input().split()))
    begin_now = time_periods[i][0]
    energy_cons += (time_periods[i][1] - time_periods[i][0]) * P1
    if begin_now > end_last:
        if begin_now - end_last <= T1:
            energy_cons += (begin_now - end_last) * P1
        elif begin_now - end_last <= (T1 + T2):
            energy_cons += (begin_now - end_last - T1) * P2 + T1 * P1
        else:
            energy_cons += (begin_now - end_last - T1 - T2) * P3 + T1 * P1 + T2 * P2
    end_last = time_periods[i][1]

print energy_cons

