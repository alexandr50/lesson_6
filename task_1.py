with open('../nginx_logs.txt', 'r', encoding='utf-8') as f:
    list_1 = []
    for i in f.readlines():
        result = i.find('-')
        segment_1 = i[:result - 1]
        result_1 = i.find('"')
        result_2 = i[result_1 + 1:].find('"')
        segment_3 = i[result_1 + 5:result_1 + result_2 - 8]
        segment_2 = i[result_1 + 1:result_1 + 4]
        segment = segment_1, segment_2, segment_3
        list_1.append(segment)
    print(list_1)
