from py2neo import Node, Graph, Relationship, NodeMatcher

class DataToNeo4j(object):
    def __init__(self):
        link = Graph('http://localhost:7474', username='neo4j', password='19990806')
        self.graph = link
        self.buy = 'buy'
        self.sell = 'sell'
        self.graph.delete_all()
        self.matcher = NodeMatcher(link)
        node1 = Node('Person', name='laity')
        node2 = Node('animal', name='dog')
        r1 = Relationship(node1, 'have', node2)
        self.graph.create(node1)
        self.graph.create(node2)
        self.graph.create(r1)
        print('successful')


D = DataToNeo4j()
