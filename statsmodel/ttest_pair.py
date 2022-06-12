from tracemalloc import Statistic
from scipy import stats

arr1 = [8, 7, 9, 6, 8]
arr2 = [6, 7, 7, 6, 6]

statistic, pvalue = stats.ttest_rel(arr1, arr2)
print('statistic={},pvalue={}'.format(statistic, pvalue))

# 输出：statistic=2.449489742783178, pvalue=0.07048399691021993
# 假设置信度为 0.05 ，由于 p 值大于置信度 0.05 ，接受原假设。所以 arr1 与 arr2 所代表的总体均值相等。