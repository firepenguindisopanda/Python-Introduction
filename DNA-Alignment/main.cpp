#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdlib>

using namespace std;

int main()
{
	ifstream fin_dna;
	ifstream fin_patterns;
	string dnaTxt;
	string patternsTxt;
	fin_dna.open("dna.txt");
	fin_patterns.open("patterns.txt");
	if(!fin_dna.is_open()){
		cout<<"Couldn't find dna.txt file....\nClosing program.";
		return 0;
	}
	if(!fin_patterns.is_open()){
		cout<<"Couldn't find patterns.txt.....\nClosing program.";
		return 0;
	}
	while(getline(fin_dna, dnaTxt)){
		cout<<dnaTxt;
	}
	while(getline(fin_patterns, patternsTxt)){
		cout<<patternsTxt<<"\n";
	}
	
    return 0;
}
