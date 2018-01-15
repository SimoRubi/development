==================
Proof for onchange
==================

In order to replicate the debug do the following:

1. Create a new Product 'product' with a vendor 'vendor'
2. Create a parent 'parent' and, inside the parent, a child 'child'
3. Edit the parent: open its child and select the product 'product': the seller field is automatically updated with 'vendor'
4. Save the parent

Error: the field seller in 'child' is empty, it should contain 'vendor'

Credits
=======

Contributors
------------

* Simone Rubino <simone.rubino@agilebg.com> (www.agilebg.com)

Do not contact contributors directly about support or help with technical issues.