from py2neo import Node, Graph, Relationship, NodeMatcher

class DataToNeo4j(object):
    def __init__(self):
        link = Graph('http://localhost:7474', username='neo4j', password='19990806')
        self.graph = link
        self.buy = 'buy'
        self.sell = 'sell'
        self.graph.delete_all()
        self.matcher = NodeMatcher(link)


money_list = []
sell_list = []
buy_list = []

if __name__ == '__main__':
    # invoice_data = open('Invoice_data_Demo.xls', 'w', encoding='utf-8')
    # for i in range(len(invoice_data)):
    #    money_list.append(invoice_data[invoice_data.columns[19]][i])
    #    sell_list.append(invoice_data[invoice_data.columns[10]][i])
    print()