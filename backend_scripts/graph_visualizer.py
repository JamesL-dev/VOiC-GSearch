import graphviz

def visualize_graph(graph_filename):
   graphviz.render('dot', 'pdf', graph_filename, outfile= graph_filename + "_output.pdf").replace('\\', '/')