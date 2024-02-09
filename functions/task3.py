def solve(numheads,numlegs):
    for rabbit in range(0,numheads):
        chickens = numheads - rabbit
        if((rabbit*4)+(chickens*2)==numlegs):
            print(f"Chickens: {chickens}, Rabbits: {rabbit}")
            break