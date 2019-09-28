from collections import Counter
def checkio(text: str) -> str:
    
    # count symbols frequency
    count = Counter(text.lower())
    
    # sort by frequency exclude non letter symbols
    sorted_alphas = [x for x in count.most_common() if x[0].isalpha()]
    
    # counters whith max value - at list begin
    max_count = sorted_alphas[0][1]
    
    # filter only letters with max freq
    syms_max = [sym for sym, coun in sorted_alphas if coun == max_count]
    
    # return first in alphbet
    return sorted(syms_max)[0]

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")