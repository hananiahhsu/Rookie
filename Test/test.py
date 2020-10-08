# 从包导入类或方法有以下两种方法

from cnnapp import firstCnn
#import cnnapp.firstCnn



oCnn = firstCnn.CFirstCnn("xuxu")
oRes = oCnn.calculate(1, 2, 3)
print("Result = ", oRes)

oRes = oCnn.calculate(2, 4, 6)
print("Result = ", oRes)

oRes = oCnn.calculate(2, 4, 6)
oCnn.show()