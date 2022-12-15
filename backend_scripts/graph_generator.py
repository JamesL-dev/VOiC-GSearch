from treelib import Node, Tree
from doc_data import create_doc_dict as create_doc_dict
from graph_visualizer import visualize_graph


def dict_to_tree(doc_dict, type):
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
   filename= type + "_dictionary_graph"
   tree.to_graphviz(filename)
   visualize_graph(filename)


def main():
   """Main function"""

   # and_doc_dict = create_doc_dict('and_dict')
   # dict_to_tree(and_doc_dict,"and")


   # or_doc_dict = create_doc_dict('or_dict')
   # dict_to_tree(or_doc_dict, "or")


   and_or_doc_dict = create_doc_dict('and_or_dict')
   dict_to_tree(and_or_doc_dict, "and_or")


if(__name__== "__main__"):
   main()# dict_to_tree(and_doc_dict,"and")