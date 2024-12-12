#include <bits/stdc++.h>

using namespace std;

using ll=long long;

ll r(string s) {

  int n = (int) s.size() / 2;

  vector<int> a, b;

  for (int i = 0; i < 2 * n; i++) {

    if (s[i] != s[0]) {

      a.push_back(i);

    }

    else {

      b.push_back(i);

    }

  }

  vector<ll> cnt(n, -n);

 

  function<void(int, int, int)> add = [&] (int l, int r, int x) {

    if (l <= r) {

      for (int j = l; j <= r; j++) {

        cnt[j] += x;

      }

    } else {

      for (int j = l; j < n; j++) {

        cnt[j] += x;

      }

      for (int j = 0; j <= r; j++) {

        cnt[j] += x;

      }

    }

  };

 

  int e = 0, w = 0, q = 0;

 

  for (int i = 0; i < n; i++) {

    while (e < n && b[e] < a[i]) {

      e++;

    }

 

    while (w < n && a[i] >= n + b[w]) {

      w++;

    }

 

    while (q < n && b[q] < n + a[i]) {

      q++;

    }

 

    if (e < q) {

      add((n - i + e) % n, (n - i + q - 1) % n, -a[i]);

    }

    if (q < n) {

      add((n - i + q) % n, (n - i + n - 1) % n, 2 * n + a[i]);

    }

 

    if (0 < w) {

      add((n - i) % n, (n - i + w - 1) % n, 2 * n - a[i]);

    }

    if (w < e) {

      add((n - i + w) % n, (n - i + e - 1) % n, a[i]);

    }

 

  }

 

 

  e = 0;

 

  for (int j = 0; j < n; j++) {

    while (e < n && a[e] < b[j]) {

      e++;

    }

 

    for (int i = 0; i < e; i++) {

      if (b[j] < n + a[i]) {

        cnt[(n - i + j) % n] += b[j];

      } else {

        cnt[(n - i + j) % n] -= b[j];

      }

    }

 

    for (int i = e; i < n; i++) {

      if (a[i] < n + b[j]) {

        cnt[(n - i + j) % n] -= b[j];

      } else {

        cnt[(n - i + j) % n] += b[j];

      }

    }

  }

 

  ll sol = 0;

  for (auto &x : cnt) {

    sol = max(sol, x);

  }

  return sol /2;

}



int main()

{

    int n;

    cin>>n;

    string s;

    cin>>s;

    

    cout << r(s);

    return 0;

}