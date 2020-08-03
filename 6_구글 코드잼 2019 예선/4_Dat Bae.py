from sys import stdout

def send(q):
    print("".join([str(x) for x in q]), flush=True)
    res = input().strip()
    if len(res) == 2 and res == "-1": exit(-1)
    return res

def query(length, ranges):
    data = [0] * length
    for pos, length, bit, _, used in ranges:
        if used: continue
        for k in range(length):
            data[k + pos] = bit
    return send(data)

def divide_range(pos, length, bit, broken, used):
    if broken == 0 or length == 0:
        return [], []

    if broken == length:
        return [] if used else [pos + x for x in range(length)], [[pos, length, bit, broken, True]]

    k = max(2, length // broken)
    m = length // k
    nxt = [[pos + m * j, m, (j+1) % 2, 0, False] for j in range(k-1)]
    nxt += [[pos + m*(k-1), length - m*(k-1), k % 2, 0, False]]

    return [], nxt

def clean(result, bit):
    return result[:result.rfind(str(1 - bit))] if len(result) > 0 and int(result[-1]) != bit else result

def solve(n, broken, f, pos=0):
    q, ans, query_count = [[pos, n, 0, broken, False]], [], 0
    while len(q) > 0 and query_count <= f:
        ranges = [divide_range(*rng) for rng in q]
        ans = sum([rng[0] for rng in ranges], ans)
        q_next = sum([rng[1] for rng in ranges], [])

        if len(q_next) == 0 or query_count >= f: break
        query_res, query_count = query(n, q_next), query_count + 1

        faults, nptr = 0, 0
        for i in range(len(q)):
            pos, length, bit, broken, _ = q[i]
            if broken == length or broken == 0:
                nptr, faults = nptr + int(broken > 0), faults + broken
                continue

            k = max(2, length // broken)
            m = length // k

            actual_pos, actual_length = pos - faults, length - broken
            result = query_res[actual_pos:actual_pos + actual_length]

            pos = 0
            for j in range(k):
                length = q_next[nptr][1]
                current = clean(result[pos:pos+length], (j + 1) % 2)
                faults_found = length - sum([(j + 1) % 2 == int(x) for x in current])
                q_next[nptr][-2] = faults_found
                pos, faults, nptr = pos + length - faults_found, faults + faults_found, nptr + 1

        q = q_next

    return " ".join([str(x) for x in sorted(ans)])


T = int(input().strip())
for C in range(1, T + 1):
    n, b, f = map(lambda x: int(x.strip()), input().split())
    w = solve(n, b, f)
    print(w, flush=True)
    if int(input().strip()) == -1: exit(-2)

exit(0)