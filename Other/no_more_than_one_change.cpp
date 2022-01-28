#include <string>
#include <iostream>


bool no_more_than_one_change(const std::string& first, const std::string& second) {
    if(first.size() > second.size() && first.size() - second.size() > 1) {
        return false;
    }
    if (second.size() > first.size() && second.size() - first.size() > 1) {
        return false;
    }

    size_t prefix = 0;
    while (prefix < first.size() && prefix < second.size())
    {
        if(first[prefix] != second[prefix]) {
            break;
        }
        ++prefix;
    }
    
    if(prefix == first.size() && prefix == second.size()) {
        return true;
    }
    
    size_t suffix = 0;
    while (suffix < first.size() && suffix < second.size())
    {
        if(first[first.size() - suffix - 1] != second[second.size() - suffix - 1]){
            break;
        }
        ++suffix;
    }
    
    size_t length = first.size() > second.size() ? first.size() : second.size();
    return length - prefix - suffix <= 1;
}

int main()
{
    if (no_more_than_one_change("a", "a") == false)
    {
        std::cerr << "'a' and 'a' failed";
    }
    if (no_more_than_one_change("", "") == false)
    {
        std::cerr << "empty failed";
    }
    if (no_more_than_one_change("", "a") == false)
    {
        std::cerr << "empty and 'a' failed";
    }

    if (no_more_than_one_change("a", "ab") == false)
    {
        std::cerr << "'a' and 'ab' failed";
    }
    if (no_more_than_one_change("abc", "ab") == false)
    {
        std::cerr << "'abc' and 'ab' failed";
    }

    if (no_more_than_one_change("a", "abc"))
    {
        std::cerr << "'a' and 'abc' failed";
    }
    if (no_more_than_one_change("a", "b") == false)
    {
        std::cerr << "'a' and 'b' failed";
    }
    if (no_more_than_one_change("", "bc"))
    {
        std::cerr << "'' and 'bc' failed";
    }
    if (no_more_than_one_change("1abc", "2abcd"))
    {
        std::cerr << "'1abc' and '2abcd' failed";
    }
    return 0;
}
