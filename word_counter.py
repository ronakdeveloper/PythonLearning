def word_counter(sentence):
    if sentence == '':
        return  {}
    words = sentence.split(' ')

    words = map(lambda w : w.lower(), words)

    frequency_dict: dict[str, int] = {}

    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    return frequency_dict

def run_tests():
    test_cases = [
        (
            "hello world hello python",
            {"hello": 2, "python": 1, "world": 1}
        ),
        (
            "Python python PYTHON Java java",
            {"java": 2, "python": 3}
        ),
        (
            "coding",
            {"coding": 1}
        ),
        (
            "cat dog cat bird dog cat",
            {"bird": 1, "cat": 3, "dog": 2}
        ),
        (
            "apple banana cherry apple banana",
            {"apple": 2, "banana": 2, "cherry": 1}
        ),
        (
            "zebra apple mango zebra apple",
            {"apple": 2, "mango": 1, "zebra": 2}
        ),
        (
            "",
            {}
        ),
        (
            "1 2 1 python 2 python",
            {"1": 2, "2": 2, "python": 2}
        )
    ]

    passed = 0

    for i, (sentence, expected) in enumerate(test_cases, 1):
        result = word_counter(sentence)

        if result == expected:
            print(f"Test {i}: PASSED ✅")
            passed += 1
        else:
            print(f"Test {i}: FAILED ❌")
            print("Input:   ", sentence)
            print("Expected:", expected)
            print("Got:     ", result)

    print(f"\nScore: {passed}/{len(test_cases)}")


run_tests()