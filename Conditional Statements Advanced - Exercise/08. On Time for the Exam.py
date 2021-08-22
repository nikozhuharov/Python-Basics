hour_start = int(input())
minute_start = int(input())
hour_arrive = int(input())
minute_arrive = int(input())

ms = hour_start*60 + minute_start
ma = hour_arrive*60 + minute_arrive

diff = ms - ma

if diff > 30:
    print("Early")
    if diff > 59:
        hl = diff // 60
        ml = diff % 60
        if ml < 10:
            print(f"{hl}:0{ml} hours before the start")
        else:
            print(f"{hl}:{ml} hours before the start")
    else:
        print(f"{diff} minutes before the start")

if 30 >= diff >= 0:
    print("On time")
    if diff != 0:
        print(f"{diff} minutes before the start")

if diff < 0:
    print("Late")
    diff = - diff
    if diff > 59:
        hl = diff // 60
        ml = diff % 60
        if ml < 10:
            print(f"{hl}:0{ml} hours after the start")
        else:
            print(f"{hl}:{ml} hours after the start")
    else:
        print(f"{diff} minutes after the start")

