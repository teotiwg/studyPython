KB = 1024
totalService = 0

with open('access_log', 'r') as f:
    logs = f.readlines()
    for log in logs:
        log = log.split()
        serviceByte = log[9]
        if serviceByte.isdigit():
            totalService += int(serviceByte)

totalService /= KB
print('총 서비스 용량: %dKB' %totalService)