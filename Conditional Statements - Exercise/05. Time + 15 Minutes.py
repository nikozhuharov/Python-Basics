hours = int(input())
minutes = int(input())

if minutes < 45:
    minutes = minutes + 15
    print(f"{hours}:{minutes}")
else:
    minutes = minutes - 45
    hours = hours + 1
    if hours < 24:
        if minutes < 10:
            print(f"{hours}:0{minutes}")
        else:
            print(f"{hours}:{minutes}")
    else:
        hours = 0
        if minutes < 10:
            print(f"{hours}:0{minutes}")
        else:
            print(f"{hours}:{minutes}")





