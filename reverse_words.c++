#include <iostream>
#include <string>
#include <cassert>
#include <algorithm> // Required for std::reverse
#include <cctype>    // Required for std::isalnum

std::string reverse_words(const std::string &str)
{
    // We create a copy of the input string to modify and return
    std::string result = str;
    int n = result.length();
    int i = 0;

    while (i < n) {
        // 1. Skip characters that are not letters or numbers (spaces, punctuation)
        if (!std::isalnum(static_cast<unsigned char>(result[i]))) {
            i++;
            continue;
        }

        // 2. We found the start of a word
        int start = i;
        
        // Find the end of this word
        while (i < n && std::isalnum(static_cast<unsigned char>(result[i]))) {
            i++;
        }
        int end = i;

        // 3. Reverse the characters in this specific range
        // result.begin() + start is an iterator pointing to the first char of the word
        std::reverse(result.begin() + start, result.begin() + end);
    }

    return result;
}

int main()
{
    // The specific test case provided in the assignment
    std::string test_str = "String;  2be reversed...";
    std::string expected = "gnirtS;  eb2 desrever...";
    
    std::string result = reverse_words(test_str);
    
    // Output for manual verification
    std::cout << "Input:  " << test_str << std::endl;
    std::cout << "Output: " << result << std::endl;

    // Assignment requirement: assert in main() should succeed
    assert(result == expected);
    
    std::cout << "Assertion passed!" << std::endl;
    return 0;
}