king_point = raw_input()
visit_point = raw_input()

x_distance = int(map(ord,king_point[0])[0]) - int(map(ord,visit_point[0])[0])
y_distance = int(king_point[1]) - int(visit_point[1])

if cmp(abs(x_distance,y_distance)) == -1:
    for i in xrange(abs(x_distance)):

