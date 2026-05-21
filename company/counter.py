def visits_counter():
    with open('E:\web-prog\Lab2-KB-309-10-Павлюк\company\counter.txt', 'r') as f:
        count = int(f.read())
    count += 1
    with open('E:\web-prog\Lab2-KB-309-10-Павлюк\company\counter.txt', 'w') as f:
        f.write(str(count))
    return count