import time
import random


class ExecutionTime:
    """ 获取代码段的执行时间
    Returns:
        number: 计时数字
    """
    def __init__(self) -> None:
        self.start_time = time.time()

    def duration(self):
        return time.time() - self.start_time


# run code
timer = ExecutionTime()
sample_list = list()
my_list = [
    random.randint(1, 8888898) for num in range(1, 10000000) if num % 2 == 0
]
print("Finished in {} seconds.".format(timer.duration()))
