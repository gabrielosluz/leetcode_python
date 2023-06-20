def divideString(s: str, k: int, fill: str):
    while len(s) % k != 0:
        s += fill
    # checking until the string is dividable into k groups
    # if not, it will add the filler until it is

    c = []
    for x in range(0, len(s), k):  # starts at 0, goes to len(s), iteration value is k
        c.append(s[x:x + k])  # appends everything from x->x+k (iteration value)

    return c  # return final list

divideString(s="abcdefghij",k=3,fill="x")