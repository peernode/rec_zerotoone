import statsmodels.stats.weightstats as st

arr1 = [8, 7, 9, 6, 8]
arr2 = [6, 7, 7, 6, 6]
# usevar='unequal'两个总体方差不一样

t, p, df = st.ttest_ind(arr1, arr2, alternative='two-sided', usevar='unequal')
print('t值={},p值={},自由度={}'.format(t, p, df))


# 输出：t值=2.1213203435596415，p值=0.08011884223003829，自由度=5.752808988764045
# 假设置信度为 0.05 ，由于 p 值大于置信度 0.05 ，接受原假设。所以 arr1 与 arr2 的均值没有差异。