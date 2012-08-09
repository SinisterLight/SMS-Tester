#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

int main()
{
	freopen ("Keywords.txt","r",stdin);
	freopen ("MainScript.sh","w",stdout);
	string str;
	cout<<"#!/bin/sh\n"<<endl;
	cout<<"while :\n";
	cout<<"do\n";
	for ( int i=0;i<507;i++) 
	{
		getline(cin,str);
		str.resize(str.size()-1);
		cout<<"   python StoreRecievedMessage.py loop 3 > storeDataScript.sh\n";
		cout<<"   sh storeDataScript.sh\n";
		cout<<"   rm storeDataScript.sh\n";
		cout<<"   sleep 30\n";
		cout<<"   python SendNStoreMessage.py 0 56660 "<<str<<" > storeDataScript.sh"<<endl;
		cout<<"   sh storeDataScript.sh\n";
		cout<<"   rm storeDataScript.sh\n";
		cout<<"   python SendNStoreMessage.py 1 56660 "<<str<<" > storeDataScript.sh"<<endl;
		cout<<"   sh storeDataScript.sh\n";
		cout<<"   rm storeDataScript.sh\n";
		cout<<"   python SendNStoreMessage.py 2 56660 "<<str<<" > storeDataScript.sh"<<endl;
		cout<<"   sh storeDataScript.sh\n";
		cout<<"   rm storeDataScript.sh\n";
		cout<<"   python SendNStoreMessage.py 3 56660 "<<str<<" > storeDataScript.sh"<<endl;
		cout<<"   sh storeDataScript.sh\n";
		cout<<"   rm storeDataScript.sh\n";
	//	cout<<"   python SendNStoreMessage.py 4 56660 "<<str<<" > storeDataScript.sh"<<endl;
	//	cout<<"   sh storeDataScript.sh\n";
	//	cout<<"   rm storeDataScript.sh\n";
		cout<<"   sleep 60\n\n";
	}
	cout<<"done"<<endl;
	return 0;
}
