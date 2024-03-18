import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    def func1(n):
        return (2**-n)*(2**-n)**-1


    def func2(n):
        return 1 / (n ** 6)

    n = np.linspace(1, 10)

    plt.plot(n, func1(n), label='(2**-n)*(2**-n)**-1')
    plt.plot(n, func2(n), label='1/(n**6)', color='r')
    plt.xlabel('n')
    plt.title('(2**-n)*(2**-n)**-1 < 1/(n**6)')
    plt.legend()

    # Mark where the functions are equal
    intersection_point = np.argmin(np.abs(func1(n) - func2(n)))
    plt.scatter(n[intersection_point], func1(n)[intersection_point], color='g', label=f'Intersection = {n[intersection_point]}')
    plt.legend()

    plt.tight_layout()
    plt.show()
