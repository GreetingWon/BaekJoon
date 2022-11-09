#include <iostream>
using namespace std;

int main() {
	int T;	// 테스트 케이스의 개수
	int N;	// 각 테스트 케이스, fibonacci(N)

	// 피보나치 함수의 0, 1의 개수 저장
	// fibonacci[a][b]에서, a는 몇번째 함수인지
	// b는 0의 개수인지 1의 개수인지를 뜻함
	int fibonacci[42][2];

	// 피보나치 수열 값 초기화
	// fibonacci(0)의 0값은 1, fibonacci(0)의 1값은 0
	fibonacci[0][0] = 1;
	fibonacci[0][1] = 0;
	// fibonacci(1)의 0값은 0, fibonacci(1)의 1값은 1
	fibonacci[1][0] = 0;
	fibonacci[1][1] = 1;

	// 피보나치 함수의 원리를 적용
	for (int i = 2; i < 42; ++i)
	{
		fibonacci[i][0] = fibonacci[i - 1][0] + fibonacci[i - 2][0];
		fibonacci[i][1] = fibonacci[i - 1][1] + fibonacci[i - 2][1];
	}

	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> N;
		cout << fibonacci[N][0] << " " << fibonacci[N][1] << endl;
	}

	return 0;
}