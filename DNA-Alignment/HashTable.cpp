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
int hashCode(int sizeTable, string key){
	int x, value = 0, ascii = 0;
	int length = key.size();
	for(x = 0; x < length; x++){
		ascii = int(key[x]);
		value = value + (ascii * x);
	}
	return value;
}

int containHT(Hashtable * ht, string key, int sizeTable){
	int x, num = 0, d = 0, original = 0;
	num = hashCode(sizeTable, key);
	x = num % sizeTable;
	if(ht->elements[x].pattern == key){
		return ht->elements[x].pValue;
	}
	
	original = x;
	d = num % (sizeTable/2);
	x = x + d;
	while(x != original){	//while spot in hashtable is not empty
		if(ht->elements[x].pattern == key){		//compare key to condition name to see if it matches ans return true
			return ht->elements[x].pValue;
			
		}
		x += d;
	}
	return -1;			//searched hashtable and key was not found
}