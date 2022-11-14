
def main():
   """main"""
   doc_dict = create_doc_dict()

   for key, value in dict.items():
    print('\n',key+':\n')
    for key, value in value.items():
        print('{} : {}'.format(key, value))

def create_doc_dict():
   """This functionn will be for creating the dictionary for the document tags"""

   print("Creating document dictionary\n\n")

   dict = {"abebi lives in virginia" : {'parent' : "fila is absent from virginia"}, 
            "fila is absent from virginia" : {'parent' : "within 6 months"}, 
            "within 6 months" : {'parent' : "virginia is home state"}, 
            "virginia is home state" : {'parent' : "home section"},
            "home section" : {'parent' : "initial child custody"},
            "initial child custody" : {'parent' : None}
         }
   return dict

if(__name__ == '__main__'):
   main()