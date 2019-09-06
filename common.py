#!/usr/bin/env python
# Import plt
import matplotlib.pyplot as plt

def show_image(image,Title="Image",cmap_type="gray"):
    plt.imshow(image,cmap=cmap_type)
    plt.title(Title)
    plt.axis('off')
    plt.show()