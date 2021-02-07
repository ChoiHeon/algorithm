# https://programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    import re

    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9\-_.]', '', new_id)
    new_id = re.sub('\.+', '.', new_id)
    new_id = re.sub('^\.|\.$', '', new_id)

    if new_id == '':
        new_id = 'a'

    if 15 < len(new_id):
        if new_id[14] == '.':
            new_id = new_id[:14]
        else:
            new_id = new_id[:15]
    elif len(new_id) < 3:
        new_id = new_id + new_id[-1] * (3 - len(new_id))

    return new_id