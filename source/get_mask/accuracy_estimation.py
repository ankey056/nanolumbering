
import numpy as np

def mask_sum(m):
    m1 = np.ones(m.shape, np.int8)
    m1[np.logical_not(m)] = 0
    return m1.sum()


def estimate_accuracy (method, test_img, standard_img):
    result = method.apply(test_img)
    coincidence = mask_sum(np.bitwise_and(result, standard_img))
    mistake = mask_sum(np.bitwise_and(np.bitwise_not(standard_img),
                                      result))
    if mistake == 0: mistake = 0.5
    return float(coincidence)/mistake
