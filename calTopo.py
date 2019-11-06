import numpy as np
import os
from log import log


def cal_adj_mat(RawDataPath="./RawTopoData/"):
    # read in raw data as list
    res = []
    target_dir = os.walk(RawDataPath)

    for path, dir_list, file_list in target_dir:
        for file_name in file_list:
            file_path = os.path.join(path, file_name)
            tmp_res = []
            with open(file_path, "r") as f:
                for line in f.readlines():
                    tmp_res.append(line.strip('\n'))

            res.append(tmp_res)

    # cal vertex set:
    vertex = np.array([])
    for raw_vec in res:
        vertex = np.array((list(set(vertex).union(set(np.array(raw_vec))))))

    vertex = np.sort(vertex)
    log.info("node cal finished.")

    # cal adj mat
    n = len(vertex)
    log.info("nums of nodes: " + str(n))
    matrix = np.zeros(shape=(n, n))
    for raw_vec in res:
        vec = np.array(raw_vec)
        for index in range(0, len(raw_vec) - 1):
            i = np.where(vertex == vec[index])
            j = np.where(vertex == vec[index + 1])
            matrix[i, j] = 1

    log.info("edge cal finished.")
    log.info("nums of edges: " + str(int(np.sum(matrix))))

    return vertex, matrix


if __name__ == "__main__":
    cal_adj_mat()
