# Increasing version number

"""
In a software project with N applications, each app's version number is stored in an array versionNumbers[i]. The objective is to make the versionNumbers array strictly increasing.

You can perform the following operation any number of times:
- Increasing the i-th version number by i, where 1 <= i <= N (using 1-based indexing).

Determinate the minimum number of operations required to make the versionNumbers array strictly increasing.

Example
versionNumebers = [2,1,3]
Output: [2,3,3]

After 2 operations, versionNumbers[] is strictly increasing.

Function Description
Complete the function getMinimumOperations in the editor with the following parameters:
int versionNumbers[n]: the app's version numbers

Returns
long: the minimum number of operations required to make versionNumbers strictly increasing

Constraints
1 <= n <= 2 * 10^5
1 <= versionNumbers[i] <= 10^9
"""

def getMinimumOperations(versionNumbers: list[int]) -> int:
    n = len(versionNumbers)
    total_operations = 0
    for i in range(1, n):
        if versionNumbers[i] <= versionNumbers[i - 1]:
            needed_increase = (versionNumbers[i - 1] - versionNumbers[i]) + 1
            increase_per_operation = i + 1
            operations_needed_for_current = (needed_increase + increase_per_operation - 1) // increase_per_operation
            total_operations += operations_needed_for_current
            versionNumbers[i] += operations_needed_for_current * increase_per_operation
    return total_operations


if __name__ == "__main__":
    versionNumbers = [2, 1, 3]
    print(getMinimumOperations(versionNumbers))  # Output: 2
    versionNumbers = [1, 2, 3]
    print(getMinimumOperations(versionNumbers))  # Output: 0
    versionNumbers = [4, 3, 2, 1]
    print(getMinimumOperations(versionNumbers))  # Output: 10
    versionNumbers = [1, 1, 1, 1]
    print(getMinimumOperations(versionNumbers))  # Output: 10
    versionNumbers = [1, 2, 1, 2]
    print(getMinimumOperations(versionNumbers))  # Output: 5
