# advent-of-code/2022/day08
class FileReader:
    @staticmethod
    def get_lines(filename):

        lines = []
        with open(filename, "r") as file:
            for line in file:
                lines.append(line[:-1])

        return lines


class Solution:
    def __init__(self, lines) -> None:

        self.tree_grid = [[int(x) for x in line] for line in lines]

        self.m = len(self.tree_grid)
        self.n = len(self.tree_grid[0])

    def scrape_left(self, i, j):

        best = -1
        while j + 1 < self.n:
            j += 1
            best = max(best, self.tree_grid[i][j])

        return best

    def scrape_right(self, i, j):

        best = -1
        while j - 1 >= 0:
            j -= 1
            best = max(best, self.tree_grid[i][j])

        return best

    def scrape_up(self, i, j):

        best = -1
        while i - 1 >= 0:
            i -= 1
            best = max(best, self.tree_grid[i][j])

        return best

    def scrape_down(self, i, j):

        best = -1
        while i + 1 < self.m:
            i += 1
            best = max(best, self.tree_grid[i][j])

        return best

    def is_visible(self, i, j):

        height = self.tree_grid[i][j]

        vals = []
        vals.append(self.scrape_left(i, j))
        vals.append(self.scrape_right(i, j))
        vals.append(self.scrape_up(i, j))
        vals.append(self.scrape_down(i, j))

        for blocker in vals:
            if height > blocker:
                return True
        return False

    def count_visible_trees(self):

        count = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.is_visible(i, j):
                    count += 1

        return count

    def look_left(self, i, j):

        height = self.tree_grid[i][j]
        score = 0
        while j + 1 < self.n:
            j += 1
            score += 1
            if self.tree_grid[i][j] >= height:
                break

        return score

    def look_right(self, i, j):

        height = self.tree_grid[i][j]
        score = 0
        while j - 1 >= 0:
            j -= 1
            score += 1
            if self.tree_grid[i][j] >= height:
                break

        return score

    def look_up(self, i, j):

        height = self.tree_grid[i][j]
        score = 0
        while i - 1 >= 0:
            i -= 1
            score += 1
            if self.tree_grid[i][j] >= height:
                break

        return score

    def look_down(self, i, j):

        height = self.tree_grid[i][j]
        score = 0
        while i + 1 < self.m:
            i += 1
            score += 1
            if self.tree_grid[i][j] >= height:
                break

        return score

    def get_score(self, i, j):

        score = 1
        score *= self.look_left(i, j)
        score *= self.look_right(i, j)
        score *= self.look_up(i, j)
        score *= self.look_down(i, j)

        return score

    def get_best_tree_score(self):

        best = 0
        for i in range(self.m):
            for j in range(self.n):
                score = self.get_score(i, j)
                best = max(best, score)

        return best


lines = FileReader.get_lines("input.txt")
solver = Solution(lines)

print(f"count of visible trees = {solver.count_visible_trees()}")
print(f"best tree score = {solver.get_best_tree_score()}")
