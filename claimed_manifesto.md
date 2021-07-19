The following list are the design principles behind CLAIMED – they are targeted at practical use in favor of the data scientists using the library

1. Everything what makes up a CLAIMED component is self-contained in a notebook – no additional deployment descriptors are necessary
1. Design by contract allows CLAIMED to make smart decisions if some deployment parameter isn’t defined. E.g. it should be possible to use an existing notebook without changes as good as possible
1. It is ok to mix bash/shell and python/R code in a single notebook
1. If no container image is specified, a default one is taken (currently continuumio/anaconda3:2021.05-alpine)
