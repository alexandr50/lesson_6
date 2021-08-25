from itertools import zip_longest
import sys
users, hobbys, out = sys.argv[1:]
with open(out, 'w', encoding='utf-8') as f:
    with open(users, encoding='utf-8') as users:
        with open(hobbys, encoding='utf-8') as hobbys:
            num_users = sum(1 for num in users)
            num_hobbys = sum(1 for num in hobbys)
            if num_users < num_hobbys:
                sys.exit(1)
            users.seek(0)
            hobbys.seek(0)
            for line_user, line_user_hobby in zip_longest(users, hobbys):
                f.write((f'{line_user.strip()}: '
                    f'{line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby}\n'))