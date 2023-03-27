# 특별한 학교 이름

import sys

input = sys.stdin.readline

school_name_hash = {
    'NLCS': 'North London Collegiate School',
    'BHA': 'Branksome Hall Asia',
    'KIS': 'Korea International School',
    'SJA': 'St. Johnsbury Academy',
}

acronyms = input().rstrip('\n')

print(school_name_hash.get(acronyms))
