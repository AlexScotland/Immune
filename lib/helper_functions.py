from datetime import datetime, timedelta

def collision_detection(x1, y1, x2, y2, r1, r2):
    distSq = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
    radSumSq = (r1 + r2) * (r1 + r2)
    if (distSq == radSumSq):
        return True
    elif (distSq > radSumSq):
        return False
    else:
        return True

def has_time_passed(last_spawn, delay):
    right_now = datetime.now()
    future_date = last_spawn + timedelta(days = 0, seconds = delay)
    if right_now > future_date:
        return True
    return False

def get_center_coordinates_of_cirle(x_coord, y_coord, size):
    left_side_x = x_coord - size/2
    right_side_x = x_coord + size/2
    top_side_y = y_coord - size/2
    bottom_side_y = y_coord + size/2
    return [int(left_side_x + right_side_x) / 2, int(top_side_y + bottom_side_y) / 2]

def check_if_host_infected(host, list_of_viruses):
    for virus in list_of_viruses:

        if virus.protein == host.protein:
            return virus
    return False

def infect_hosts(host1, host2):
    for virus in host2.viruses:
        if virus.protein == host1.protein:
            host1._infect(virus)
            print(f"Host with protein {host1.protein} has been infected")
            return

def infect_touching_hosts(list_of_hosts, threshold=2):
    for i in range(len(list_of_hosts)):
        current_host = list_of_hosts[i]
        for j in range(i+1, len(list_of_hosts)):
            next_host = list_of_hosts[j]
            if current_host.sick or next_host.sick:
                # calculate the overlap between the two objects
                overlap_width = min(current_host.x + current_host.size, next_host.x + next_host.size) - max(current_host.x, next_host.x)
                overlap_height = min(current_host.y + current_host.size, next_host.y + next_host.size) - max(current_host.y, next_host.y)
                # check if the overlap is larger than the threshold
                if overlap_width > threshold and overlap_height > threshold:
                    infect_hosts(current_host, next_host)
                    continue
                    

        