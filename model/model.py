import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._graph = nx.Graph()
        self._countries = DAO.getAllCountries()
        self._idMap = {}
        for v in self._countries:
            self._idMap[v.StateAbb] = v
        self._nodes = None
        self._anno = None
        self._allEdges = None

    def buildGraph(self, anno):
        self._anno = anno
        self._nodes = DAO.getAllNodes(self._idMap, anno)
        self._graph.add_nodes_from(self._nodes)
        self.addAllEdges()

    def getNumNodes(self):
        return len(self._graph.nodes)

    def getNumEdges(self):
        return len(self._graph.edges)

    def addAllEdges(self):
        self._allEdges = DAO.getAllEdges(self._idMap, self._anno)
        for edge in self._allEdges:
            self._graph.add_edge(edge.state1ab, edge.state2ab)

    def getVicini(self):
        self._vicini = {}
        for v in self._nodes:
            self._vicini[v.StateNme] = DAO.getVicini(v.StateAbb, self._anno)
        #conn = nx.node_connected_component(self._graph)
        return self._vicini
