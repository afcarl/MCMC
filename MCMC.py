import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from MH import sampler, calc_posterior_analytical

sns.set_style('white')
sns.set_context('talk')

np.random.seed(0)
data = np.random.randn(100)

# ax = plt.subplot()
# sns.distplot(data, kde=False, ax=ax)
# _ = ax.set(title='Histogram of observed data', xlabel='x', ylabel='# observations')


# ax = plt.subplot()
# x = np.linspace(-1, 1, 500)
# posterior_analytical = calc_posterior_analytical(data, x, 0., 1.)
# ax.plot(x, posterior_analytical)
# ax.set(xlabel='mu', ylabel='belief', title='Analytical posterior')
# sns.despine()
# plt.show()


posterior = sampler(data, samples=1000, mu_init=1., plot=False)
fig, ax = plt.subplots()
ax.plot(posterior)
_ = ax.set(xlabel='sample', ylabel='mu')
plt.show()


# ax = plt.subplot()
# sns.distplot(posterior[500:], ax=ax, label='estimated posterior')
# x = np.linspace(-.5, .5, 500)
# post = calc_posterior_analytical(data, x, 0, 1)
# ax.plot(x, post, 'g', label='analytic posterior')
# _ = ax.set(xlabel='mu', ylabel='belief')
# ax.legend()
# plt.show()
