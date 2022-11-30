# DUCATI

This repository contains some python components of DUCATI and the overall training scripts.
We put the underlying implementations of some APIs in a customized version of DGL (https://github.com/CSLabor/DUCATI_dgl.git).

Please follow these steps to prepare environment and datasets:
1. follow the [instructions](https://docs.dgl.ai/install/index.html#install-from-source) to install our [customized DGL](https://github.com/CSLabor/DUCATI_dgl.git) from source  
2. install other dependent libraries in `requirements.txt`
3. prepare the datasets: download PA from [OGB](https://ogb.stanford.edu/docs/nodeprop/#ogbn-papers100M), download UK & UU & TW from [GNNLab](https://github.com/SJTU-IPADS/fgnn-artifacts) and [WebGraph](https://webgraph.di.unimi.it)
4. pre-process the datasets using scripts in the `preprocess` directory

Then we run the DUCATI with different settings as follows:
```
CUDA_VISIBLE_DEVICES=0 python run.py --dataset [DS] --fanouts [DS] --dim [DM] --total-budget [TB]
```
