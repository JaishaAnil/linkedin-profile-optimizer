from keywords import TECH_KEYWORDS

def analyze_profile(text):
    missing = []

    for keyword in TECH_KEYWORDS:
        if keyword.lower() not in text.lower():
            missing.append(keyword)

    score = int(((len(TECH_KEYWORDS) - len(missing))
                 / len(TECH_KEYWORDS)) * 100)

    return score, missing