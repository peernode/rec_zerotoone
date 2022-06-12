# 显著性水平 α = 0.05 ，原假设 H0 ：汽车不安全性小于 0.1 ；备择假设 H1 ：汽车不安全性大于 0.1
from curses.ascii import alt
from statsmodels.stats.proportion import proportions_ztest
stat, pval = proportions_ztest(3, 15, 0.1, alternative='larger')
print('pvalue={}'.format(pval))


# 输出：0.1664
# 由于p大于0.05，接受原假设。