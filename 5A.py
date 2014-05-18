import sys

send_length = 0
on_num = 0

for s in sys.stdin:
    if '+' in s:
        on_num = on_num + 1
    elif '-' in s: 
        on_num = on_num - 1
    else:
        send_length = send_length + on_num * (len(s) - s.find(':') - 2)

print send_length
