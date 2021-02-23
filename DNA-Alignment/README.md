## Description
One of the earliest problems in Bioinformatics is the read alignment problem. In this problem
you are given several DNA sequences. One of these sequences is called the text, denoted as T,
and the rest of the sequences is called the set of patterns P. Each DNA sequence comprises
characters drawn from the set {A, C, G, T}. The text contains n characters, and each pattern
in P contains m characters where n < m.
Given a set of patterns, P, The goal of the (exact) read alignment problem is to find all
occurrences of each P in T.
Consider T = ACACGAAC, and let P = {AC, GA}. The pattern AC occurs at positions 2
and 6 in T, and the pattern GA occurs at position 4 in T.

# Content Information
* Main.py is the only one that has code at the moment.
* Run in IDLE, will produce a text file called solutions.txt
* This program finds all occurences of a set of patterns called P in, located in patterns.txt, in a long pattern called T, located in dna.txt
* It outputs the position of the pattern found in T to a tet file solutions.txt
* Uses hash tables and the Quadratic Probing Technique to handle collisions.
