"""

create (n:Person{name:'laity',age:31})  # 创建节点
create (n:Person{name:'laity',age:31})-[:wechat{微信号:201212}]->(a:Person{name:'2u',age:18})  # 创建关系

match (n:Person{name:'laity'}) delete n # 删除节点

match (n:Person{name:'laity',age:31})-[f:wechat{微信号:201212}]->(a:Person{name:'2u',age:18})  # 选择关系
delete f    # 删除关系

match (t:Person) where id(t)=344 set t:好人 return t        # 设置标签
match (t:Person) where id(t)=344 set t.战斗力=200 return t  # 设置属性

# 查找哪两个人之间是wechat关系
match (p:Person) - [:wechat] -> (n:Person) return p,n

"""