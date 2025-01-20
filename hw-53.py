#1
n = int(input("Enter the number of gas stations: "))
print("Enter the gas available at each station:")
gas = list(map(int, input().split()))
print("Enter the cost to travel to the next station:")
cost = list(map(int, input().split()))
total_gas = 0
total_cost = 0
tank = 0
start_station = 0

for i in range(n):
    total_gas += gas[i]
    total_cost += cost[i]
    tank += gas[i] - cost[i]
    if tank < 0:
        start_station = i + 1
        tank = 0
if total_gas >= total_cost:
    print("Start station:", start_station)
else:
    print("It's not possible to complete the circuit.")

#2
def minimum_candies(ratings):
    n = len(ratings)
    candies = [1] * n

    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)
ratings = [1, 0, 2]
print(minimum_candies(ratings))  
ratings = [1, 2, 2]
print(minimum_candies(ratings))  
