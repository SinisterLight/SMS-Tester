#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
	freopen ("Keywords.txt","r",stdin);
	freopen ("mainProg.sh","w",stdout);
	string str;
	cout<<"#!/bin/sh\n"<<endl;
	cout<<"while [true]\n";
	cout<<"do\n";
	for ( int i=0;i<506;i++) 
	{
		getline(cin,str);
		cout<<"   python stor_data_over_all_sim.py > storeDataScript.sh\n";
		cout<<"   sh storeDataScript.sh\n";
		cout<<"   rm storeDataScript.sh\n";
		cout<<"   python send_sms.py 56660 "<<str<<endl;
		cout<<"   sleep 60\n\n";
	}
	cout<<"done"<<endl;
	return 0;
}