# pyFlix-Library-Binary-Search-Tree
My Implementation of a Binary Search Tree in Python received grade of 100%

The online Movie Library PyFlix must maintain a library of movie files that are available for users to stream. 
The library is dynamic, and keeps changing, with movies being added and removed frequently. 
Users will want to search the catalogue to see if particular movies are available. 
Used Python classes to represent the catalogue using a recursively-defined Binary Search Tree.
Two classes - one for a generic BinarySearchTree, and one for a MovieLib. 
A MovieLib object will then contain a BST as one of its fields, and will issues appropriate method calls to that BST.
The end user will never see the BST, but will only interact with the MovieLib.
The MovieLib object only has methods that make sense for managing and searching a movie library. 
A class is also required to specify Movie objects, along with one to test the BST implementation.

MovieLib class is to maintain a reference to the root of a binary search tree, and when you are asked to add a movie to the library,
create the correct Movie object and then call the add(self,obj) method of the referenced BSTNode.
Therefore, each of the methods should call the appropriate methods on that BSTNode.

