> Uncomment the below to enable extension, and install libraries


```python
#!jupyter nbextension enable --py widgetsnbextension
#!pip install numpy pandas ipywidgets
```


```python
from __future__ import print_function
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
import pandas as pd
import numpy as np

```


```python
@interact(size=list(range(1, 21)))
def main(size):
    if not isinstance(size, int):
        size = 12
    final = np.zeros((size, size))
    for i in range(size):
        for k in range(size):
            final[i, k] = ((i+1) * (k+1))
    display(pd.DataFrame(final.astype(int)))
```


    interactive(children=(Dropdown(description='size', options=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,…

