There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

Example 1:
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false

Example 2:
Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true

we need to simulate how many people are in the car at any time

stops[i] tells us how many people got in or out at point i

every pickup adds passengers, every drop removes them

this is basically a prefix sum pattern

steps:
make a list stops[0...1000] (because locations go up to 1000)

for each trip:

add passengers at pickup point

subtract passengers at drop point

now loop through all stops from 0 to 1000

track current number of people in the car

if at any point current > capacity, return False

why it works:
instead of simulating every trip one by one, we flatten everything into a single array

that way, we just scan once and track passenger count over time

clean, simple, and avoids sorting or event processing

time:
O(n) for trips

O(1001) for scanning stops → constant time
