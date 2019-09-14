def getScore(s):
    # calculate Longest Palindromic Subsequence Array
    memoized_result = [[0 for i in range(len(s))] for i in range(len(s))]

    def LPS(s):
        for i in range(len(s)):
            memoized_result[i][i] = 1

        # sl = substring length
        for sl in range(2, len(s) + 1):
            for i in range(0, len(s) - sl + 1):
                j = i + sl - 1
                if s[i] == s[j] and sl == 2:
                    memoized_result[i][j] = 2
                elif s[i] == s[j]:
                    memoized_result[i][j] = memoized_result[i + 1][j - 1] + 2
                else:
                    memoized_result[i][j] = max(memoized_result[i + 1][j], memoized_result[i][j - 1])

        return memoized_result[0][len(s) - 1]

    LPS(s)
    maximum_product = 0

    for i in range(len(memoized_result) - 1):
        value = memoized_result[0][i] * memoized_result[i + 1][len(memoized_result) - 1]
        maximum_product = max(maximum_product, value)

    return maximum_product
print(getScore('acdapmpomp'))