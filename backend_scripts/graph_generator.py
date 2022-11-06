from treelib import Node, Tree
from doc_data import create_doc_dict as create_doc_dict
from graph_visualizer import visualize_graph


def dict_to_tree(doc_dict):
   """Convert a dictionary into a tree."""
   added = set()
   tree = Tree()
   print("Convert a dictionary into a tree.\n\n")

   while doc_dict:

      for key, value in doc_dict.items():
         if value['parent'] in added:
               tree.create_node(key, key, parent=value['parent'])
               added.add(key)
               doc_dict.pop(key)
               break
         elif value['parent'] is None:
               tree.create_node(key, key)
               added.add(key)
               doc_dict.pop(key)
               break

   tree.show()
   filename="dictionary_graph"
   tree.to_graphviz(filename)
   visualize_graph(filename)


def main():
   """Main function"""
   doc_dict = create_doc_dict()
   dict_to_tree(doc_dict)

if(__name__== "__main__"):
   main()