with open('stockcode.txt', 'r') as f: # 자동으로 닫아줌
    for line_num, line in enumerate(f.readlines()):
        print(' %d %s' %(line_num+1, line), end='')