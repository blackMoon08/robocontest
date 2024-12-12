#include <bits/stdc++.h>

using namespace std;

char a[7][7];

bool used[8][8];

int main(){

	int n, m;

	cin >> n >> m;

	for(int i = 1; i <= n; i ++)

		for(int j = 1; j <= m; j ++)

			used[i][j] = true;

	for(int i = 1; i <= n; i ++)

		for(int j = 1; j <= m; j ++)

			cin >> a[i][j];

	for(int i = 1; i <= n; i ++){

		for(int j = 1; j <= m; j ++){

			if(a[i][j] == 'R'){

				for(int k = j + 1; k <= m; k ++){

					if(a[i][k] == 'L'){

						cout << -1;

						return 0;

					}

				}

			}

			else if(a[i][j] == 'L'){

				for(int k = 1; k <= j-1; k ++){

					if(a[i][k] == 'R'){

						cout << -1;

						return 0;

					}

				}

			}

			else if(a[i][j] == 'U'){

				for(int k = 1; k <= i-1; k ++){

					if(a[k][j] == 'D'){

						cout << -1;

						return 0;

					}

				}

			}

			else {

				for(int k = i + 1; k <= n; k ++){

					if(a[k][j] == 'U'){

						cout << -1;

						return 0;

					}

				}

			}

		}

	}

	for(int k = 0; k < 100; k ++){

		for(int i = 1; i <= n; i ++){

			for(int j = 1; j <= m; j ++){

				if(a[i][j] == 'U' && !used[i-1][j]){

					used[i][j] = false;

				}

				if(a[i][j] == 'L' && !used[i][j-1]){

					used[i][j] = false;

				}

				if(a[i][j] == 'R' && !used[i][j+1])

					used[i][j] = false;

				if(a[i][j] == 'D' && !used[i+1][j])

					used[i][j] = false;

			}

		}	

	}

	for(int i = 1; i <= n; i ++){

		for(int j = 1; j <= m; j ++){

			if(used[i][j]){

				cout << -1;

				return 0;

			}

		}

	}

	cout << n * m;

}