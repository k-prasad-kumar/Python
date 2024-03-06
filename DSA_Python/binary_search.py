#binary search

def binary_search(cards, query):
    low, high = 0, len(cards) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_number = cards[mid]
        if mid_number == query:
            return mid
        elif mid_number < query:
            low = mid + 1
        elif mid_number > query:
            high = mid - 1
    return -1


# Testing
tests = []

tests.append({
    'input': {
        'cards': [1,2,3,4,5,6,7,8,9],
        'query': 4
    },
    'output': 3
})

tests.append({
    'input': {
        'cards': [1,2,3,4,5,6,7,8,9],
        'query': 7
    },
    'output': 6
})
tests.append({
    'input': {
        'cards': [1,2,3,4,5,6,7,8,9],
        'query': 5
    },
    'output': 4
})
tests.append({
    'input': {
        'cards': [],
        'query': 6
    },
    'output': -1
})
tests.append({
    'input': {
        'cards': [1,2,3,4,5,6],
        'query': 9
    },
    'output': -1
})
tests.append({
    'input': {
        'cards': [1,2,2,2,3,4,4,4,4,4,4,5,5,5,5,6,7,8,9],
        'query': 3
    },
    'output': 4
})
tests.append({
    'input': {
        'cards': [1,2,2,2,3,4,4,4,4,4,4,5,5,5,5,6,7,8,9],
        'query': 8
    },
    'output': 17
})


def evaluate_test_cases(tests, fun):
    results = []
    for x in tests:
        result = fun(x["input"]['cards'], x["input"]['query'])
        if result == x["output"]:
            results.append({
                'input': {
                            'cards': x["input"]['cards'],
                            'query': x["input"]['query']
                        },
                'output': x["output"],
                'result':'PASSED'
            })
        else:
            results.append({
                'input': {
                            'cards': x["input"]['cards'],
                            'query': x["input"]['query']
                        },
                'output': x["output"],
                'result':'FAILED'
            })
    return results

test_case_results = evaluate_test_cases(tests, binary_search)
for x in test_case_results:
    print("CARDS : ", x["input"]['cards'])
    print("QUERY : ", x["input"]['query'])
    print("OUTPUT", x["output"])
    print("TEST RESULT: ", x["result"])