#include <bits/stdc++.h>
#include <tr1/unordered_map>
#define ri register int
using namespace std;
typedef double db;
typedef long double ld;
typedef long long ll;
typedef vector <int> poly;
typedef pair <int, int> pii;
typedef pair <ll, int> pli;
typedef pair <int, ll> pil;
typedef pair <ll, ll> pll;
typedef unsigned long long ulll;
typedef unsigned int uii;
typedef string strr;
#define fi first
#define se second
#define pb push_back
#define ppp pop_back
#define rez resize
const ll Inf = 2e18;
const int rlen = 1 << 20, inf = 0x3f3f3f3f;
char buf[rlen], *ib = buf, *ob = buf;
#define gc() (((ib == ob) && (ob = (ib =  buf) + fread(buf, 1, rlen, stdin)), ib == ob) ? -1 : *ib++)
inline int read() {
  static int ans, f;
  static char ch;
  ans = 0, ch = gc(), f = 1;
  while (!isdigit(ch)) f ^= ch == '-', ch = gc();
  while (isdigit(ch)) ans = (ans << 3) + (ans << 1) + (ch ^ 48), ch = gc();
  return f ? ans: -ans;
}
inline ll readl() {
  static ll ans;
  static char ch;
  for (ans = 0, ch = gc(); !isdigit(ch); ch = gc());
  while (isdigit(ch)) ans = ((ans << 2) + ans << 1) + (ch ^ 48), ch = gc();
  return ans;
}
inline int Read(char *s) {
  static int top;
  static char ch;
  top = 0, ch = gc();
  while (!isalpha(ch) && !isdigit(ch)) ch = gc();
  while (isalpha(ch) || isdigit(ch)) s[++top] = ch, ch = gc();
  return top;
}
namespace modular {
  const int mod  = 998244353;// = 1e9 + 7;
  //int mod;
  int ret;
  inline int add(int a, int b) { return a + b < mod ? a + b : a + b - mod; }
  inline int dec(int a, int b) { return a < b ? a - b + mod : a - b; }
  inline int mul(int a, int b) { return (ll) a * b % mod; }
  inline void Add(int &a, int b) { a = a + b < mod ? a + b : a + b - mod; }
  inline void Dec(int &a, int b) { a = a < b? a - b + mod : a - b; }
  inline void Mul(int &a, int b) { a = (ll) a * b % mod; }
  inline int ksm(int a, int p) {
    for (ret = 1; p; p >>= 1, Mul(a, a)) (p & 1) && (Mul(ret, a), 1);
    return ret;
  }
  inline int Inv(int a) { return ksm(a, mod - 2); }
  inline int sqr(int a) { return (ll) a * a % mod; }
  inline int cub(int a) { return (ll) a * a % mod * a % mod; }
} using namespace modular;
template <typename T> inline void ckmax(T &a, T b) { a < b ? a = b : 0; }
template <typename T> inline void ckmin(T &a, T b) { a > b ? a = b : 0; }
template <typename T> inline T Abs(T a) { return a < 0 ? -a : a; }
template <typename T> inline T gcd(T a, T b) {
  T t;
  while (b) t = a, a = b, b = t - t / a * a;
  return a;
}
template <typename T> inline void exgcd(T a, T b, T &x, T &y) {
  if (!b) {
    x = 1, y = 0;
    return;
  }
  exgcd(b, a - a / b * b, y, x);
  y -= a / b * x;
}
const int N = 2e5 + 5;
int n, m, a[N], w[N];
namespace sgt {
  #define lc (p << 1)
  #define rc (p << 1 | 1)
  #define mid ((l + r) >> 1)
  #define qll lc, l, mid
  #define qrr rc, mid + 1, r
  ll ssl[N << 2], ssr[N << 2];
  int mx[N << 2], ql, qr;
  inline ll Ql(int p, int l, int r, int v) {
    if (l == r) return v < mx[p] ? w[l] : 0;
    if (mx[lc] <= v) return Ql(qrr, v);
    return Ql(qll, v) + ssl[p];
  }
  inline ll Qr(int p, int l, int r, int v) {
    if (l == r) return v < mx[p] ? w[r] : 0;
    if (mx[rc] <= v) return Qr(qll, v);
    return ssr[p] + Qr(qrr, v);
  }
  inline void pushup(int p, int l, int r) {
    mx[p] = max(mx[lc], mx[rc]);
    ssl[p] = Ql(qrr, mx[lc]), ssr[p] = Qr(qll, mx[rc]);
  }
  inline void build(int p, int l, int r) {
    if (l == r) { mx[p] = a[l], ssl[p] = ssr[p] = 0; return; }
    build(qll), build(qrr), pushup(p, l, r);
  }
  inline void upd(int p, int l, int r, int k) {
    if (l == r) return;
    k <= mid ? upd(qll, k) : upd(qrr, k);
    pushup(p, l, r);
  }
  inline pil qryl(int p, int l, int r, int v) {
    if (ql <= l && r <= qr) return pil(max(mx[p], v), Ql(p, l, r, v));
    if (qr <= mid) return qryl(qll, v);
    if (ql > mid) return qryl(qrr, v);
    pil L = qryl(qll, v), R = qryl(qrr, L.fi);
    return pil(max(L.fi, R.fi), L.se + R.se);
  }
  inline pil qryr(int p, int l, int r, int v) {
    if (ql <= l && r <= qr) return pil(max(mx[p], v), Qr(p, l, r, v));
    if (qr <= mid) return qryr(qll, v);
    if (ql > mid) return qryr(qrr, v);
    pil R = qryr(qrr, v), L = qryr(qll, R.fi);
    return pil(max(R.fi, L.fi), R.se + L.se);
  }
  inline int qry(int p, int l, int r) {
    if (ql <= l && r <= qr) return mx[p];
    if (qr <= mid) return qry(qll);
    if (ql > mid) return qry(qrr);
    return max(qry(qll), qry(qrr));
  }
  inline int qry(int l, int r) { return ql = l, qr = r, qry(1, 1, n); }
  inline ll qryl(int l, int r) { return ql = l, qr = r, qryl(1, 1, n, 0).se; }
  inline ll qryr(int l, int r) { return ql = l, qr = r, qryr(1, 1, n, 0).se; }
  #undef lc
  #undef rc
  #undef mid
  #undef qll
  #undef qrr
}
int main() {
  #ifdef ldxcaicai
  freopen("lx.in", "r", stdin);
  freopen("own.out", "w", stdout);
  #endif
  n = read(), m = read();
  for (ri i = 1; i <= n; ++i) a[i] = read();
  for (ri i = 1; i <= n; ++i) w[i] = read();
  sgt:: build(1, 1, n);
  for (ri op, x, y; m; --m) {
    op = read(), x = read(), y = read();
    if (op == 1) w[x] = y, sgt:: upd(1, 1, n, x);
    else {
      if (x == y) cout << w[x] << '\n';
      else if (x < y) {
        if (a[x] <= sgt:: qry(x + 1, y)) {
          puts("-1");
          continue;
        }
        cout << sgt:: qryr(x, y) << '\n';
      }
      else {
        swap(x, y);
        if (a[y] <= sgt:: qry(x, y - 1)) {
          puts("-1");
          continue;
        }
        cout << sgt:: qryl(x, y) << '\n';
      }
    }
  }
  return 0;
}