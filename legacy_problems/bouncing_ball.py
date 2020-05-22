def bouncing_ball(h, bounce, window):
    if h > 0 and 1 > bounce > 0 and window < h:
        num_seen = 1

        while h > window:
            h *= bounce
            print h
            num_seen += 1

        return num_seen
    else:
        return -1


print bouncing_ball(3, 0.66, 1.5)
print bouncing_ball(30, 0.66, 1.5)
print bouncing_ball(3, 1, 1.5)
