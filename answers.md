/*Author liltongungob03@gmail.com


What is the complexity of your algorithm (in big O notation)?

Algorithm Description:
Read Data from database
,Example Data:

    0:ImageNet 2011 Fall Release>plant, flora, plant life>phytoplankton>planktonic algae,0
    1:ImageNet 2011 Fall Release>plant, flora, plant life>phytoplankton>diatom,0



Convert to Tree Structure:
 Root Name = 'ImageNet 2011 Fall Release'

 Root Name can be 'ImageNet 2011 Fall Release>plant, flora, plant life'
 or 'ImageNet 2011 Fall Release>plant, flora, plant life>phytoplankton>' and so on
 as long as it follows and order of precedence from node to child.

 Therefore in this situation we get every subtree of the root node

 We read Example Data linearly starting at index 0

 Insert Example Data [0] to tree()
 tree={}
 Separate Example Data[0]['name'] by '>'

 Example Data[0]['name']:

 0:ImageNet 2011 Fall Release

 1:plant, flora, plant life

 2:phytoplankton

 3:planktonic algae

 Loop through Data[0]['name'] and get their unique hash value
 using the string_hash_function(Data[0]['name'][n]) in class Tree in TreeStructure.py

 0:ImageNet 2011 Fall Release - Unique Value 0

 1:plant, flora, plant life - Unique Value 1

 2:phytoplankton - Unique Value 2

 3:planktonic algae - Unique Value 3


 Insert Data[0]['name'][0] - Unique Value 0 to tree:

 Before Operation:
    
    tree={}

 After Operation:

    tree={
    Unique Value 0:{'name':'ImageNet 2011 Fall Release','size':0,'children':{}}
    }

 Insert Data[0]['name'][1] - Unique Value 1 to tree:

 Before Operation:
 tree={
    
    Unique Value 0:{
    'name':'ImageNet 2011 Fall Release',
    'size':1,
    'children':{}}
 }

 After Operation:
 tree={
    
    Unique Value 0:{
    'name':'ImageNet 2011 Fall Release',
    'size':1,
    'children':{

    Unique Value 1:{

        'name':'plant, flora, plant life'
        'size':1
         'children':{}

    }
    }
     }
     }


 Insert Data[0]['name'][2] - Unique Value 2 to tree:

 Before Operation:
 tree={
    
    Unique Value 0:{
    'name':'ImageNet 2011 Fall Release',
    'size':1,
    'children':{

        Unique Value 1:{

            'name':'plant, flora, plant life'
            'size':1
            'children':{}

            }
         }
     }
    }

After Operation:

 tree={
    
    Unique Value 0:{
    'name':'ImageNet 2011 Fall Release',
    'size':1,
    'children':{

        Unique Value 1:{

            'name':'plant, flora, plant life'
            'size':1
            'children':{
                    Unique Value 2: {
                    'name':'phytoplankton'
                    'size'1
                    'children':{}

                    }
                }

            }
         }
     }
    }

Insert Data[0]['name'][3] - Unique Value 3 to tree:

Before Operation:
 tree={
 
    Unique Value 0:{
    'name':'ImageNet 2011 Fall Release',
    'size':1,
    'children':{

        Unique Value 1:{

            'name':'plant, flora, plant life'
            'size':1
            'children':{
                    Unique Value 2: {
                    'name':'phytoplankton'
                    'size'1
                    'children':{}

                    }
                }

            }
         }
     }
    }

 After Operation:
  tree={
  
    Unique Value 0:{
    'name':'ImageNet 2011 Fall Release',
    'size':1,
    'children':{

        Unique Value 1:{

            'name':'plant, flora, plant life'
            'size':1
            'children':{

                    Unique Value 2: {
                    'name':'phytoplankton'
                    'size'1
                    'children':{

                        Unique Value 3:
                        'name':planktonic algae
                        'size':0
                        'children':{}
                    }

                    }
                }

            }
         }
     }
    }

Insert Example Data [1] to tree():
 Separate Example Data[1]['name'] by '>'

 Example Data[1]['name']:

 0:ImageNet 2011 Fall Release

 1:plant, flora, plant life

 2:phytoplankton

 3:diatom


 Loop through Data[1]['name'] and get their unique hash value
 using the string_hash_function(Data[1]['name'][n]) in class Tree in TreeStructure.py

 0:ImageNet 2011 Fall Release - Unique Value 0

 1:plant, flora, plant life - Unique Value 1

 2:phytoplankton - Unique Value 2

 3:diatom- Unique Value 4

 Insert Data[1]['name'][0] - Unique Value 0 to tree:

 Before Operation:
 tree={
 
    Unique Value 0:{
    'name':'ImageNet 2011 Fall Release',
    'size':1,
    'children':{

        Unique Value 1:{

            'name':'plant, flora, plant life'
            'size':1
            'children':{

                    Unique Value 2: {
                    'name':'phytoplankton'
                    'size'1
                    'children':{

                        Unique Value 3:
                        'name':planktonic algae
                        'size':0
                        'children':{}
                    }

                    }
                }

            }
         }
     }
    }
 
 After Operation:
  tree={
 
    Unique Value 0:{
    'name':'ImageNet 2011 Fall Release',
    'size':2,
    'children':{

        Unique Value 1:{

            'name':'plant, flora, plant life'
            'size':1
            'children':{

                    Unique Value 2: {
                    'name':'phytoplankton'
                    'size'1
                    'children':{

                        Unique Value 3:
                        'name':planktonic algae
                        'size':0
                        'children':{}
                    }

                    }
                }

            }
         }
     }
    }
 

Insert Data[1]['name'][1] - Unique Value 1 to tree:
Before Operation:
 tree={

    Unique Value 0:{
    'name':'ImageNet 2011 Fall Release',
    'size':2,
    'children':{

        Unique Value 1:{

            'name':'plant, flora, plant life'
            'size':1
            'children':{

                    Unique Value 2: {
                    'name':'phytoplankton'
                    'size'1
                    'children':{

                        Unique Value 3:
                        'name':planktonic algae
                        'size':0
                        'children':{}
                    }

                    }
                }

            }
         }
     }
    }
 
 After Operation:
  tree={
 
    Unique Value 0:{
    'name':'ImageNet 2011 Fall Release',
    'size':2,
    'children':{

        Unique Value 1:{

            'name':'plant, flora, plant life'
            'size':2
            'children':{

                    Unique Value 2: {
                    'name':'phytoplankton'
                    'size'1
                    'children':{

                        Unique Value 3:
                        'name':planktonic algae
                        'size':0
                        'children':{}
                    }

                    }
                }

            }
         }
     }
    }

Insert Data[1]['name'][2] - Unique Value 2 to tree:

Before Operation
tree={
 
    Unique Value 0:{
    'name':'ImageNet 2011 Fall Release',
    'size':2,
    'children':{

        Unique Value 1:{

            'name':'plant, flora, plant life'
            'size':2
            'children':{

                    Unique Value 2: {
                    'name':'phytoplankton'
                    'size'1
                    'children':{

                        Unique Value 3:
                        'name':planktonic algae
                        'size':0
                        'children':{}
                    }

                    }
                }

            }
         }
     }
    }

After Operation:

    Unique Value 0:{
    'name':'ImageNet 2011 Fall Release',
    'size':2,
    'children':{

        Unique Value 1:{

            'name':'plant, flora, plant life'
            'size':2
            'children':{

                    Unique Value 2: {
                    'name':'phytoplankton'
                    'size'2
                    'children':{

                        Unique Value 3:
                        'name':planktonic algae
                        'size':0
                        'children':{}
                    }

                    }
                }

            }
         }
     }


Insert Data[1]['name'][3] - Unique Value 4 to tree:

Before Operation:

    Unique Value 0:{
        'name':'ImageNet 2011 Fall Release',
        'size':2,
        'children':{
        
        Unique Value 1:{

            'name':'plant, flora, plant life'
            'size':2
            'children':{

                    Unique Value 2: {
                    'name':'phytoplankton'
                    'size'2
                    'children':{

                        Unique Value 3:
                        'name':planktonic algae
                        'size':0
                        'children':{}
                    }

                    }
                }

            }
         }
     }
 
 
 
 After Operation:
 
    'name':'ImageNet 2011 Fall Release',
    'size':2,
    'children':{

        Unique Value 1:{

            'name':'plant, flora, plant life'
            'size':2
            'children':{

                    Unique Value 2: {
                    'name':'phytoplankton'
                    'size'2
                    'children':{
                        
                        Unique Value 3:
                        'name':planktonic algae
                        'size':0
                        'children':{}
                        
                        Unique Value 4:
                        'name':diatom
                        'size':0
                        'children':{}
                    }

                    }
                }

            }
         }
     }
    }

Then we can format this tree data into it's proper format using tree.get_properly_formatted_tree(Root Name)


resulting into :


    name: 'ImageNet 2011 Fall Release',
    size: 2,
    children: [
        {
            name: 'plant, flora, plant life',
            size: 2,
            children: [
                {
                    name: 'phytoplankton',
                    size: 2,
                    children: [
                        'name':planktonic algae
                        'size':0
                        'children':[],
                        
                        'name':diatom
                        'size':0
                        'children':[]
                    ]
                },
                ...
            ]
        },
        ...
    ]



Doing this the same process to the entire tree list data on the data base results exactly in this order,
when Root Name = 'ImageNet 2011 Fall Release':


    name: 'ImageNet 2011 Fall Release',
    size: 60941,
    children: [
        {
            name: 'plant, flora, plant life',
            size: 4699,
            children: [
                {
                    name: 'phytoplankton',
                    size: 2,
                    children: [
                        ...
                    ]
                },
                ...
            ]
        },
        ...
    ]


----------ALSO A BUG TO NOTE, Correct my if I'm wrong-----------------
 My assumption is that a node's size is the size of all it's children,
 like:
 'ImageNet 2011 Fall Release>plant, flora, plant life>phytoplankton,2'

 for instance it has a size of 2 because it has a  total of 2 children

 Basically if we do this for all the nodes in the tree the root node

 'ImageNet 2011 Fall Release'
 should not only have a size of 32326 but 60941. and
 'ImageNet 2011 Fall Release>plant, flora, plant life' should have 4699
 instead of 4486 and so on.

 See -downloaded_tree_file.txt- for proof.
 ----------------------------------------------------------------------



The Algorithmic Complexity of this algorithm would be:

    Insertion,Retrieval, and Deletion of a node would be linear time:
        n = the number of inputs
        best case: 0(1)
        worst case: 0(n)
        average case runtime complexity is O(n/2)=O(n)

    Space Complexity:
        O(n)




Technologies Used:

Python and Flask
-I wanted to try out python and flask, this was actually my first time using these two.

SqLite 3 for database
-Wanted to test out a light wait Sql library built on C

and Javascript for displaying data
-I've had previous experience using Javascript, mostly with AngularJs














