def solution(dirs):
    answer = 0
    cursor_x = 0
    cursor_y = 0
    direction_arr = []
    for dir in dirs:
        if dir == "U":
            if cursor_y <5:
                direction_arr.append((cursor_x,cursor_y,cursor_x,cursor_y+1))
                cursor_y +=1
        elif dir == "R":
            if cursor_x <5:
                direction_arr.append((cursor_x,cursor_y,cursor_x+1,cursor_y))
                cursor_x +=1
        elif dir == "D":
            if cursor_y>-5:
                direction_arr.append((cursor_x,cursor_y-1,cursor_x,cursor_y))
                cursor_y -= 1
        elif dir == "L":
            if cursor_x>-5:
                direction_arr.append((cursor_x-1,cursor_y,cursor_x,cursor_y))
                cursor_x -= 1
    direction_set = set(direction_arr)
    return len(direction_set)