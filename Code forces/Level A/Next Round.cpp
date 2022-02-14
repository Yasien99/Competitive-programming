
#include <iostream>
#include <bits/stdc++.h> 
using namespace std;

int main()
{
	int n = 0;
	int k = 0;
	int scores = 0;
	int advance = 0;

	cin >> n;
	cin >> k;
	for (int i = 0;i < n;i++) {
		cin >> scores;
		if (scores > k) {
			advance++;
		}
	}
	cout << advance;
}