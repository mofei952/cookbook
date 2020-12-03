

# 你有个程序要执行CPU密集型工作，你想让他利用多核CPU的优势来运行的快一点。
# concurrent.futures 库提供了一个 ProcessPoolExecutor 类，可被用来在一个单独的Python解释器中执行计算密集型函数。

import gzip
import io
import glob
from concurrent import futures


def find_robots(filename):
    '''
    Find all of the hosts that access robots.txt in a single log file
    '''
    robots = set()
    with open(filename) as f:
        for line in f:
            # print(line)
            fields = line.split()
            if fields[6] == '/robots.txt':
                robots.add(fields[0])
    return robots


def find_all_robots(logdir):
    '''
    Find all hosts across and entire sequence of files
    '''
    files = glob.glob(logdir+'/*.log')
    all_robots = set()
    for robots in map(find_robots, files):
        all_robots.update(robots)
    return all_robots


def find_all_robots2(logdir):
    files = glob.glob(logdir+'/*.log')
    all_robots = set()
    with futures.ProcessPoolExecutor() as pool:
        for robots in pool.map(find_robots, files):
            all_robots.update(robots)
    return all_robots


if __name__ == '__main__':
    with open('logs/20201201.log') as f:
        data = f.read()
    with open('logs/20201204.log', 'w') as f:
        for i in range(200000):
            f.write(data)

    import time
    t = time.time()
    robots = find_all_robots('logs')
    print(time.time() - t)
    for ipaddr in robots:
        print(ipaddr)

    t = time.time()
    robots = find_all_robots2('logs')
    print(time.time() - t)
    for ipaddr in robots:
        print(ipaddr)

    import os
    os.remove('logs/20201204.log')


# cd .\c12_concurrency\p08_perform_simple_parallel_programming
# python .\process_pool.py
