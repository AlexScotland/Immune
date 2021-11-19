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
