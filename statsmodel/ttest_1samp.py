from tracemalloc import Statistic
from scipy import stats

arr = [31, 35, 28, 29, 27, 34, 32, 33, 30, 26]
statistic, pvalue = stats.ttest_1samp(arr, 30)
print('statistic={}, pvalue={}'.format(statistic, pvalue))

# 输出：statistic=0.5222329678670935, pvalue=0.614117254808394
# 假设置信度为 0.05 ，由于 p 值大于置信度 0.05 ，接受原假设。所以 arr 的均值与 30 差异不显著。