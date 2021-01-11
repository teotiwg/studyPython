services = []

with open('access_log', 'r') as f:
    logs = f.readlines()
    for log in logs:
        log = log.split()
        ip = log[0]
        serviceByte = log[9]
        if serviceByte.isdigit():
            serviceByte = int(serviceByte)
        else:
            serviceByte = 0

        if ip not in services:
            services[ip] = serviceByte
        else:
            services[ip] += serviceByte

ret = sorted(services.items(), key = lambda x:x[1], reverse=True)

print('사용자IP = 서비스 용량')
for ip, b in ret:
    print('[%s] - [%d}' %(ip, b))