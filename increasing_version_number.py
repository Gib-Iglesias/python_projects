# Increasing Version Number

"""
In a software project with N applications, each app's version number is stored in an array version_numbers[i].
The objective is to make the version_numbers array strictly increasing.

You can perform the following operation any number of times:
- Increasing the i-th version number by i, where 1 <= i <= N (using 1-based indexing).

Determinate the minimum number of operations required to make the version_numbers array strictly increasing.

Example
version_numbers = [2,1,3]
Output: [2,3,3]

After 2 operations, version_numbers[] is strictly increasing.

Function Description
Complete the function get_minimum_operations in the editor with the following parameters:
int version_numbers[n]: the app's version numbers

Returns
long: the minimum number of operations required to make version_numbers strictly increasing

Constraints
1 <= n <= 2 * 10^5
1 <= version_numbers[i] <= 10^9
"""

def get_minimum_operations(version_numbers: list[int]) -> int:
    n = len(version_numbers)
    total_operations = 0
    for i in range(1, n):
        if version_numbers[i] <= version_numbers[i - 1]:
            needed_increase = (version_numbers[i - 1] - version_numbers[i]) + 1
            increase_per_operation = i + 1
            operations_needed_for_current = (needed_increase + increase_per_operation - 1) // increase_per_operation
            total_operations += operations_needed_for_current
            version_numbers[i] += operations_needed_for_current * increase_per_operation
    return total_operations


if __name__ == "__main__":
    version_numbers = [2, 1, 3]
    print(get_minimum_operations(version_numbers))  # Output: 2
    version_numbers = [1, 2, 3]
    print(get_minimum_operations(version_numbers))  # Output: 0
    version_numbers = [2, 3, 4]
    print(get_minimum_operations(version_numbers))  # Output: 0
    version_numbers = [1, 1, 1]
    print(get_minimum_operations(version_numbers))  # Output: 2
    version_numbers = [1, 2, 2]
    print(get_minimum_operations(version_numbers))  # Output: 1
