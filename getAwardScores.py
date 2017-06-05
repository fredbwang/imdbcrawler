import re


# normal wins
def get_wins(text):
    pattern = re.compile(r'\d+\s+[win]')
    match = pattern.search(text)
    if match:
        return int(text[match.start(0) : match.end(0) - 1])
    else:
        return None


# normal nominations
def get_nominations(text):
    pattern = re.compile(r'\d+\s+[nomination]')
    match = pattern.search(text)
    if match:
        return int(text[match.start(0) : match.end(0) - 1])
    else:
        return None


# oscar wins
def get_oscars_wins(text):
    pattern = re.compile(r'[Won]+\s+\d+\s+[Oscar]')
    match = pattern.search(text)
    if match:
        return int(text[match.start(0) + 3 : match.end(0) - 1])
    else:
        return None


# oscar nominations
def get_oscars_nominations(text):
    pattern = re.compile(r'[for]\s+\d+\s+[Oscar]')
    match = pattern.search(text)
    if match:
        return int(text[match.start(0) + 1 : match.end(0) - 1])
    else:
        return None


# golden globe wins
def get_golden_wins(text):
    pattern = re.compile(r'[Won]\s+\d+\s+[Golden]')
    match = pattern.search(text)
    if match:
        return int(text[match.start(0) + 1 : match.end(0) - 1])
    else:
        return None


# golden nominations
def get_golden_nominations(text):
    pattern = re.compile(r'[for]\s+\d+\s+[Golden]')
    match = pattern.search(text)
    if match:
        return int(text[match.start(0) + 1 : match.end(0) - 1])
    else:
        return None
