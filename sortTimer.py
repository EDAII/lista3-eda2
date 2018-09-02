import time


class SortTimer():

    def __init__(self, array):
        self.array = array

    def get_time_taken(self, func,quick=False):
        time_taken = {
            "time_taken": [],
            "n_of_elements": []
        }

        for cont in range(0, len(self.array)):
            start_time = time.time()
            if quick:
                func(self.array[:cont], 0, cont-1)
            else:
                func(self.array[:cont])
            time_taken["time_taken"].append(time.time() - start_time)
            time_taken["n_of_elements"].append(cont)
        return time_taken
