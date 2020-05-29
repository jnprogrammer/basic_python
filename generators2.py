def oddnumbers():
    n = 1
    while True:
        yield n
        n += 2

def pi_series():
    odds = oddnumbers()
    apprx = 0
    while True:
        apprx += (4 / next(odds))
        yield apprx
        apprx -= (4 / next(odds))
        yield apprx




if __name__ == '__main__':
    approx_pi = pi_series()

    for x in range(194):
        print(next(approx_pi))