# -*- coding: utf-8 -*-


def searchSuggestions(repository, customerQuery):

    for i in repository:
        if customerQuery == repository[i]:
            return i


if __name__ == "__main__" :
    repository_count = int(input().strip())

    repository = []

    for _ in range(repository_count):
        repository_item = input()
        repository.append(repository_item)

    customerQuery = input()

    result = searchSuggestions(repository, customerQuery)