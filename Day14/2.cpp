#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>

std::vector<std::string> split(const std::string &s, char delimiter) {
    std::vector<std::string> tokens;
    std::string token;
    for (char c : s) {
        if (c == delimiter) {
            if (!token.empty())
                tokens.push_back(token);
            token.clear();
        } else {
            token += c;
        }
    }
    if (!token.empty())
        tokens.push_back(token);
    return tokens;
}

std::vector<std::vector<char>> game;

const int NORTH = 0;
const int SOUTH = 1;
const int EAST = 2;
const int WEST = 3;

void roll(int dir, int col) {
    if (dir == NORTH || dir == WEST) {
        for (int symb = 1; symb < game[col].size(); ++symb) {
            if (game[col][symb] == 'O') {
                int new_ind = symb;
                for (int i = symb - 1; i >= 0; --i) {
                    if (game[col][i] != '.') break;
                    if (game[col][i] == '.') {
                        if ((i >= 1 && game[col][i - 1] != '.') || i == 0) {
                            new_ind = i;
                            break;
                        }
                    }
                }
                std::swap(game[col][symb], game[col][new_ind]);
            }
        }
    } else if (dir == SOUTH || dir == EAST) {
        for (int symb = game[col].size() - 2; symb >= 0; --symb) {
            if (game[col][symb] == 'O') {
                int new_ind = symb;
                for (int i = symb + 1; i < game[col].size(); ++i) {
                    if (game[col][i] != '.') break;
                    if (game[col][i] == '.') {
                        if ((i + 1 < game[col].size() && game[col][i + 1] != '.') || i + 1 == game[col].size()) {
                            new_ind = i;
                            break;
                        }
                    }
                }
                std::swap(game[col][symb], game[col][new_ind]);
            }
        }
    }
}

int main() {
    std::ifstream f("./Day14/test.txt");
    std::string line;
    while (std::getline(f, line)) {
        std::vector<char> col(line.begin(), line.end());
        game.push_back(col);
    }

    int s = 0;
    for (int i = 0; i < 1000000000; i++) {
        //std::cout << "on iteration " << i << std::endl;
        for (int col = 0; col < game.size(); col++) {
            roll(1, col);
        }

        for (int col = 0; col < game.size(); col++) {
            roll(2, col);
        }

        for (int col = 0; col < game.size(); col++) {
            roll(3, col);
        }

        for (int col = 0; col < game.size(); col++) {
            roll(4, col);
        }

        for (int col = 0; col < game.size(); col++) {
            roll(1, col);
        }
    }

    for (int col = 0; col < game.size(); col++) {
        for (int symb = 0; symb < game[col].size(); symb++) {
            if (game[col][symb] == 'O') {
                s += game[col].size() - symb;
            }
        }
    }

    std::cout << s << std::endl;

    return 0;
}