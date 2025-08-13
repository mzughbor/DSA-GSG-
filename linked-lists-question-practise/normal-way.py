def josephus_elimination(n, k):

    people = list(range(1, n + 1))  #list of people with identifiers from 1 to n of people...
    eliminated_index = 0  # Starting index for counting

    while len(people) > 1:
        # Calculate the index of the person to be eliminated
        # (k-1) because list indices are 0-based
        # % len(people) to handle wrapping around the circle
        eliminated_index = (eliminated_index + k - 1) % len(people)
        
        # Remove the person at the calculated index
        removed_person = people.pop(eliminated_index)
        # print(f"Eliminated: {removed_person}, Remaining: {people}") # Uncomment to see the steps

    return people[0]  # The last remaining person

# Example from the problem description: n = 5, k = 3
n_example = 5
k_example = 3
result_example = josephus_elimination(n_example, k_example)
print(f"For n={n_example}, k={k_example}, the last remaining person is: {result_example}")

# You can test with other values:
# print(f"For n=7, k=3, the last remaining person is: {josephus_elimination(7, 3)}")
# print(f"For n=10, k=2, the last remaining person is: {josephus_elimination(10, 2)}")