from ogb.nodeproppred import DglNodePropPredDataset

name = 'ogbn-papers100M'
graph = DglNodePropPredDataset(name=name)
mask = graph.ndata.pop('train_mask')
indptr, indices, _ = graph.adj_sparse(fmt='csc')
new_graph = dgl.graph(('csc', (indptr, indices, torch.tensor([]))), num_nodes=graph.num_nodes())
new_graph.ndata['train_mask'] = mask
dgl.save_graphs(f'dgl_{name}.bin', [new_graph])
