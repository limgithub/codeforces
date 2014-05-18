r = lambda: map(int,raw_input().split())

n,speed_b,speed_s = r()
stations = r()
position_x, position_y = r()
mi = 0
m = 10 ** 10
Distance = ( position_x ** 2 + position_y ** 2) ** 0.5

for i,c in enumerate(stations[1:],2):
    distance = (position_y ** 2 + (position_x - c) ** 2) ** 0.5
    t = distance / speed_s + c * 0.1 / speed_b
    if t < m or  t == m and distance < D:
        mi = i
        Distance = distance
        m = t

print mi
