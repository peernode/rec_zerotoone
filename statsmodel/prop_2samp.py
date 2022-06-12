# H0：假设南方人和北方人爱吃甜豆花的比例没有差异；H1：假设南方人和北方人爱吃甜豆花的比例有差异；

from statsmodels.stats.proportion import proportions_ztest
z_score, p_value = proportions_ztest([81,48],[180,150], alternative='two-sided')
print('p_value={}'.format(p_value))
print(z_score, p_value)

# 输出：0.0160
# 由于 p 小于 0.05 ，接受备选假设，南方人与北方人在喜爱吃甜豆花的比例上有显著差别，南方人爱吃甜豆花比例更高