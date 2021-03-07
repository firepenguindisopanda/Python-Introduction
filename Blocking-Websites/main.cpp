#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdlib>
using namespace std;
int main()
{
	ifstream fin_dns;
	ifstream fin_queries;
	ifstream fin_blacklist;
	string dnsTxt;
	string queriesTxt;
	string blacklistTxt;
	fin_dns.open("dns.txt");
	fin_queries.open("queries.txt");
	fin_blacklist.open("blacklist.txt");
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
	while(getline(fin_dns, dnsTxt)){
		cout<<dnsTxt<<"\n";
	}
	while(getline(fin_queries, queriesTxt)){
		cout<<queriesTxt<<"\n";
	}
	while(getline(fin_blacklist, blacklistTxt)){
		cout<<blacklistTxt<<"\n";
	}
    return 0;
}
