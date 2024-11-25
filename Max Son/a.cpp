#include <iostream>
#include <cmath>
#include <vector>
#include <unordered_map>

bool isPrime(int n, const std::vector<int>& primes) {
    if (n <= 1) {
        return false;
    }
    for (int prime : primes) {
        if (prime * prime > n) {
            break;
        }
        if (n % prime == 0) {
            return false;
        }
    }
    return true;
}

int digitSum(int n, std::unordered_map<int, int>& cache) {
    if (n < 10) {
        return n;
    }
    int sum = 0;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    if (cache.find(sum) != cache.end()) {
        return cache[sum];
    }
    cache[sum] = sum;
    return sum;
}

int main() {
    int a, b;
    std::cin >> a >> b;

    int sqrt_b = static_cast<int>(std::sqrt(b));
    std::vector<int> primes;
    std::vector<bool> sieve(sqrt_b + 1, true);
    for (int i = 2; i <= sqrt_b; ++i) {
        if (sieve[i]) {
            primes.push_back(i);
            for (int j = i * i; j <= sqrt_b; j += i) {
                sieve[j] = false;
            }
        }
    }

    int maxPrime = -1;
    int maxDigitSum = -1;
    std::unordered_map<int, int> digitSumCache;
    for (int i = a; i <= b; ++i) {
        if (isPrime(i, primes)) {
            int sum = digitSum(i, digitSumCache);
            if (sum > maxDigitSum) {
                maxDigitSum = sum;
                maxPrime = i;
            }
        }
    }

    if (maxPrime == -1) {
        std::cout << -1 << std::endl;
    } else {
        std::cout << maxPrime << std::endl;
    }

    return 0;
}