class Solution:
  def countBits(self, num):
      ans = [0] * (num + 1)
      i = 1
      while(i <= num):

          ans[i] = ans[i >> 1] + (i & 1)
          i += 1
      return ans

x = Solution()
print(x.countBits(5))