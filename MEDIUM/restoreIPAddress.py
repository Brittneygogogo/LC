from typing import List

'''
1、一开始，字符串的长度小于 4 或者大于 12 ，一定不能拼凑出合法的 ip 地址（这一点可以一般化到中间结点的判断中，以产生剪枝行为）；

2、每一个结点可以选择截取的方法只有 3 种：截 1 位、截 2 位、截 3 位，因此每一个结点可以生长出的分支最多只有 3 条分支；

根据截取出来的字符串判断是否是合理的 ip 段，这里写法比较多，可以先截取，再转换成 int ，再判断。我采用的做法是先转成 int，是合法的 ip 段数值以后，再截取。

3、由于 ip 段最多就 4 个段，因此这棵三叉树最多 4 层，这个条件作为递归终止条件之一；

4、每一个结点表示了求解这个问题的不同阶段，需要的状态变量有：

splitTimes：已经分割出多少个 ip 段；
begin：截取 ip 段的起始位置；
path：记录从根结点到叶子结点的一个路径（回溯算法常规变量，是一个栈）；
res：记录结果集的变量，常规变量。

'''
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        size = len(s)
        if size < 4 or size > 12:
            return []

        path = []
        res = []
        self.__dfs(s, size, 0, 0, path, res)
        return res

    #全局begin指针
    def __dfs(self, s, size, split_times, begin, path, res):
        if begin == size:
            if split_times == 4:
                res.append('.'.join(path))
            return
        #因为一个seg最少一位，剩余位数 < 剩余seg的个数segs*1 or  因为每个seg最多3位，剩余位数 > 剩下segs的个数*3
        if size - begin < (4 - split_times) or size - begin > 3 * (4 - split_times):
            return

        #循环每个seg中的三位
        for i in range(3):
            if begin + i >= size:
                break

            ip_segment = self.__judge_if_ip_segment(s, begin, begin + i)

            if ip_segment != -1:
                path.append(str(ip_segment))
                self.__dfs(s, size, split_times + 1, begin + i + 1, path, res)
                path.pop()

    def __judge_if_ip_segment(self, s, left, right):
        #size 是当前seg的长度
        size = right - left + 1

        if size > 1 and s[left] == '0':
            return -1

        res = int(s[left:right + 1])

        if res > 255:
            return - 1
        return res

x = Solution()
print(x.restoreIpAddresses("25525511135"))