"""

create (n:Person{name:'laity',age:31})  # �����ڵ�
create (n:Person{name:'laity',age:31})-[:wechat{΢�ź�:201212}]->(a:Person{name:'2u',age:18})  # ������ϵ

match (n:Person{name:'laity'}) delete n # ɾ���ڵ�

match (n:Person{name:'laity',age:31})-[f:wechat{΢�ź�:201212}]->(a:Person{name:'2u',age:18})  # ѡ���ϵ
delete f    # ɾ����ϵ

match (t:Person) where id(t)=344 set t:���� return t        # ���ñ�ǩ
match (t:Person) where id(t)=344 set t.ս����=200 return t  # ��������

# ������������֮����wechat��ϵ
match (p:Person) - [:wechat] -> (n:Person) return p,n

"""