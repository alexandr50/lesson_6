from collections import Counter
with open('../nginx_logs.txt', 'r', encoding='utf-8') as f:
    list_1 = []
    for i in f.readlines():
        result = i.find('-')
        segment_1 = i[:result - 1]
        list_1.append(segment_1)
    n = Counter(list_1).most_common()
    print(n[0])