#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdlib>
using namespace std;
struct DnsData{
	string siteName[50];
	string ipAddress[50];
};
int main()
{
	ifstream fin_dns;
	ifstream fin_queries;
	ifstream fin_blacklist;
	string dnsTxt, site, ip;
	string queriesTxt;
	string blacklistTxt;
	int dnsCount = 0;
	DnsData dd;
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
	fin_dns>>site;
	fin_dns>>ip;
	while(!fin_dns.eof()){
		dd.siteName[dnsCount] = site;
		dd.ipAddress[dnsCount] = ip;
		cout<<site<<"\n";
		cout<<ip<<"\n";
		fin_dns>>site;
		fin_dns>>ip;
		dnsCount += 1;
	}
	cout<<"\n";
	while(getline(fin_queries, queriesTxt)){
		cout<<queriesTxt<<"\n";
	}
	cout<<"\n";
	while(getline(fin_blacklist, blacklistTxt)){
		cout<<blacklistTxt<<"\n";
	}
	//Checks if the data was entered correctly
//		for(int i =0; i < dnsCount; i++){
//			cout<<dd.siteName[i]<<"\t\t"<<dd.ipAddress[i]<<"\n";
//		}
//	    return 0;
}
