import json
from itertools import zip_longest
import sys

with open('../users.csv.txt', 'r', encoding='utf-8') as f:
    users_list = f.read().split('\n')
    with open('../hobby.csv.txt', 'r', encoding='utf-8') as h:
        hobby_list = h.read().split('\n')
        if len(users_list) > len(hobby_list):
            final_list = dict(zip_longest(users_list, hobby_list, fillvalue=None))
        elif len(users_list) < len(hobby_list):
            sys.exit(1)
with open('../task_3.json', 'w', encoding='utf-8') as f:
    json.dump(final_list, f, ensure_ascii=False)
print(final_list)


