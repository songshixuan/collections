#!/usr/bin/python3

travel_ids = [('USA', 'ASD23123FSA'), ('CHN', 'CHN12345')]

for passport in travel_ids:
    print('%s/%s' % passport)

for passport in sorted(travel_ids):
    print('%s/%s' % passport)
