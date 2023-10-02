class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        winner = 0

        for i in range(1 , len(colors)-1):
            if colors[i] == colors[i-1] == colors[i+1]:
                if colors[i] == "A":
                    winner+=1
                else:
                    winner-=1
        return winner>0
