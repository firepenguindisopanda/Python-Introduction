#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
	ifstream fin_dna;
	string dnaTxt;
	fin_dna.open("dna.txt");
	if(!fin_dna.is_open()){
		cout<<"Couldn't find dna.txt file....\nClosing program.";
		return 0;
	}
	while(getline(fin_dna, dnaTxt)){
		cout<<dnaTxt;
	}
	
    return 0;
}
