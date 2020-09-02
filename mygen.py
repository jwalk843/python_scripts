#!/usr/bin/python3

def indexer(sequence):
    index = 0
    for item in sequence:
        yield (index, item)
        index += 1

def dual_indexer(seq1, seq2):
    index = 0
    while index < len(seq1):
        yield (seq1[index], seq2[index])
        index += 1
