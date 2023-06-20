def capitalizeTitle(title: str) -> str:
    li = title.split()
    for i, l in enumerate(li):
        if len(l) <= 2:
            li[i] = l.lower()
        else:
            li[i] = l.title()
    return ' '.join(li)

capitalizeTitle(title="capiTalIze tHe titLe")