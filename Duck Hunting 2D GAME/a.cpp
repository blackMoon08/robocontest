#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

using PII = pair<int, int>;
const int maxn = 75 * 200000 + 25;
const int INF = 1e9;

int n, K, m, i, j, t, k, s;
int tot, lc[maxn], rc[maxn], tag[maxn], tr[maxn], nrt;

priority_queue<PII, vector<PII>, greater<PII>> Q;

inline void pushup(int rt)
{
    tr[rt] = max(tr[lc[rt]], tr[rc[rt]]) + tag[rt];
}

void upd(int &rt, int l, int r, int pl, int v)
{
    if (!rt)
        rt = ++tot;
    if (l == r)
    {
        tr[rt] = v;
        return;
    }
    int mid = (l + r) >> 1;
    if (pl <= mid)
        upd(lc[rt], l, mid, pl, v);
    else
        upd(rc[rt], mid + 1, r, pl, v);
    pushup(rt);
}
void add(int rt, int l, int r, int L, int R)
{
    if (!rt)
        return;
    if (l >= L && r <= R)
    {
        tr[rt]++;
        tag[rt]++;
        return;
    }
    int mid = (l + r) >> 1;
    if (L <= mid)
        add(lc[rt], l, mid, L, R);
    if (R > mid)
        add(rc[rt], mid + 1, r, L, R);
    pushup(rt);
}

int query(int rt, int l, int r, int L, int R)
{
    if (!rt)
        return 0;
    if (l >= L && r <= R)
        return tr[rt];
    int mid = (l + r) >> 1;
    if (R <= mid)
        return query(lc[rt], l, mid, L, R) + tag[rt];
    if (L > mid)
        return query(rc[rt], mid + 1, r, L, R) + tag[rt];
    return max(query(lc[rt], l, mid, L, R), query(rc[rt], mid + 1, r, L, R)) + tag[rt];
}

int main()
{
    cin >> n >> K;
    for (i = 1; i <= n; ++i)
    {
        cin >> s >> t;
        if (t < 0)
            continue;
        s = max(s, 0);
        Q.push(make_pair(t, s));
        Q.push(make_pair(s, -1));
    }
    nrt = tot = 1;
    int lst = -1;
    while (!Q.empty())
    {
        int l = Q.top().second, r = Q.top().first;
        Q.pop();
        if (l >= 0)
        {
            add(1, 0, INF, l, r);
            continue;
        }
        if (r == lst)
            continue;
        int u = lst >= 0 ? query(1, 0, INF, lst, lst) : 0;
        int v = r - K >= 0 ? query(1, 0, INF, 0, r - K) : 0;
        if (l == -1 || u < v)
        {
            lst = r;
            upd(nrt, 0, INF, r, v);
            if (r + K <= INF)
                Q.push(make_pair(r + K, -2));
        }
    }
    cout << tr[1] << endl;
    return 0;
}