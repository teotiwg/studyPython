visitIp = []

with open('access_log', 'r') as f:
    logs = f.readlines()
    for log in logs:
        log = log.split()
        ip = log[0]
        if ip not in visitIp:
            visitIp.append(ip)

print('방문자 수: [%d]' %len(visitIp))