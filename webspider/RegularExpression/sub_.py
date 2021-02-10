import re

content = 'asdnsaj213nfdsne3243243232ji'
# 去掉所有数字
res = re.sub('\d+', '', content)
print(res)
