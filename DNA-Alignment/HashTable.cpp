#include <iostream>
#include <stdlib.h>
#include <cstring>
#include <DataTypes.h>
#include <Hashtable.h>

using namespace std;

Hashtable * initHT(int sizeTable){
	// write code to create a new hash table with the given size, initialize
	// the hash table, and return the address of the hash table created.
	HashTable * hash = new HashTable;
	hash->sizeTable = sizeTable;
	for(int x = 0; x < sizeTable; x++){
		hash->elements[x].pattern = " ";
		hash->elements[x].pValue = 0;
	}
	return hash;
}

