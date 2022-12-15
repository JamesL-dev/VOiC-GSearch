
def main():
   """main"""
   doc_dict = create_doc_dict()

   for key, value in dict.items():
    print('\n',key+':\n')
    for key, value in value.items():
        print('{} : {}'.format(key, value))

def create_doc_dict(dict_type):
   """This functionn will be for creating the dictionary for the document tags"""

   print("Creating document dictionary\n\n")

   if(dict_type == 'and_dict'):
      and_dict = {
               "initial child custody" : {'parent' : None},
               "home section" : {'parent' : "initial child custody"},
               "virginia is home state" : {'parent' : "home section"},
               "within 6 months" : {'parent' : "virginia is home state"}, 
               "fila is absent from virginia" : {'parent' : "within 6 months"}, 
               "abebi lives in virginia" : {'parent' : "fila is absent from virginia"}, 
            }
      return and_dict

   if(dict_type == 'or_dict'):
      or_dict = {
            "initial child custody" : {'parent' : None},
            "home section" : {'parent' : "initial child custody"},
            "virginia is home state" : {'parent' : "home section"},
            "virginia is previous home state" : {'parent' : "home section"},
            "within 6 months" : {'parent' : "virginia is home state"}, 
            "fila is absent from virginia" : {'parent' : "within 6 months"}, 
            "abebi lives in virginia" : {'parent' : "within 6 months"}, 
         }
      return or_dict

   if(dict_type == 'and_or_dict'):
      and_or_dict = {
            "initial child custody" : {'parent' : None},
            "home section" : {'parent' : "initial child custody"},
            "virginia is home state" : {'parent' : "home section"},
            "virginia is previous home state" : {'parent' : "home section"},
            "within 6 months" : {'parent' : "virginia is home state"}, 
            "fila is absent from virginia" : {'parent' : "within 6 months"}, 
            "abebi lives in virginia" : {'parent' : "fila is absent from virginia"}, 
         }
      return and_or_dict

if(__name__ == '__main__'):
   main()