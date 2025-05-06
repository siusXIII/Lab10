from model.model import Model

myModel = Model()
myModel.buildGraph(1980)

print(f"Nodi: {myModel.getNumNodes()}, Archi: {myModel.getNumEdges()}")

