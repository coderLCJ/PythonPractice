from py2neo import Node, Graph, Relationship, NodeMatcher

class DataToNeo4j(object):
    def __init__(self):
        """建立连接"""
        link = Graph('http://localhost:7474', username='neo4j', password='19990806')
        self.graph = link
        self.buy = 'buy'
        self.sell = 'sell'
        self.graph.delete_all()
        self.matcher = NodeMatcher(link)


