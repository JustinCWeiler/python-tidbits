import random

nargs = 1
def generator(args):
    init_seed = abs(args[0])
    seed = init_seed
    while True:
        random.seed(seed)
        seed = random.randrange(-init_seed, init_seed)
        yield random.randrange(-abs(seed), abs(seed))
