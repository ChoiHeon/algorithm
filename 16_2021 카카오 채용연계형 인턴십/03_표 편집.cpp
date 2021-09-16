// 문제명: 표 편집
// 링크: https://programmers.co.kr/learn/courses/30/lessons/81303

#include <iostream>
#include <string>
#include <vector>
#include <stack>

std::vector<int> prev;
std::vector<int> next;
std::vector<bool> valid;
std::stack<int> erased;

int move_up(int cursor, int x) {
	while (x) {
		cursor = prev[cursor];

		if (cursor == -1)	break;
		if (valid[cursor])	--x;
	}

	return cursor;
}

int move_down(int cursor, int x) {
	while (x) {
		cursor = next[cursor];

		if (cursor == -1)	break;
		if (valid[cursor])	--x;
	}

	return cursor;
}

int remove(int cursor) {
	int i = move_up(cursor, 1);
	int j = move_down(cursor, 1);

	if (i != -1)	next[i] = j;
	if (j != -1)	prev[j] = i;

	erased.push(cursor);
	valid[cursor] = false;

	return j != -1 ? j : i;
}

void recover() {
	int target = erased.top();
	int i = move_up(target, 1);
	int j = move_down(target, 1);

	if (i != -1) {
		next[i] = target;
		prev[target] = i;
	}
	if (j != -1) {
		prev[j] = target;
		next[target] = j;
	}

	erased.pop();
	valid[target] = true;
}

std::string solution(int n, int k, std::vector<std::string> cmds) {
	int cursor = k;
	std::string answer;

	prev.resize(n, -1);
	next.resize(n, -1);
	valid.resize(n, true);
	answer.resize(n, 'X');

	for (int i = 0; i < n - 1; i++) {
		next[i] = i + 1;
		prev[i + 1] = i;
	}

	for (std::string& cmd : cmds) {
		if (cmd.size() == 1) {
			if (cmd == "C") {
				cursor = remove(cursor);
			}
			else { // cmd == "Z"
				recover();
			}
		}
		else {	// cmd.size() <= 3
			int x = stoi(cmd.substr(2));

			if (cmd[0] == 'U')	cursor = move_up(cursor, x);
			else				cursor = move_down(cursor, x);
		}
	}

	for (int i = 0; i < n; i++)
		if (valid[i])
			answer[i] = 'O';

	return answer;
}

int main() {
	int n = 10;
	int k = 9;
	std::vector<std::string> cmds = { "C", "C", "C", "C", "C", "C", "U 3", "Z", "C" };
	
	std::cout << solution(n, k, cmds) << std::endl;;

	return 0;
}