#ifndef _HASHTABLE_H
#define _HASHTABLE_H

#include <iostream>
#include <DataTypes.h>
using namespace std;
#define MAX_ELEMENTS 11

struct HashTable{
	Patterns elements [MAX_ELEMENTS];
	int tableSize;
};

HashTable * initHT (int tableSize);
void insertHT (HashTable * ht, Patterns p, int tableSize);
int containsHT (HashTable * ht, string key, int tableSize);



#endif