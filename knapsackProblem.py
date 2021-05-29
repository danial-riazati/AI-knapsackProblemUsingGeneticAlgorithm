import random

money, n = input().split()
money, n = [int(money), int(n)]
data = []
genes = [0, 1]
for _ in range(n):
    data.append([int(x) for x in input().split()])

populationSize = 10
generation = 0


def customSort(e):
    return e.fitnessCal()


def generatePack():
    return [random.choice(genes) for _ in range(n)]


class Individual:

    def __init__(self, genesList=None):
        self.fitness = 0
        if genesList is None:
            self.genesList = generatePack()
        else:
            self.genesList = genesList

    def fitnessCal(self):
        sumValue = 0
        sumWeight = 0
        for x in range(len(self.genesList)):
            if self.genesList[x] == 1:
                sumValue += data[x][1]
                sumWeight += data[x][0]
                if len(data[x]) == 4:
                    sumValue -= data[x][2] * data[x][3]

        if sumWeight > money:
            self.fitness = -1
            return self.fitness
        else:
            self.fitness = sumValue
            return self.fitness


class population:

    def __init__(self):
        self.list = [Individual() for _ in range(populationSize)]
        self.generation = 0

    def sort(self):
        self.list.sort(key=customSort, reverse=True)

    def crossoverAndMutation(self):
        new_generation = []
        s = int((10 * populationSize) / 100)
        new_generation.extend(self.list[:s])

        s = int((90 * populationSize) / 100)
        for _ in range(s):
            parent1 = random.choice(self.list[:50])
            parent2 = random.choice(self.list[:50])
            child_chromosome = []
            for gp1, gp2 in zip(parent1.genesList, parent2.genesList):

                prob = random.random()

                if prob < 0.45:
                    child_chromosome.append(gp1)

                elif prob < 0.90:
                    child_chromosome.append(gp2)

                else:
                    child_chromosome.append(random.choice(genes))

            new_generation.append(Individual(child_chromosome))

        self.list = new_generation


if __name__ == "__main__":
    p = population()
    p.sort()

    while generation < 100:
        generation += 1
        p.crossoverAndMutation()
        p.sort()

    [print(x) for x in p.list[0].genesList]
