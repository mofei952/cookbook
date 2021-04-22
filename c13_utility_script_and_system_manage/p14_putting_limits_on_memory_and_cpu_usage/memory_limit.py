import resource


def limit_memory(maxsize):
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))


if __name__ == '__main__':
    limit_memory(1)
    nums = []
    for i in range(10000):
        nums.append('a')
