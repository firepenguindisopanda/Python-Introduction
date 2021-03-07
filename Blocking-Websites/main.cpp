#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdlib>

int main()
{
	ifstream fin_dns;
	ifstream fin_queries;
	ifstream fin_blacklist;
	if(!fin_dns.is_open()){
		cout<<"Couldn't find dns.txt file....\nClosing program.";
		return 0;
	}
	if(!fin_queries.is_open()){
		cout<<"Couldn't find queries file....\n closing program.";
		return 0;
	}
	if(!fin_blacklist.is_open()){
		cout<<"Couldn't find blacklist file....\nClosing program.";
		return 0;
	}
    return 0;
}