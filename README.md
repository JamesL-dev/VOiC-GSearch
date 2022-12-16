# VOiC-GSearch
VOiC Extension: Graph Search

# Description
GSearch is a system of "tags" users will add to their documents when uploaded to the database. Our feature will be to use these tags to build a visual graph which can then be used to search the database for documents containing those tags.

# Phase 1 Report

# Authors
[James Lasso](https://github.com/JamesL-dev/)<br>
[Dan Blanchette](https://github.com/Dan-Blanchette/)<br>
[Taylor Martin](https://github.com/Trmart/)<br>

# Installation

## Dependencies

#### Python and Pip
Project is built using Python `3.10.7` and Pip `22.2.2` 

#### Packages
- 'dash'
- 'dash-bootstrap-components'
- 'dash-cytoscape'
- 'pandas'
- 'treelib'
- 'lorem'
- 'graphviz'


Use following command to install all packages:
```
pip3 install dash dash-bootstrap-components dash-cytoscape lorem pandas treelib graphviz
```

Or you can use pip to install all the packages from our reuirements.txt:
```
pip install -r requirements.txt
```

Run this command to start server
```
python3 gSearch_redux.py
```

#### Graphviz
After those packages are installed, You need to install the Graphviz graph generation software here:
<br>
[Graphviz install](https://www.graphviz.org/)<br>
