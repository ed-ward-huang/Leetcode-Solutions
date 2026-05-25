class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ## (pos, speed)
        sortedCarData = []
        for i in range(len(position)):
            timeToDestination = (target - position[i]) / speed[i]
            sortedCarData.append([position[i], timeToDestination])

        sortedCarData.sort(key=lambda x: x[0])

        fleets = 0
        
        for i in range(len(sortedCarData) - 1, -1, -1):
            if i != len(sortedCarData) - 1 and sortedCarData[i][1] <= sortedCarData[i + 1][1]:
                sortedCarData[i] = sortedCarData[i + 1]
                continue
            else:
                fleets += 1


        return fleets        



