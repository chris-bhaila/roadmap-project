class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None,
                 class_distribution=None, leaf=False):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.class_distribution = class_distribution
        self.leaf = leaf

    def is_leaf(self):
        return self.leaf


def predict_proba(tree, sample, feature_list, top_k=5, borrow_factor=0.4):
    node = tree
    path = [node]
    while not node.is_leaf():
        j = feature_list.index(node.feature)
        value = sample[j]
        node = node.left if value <= node.threshold else node.right
        path.append(node)

    combined = dict(path[-1].class_distribution)

    for ancestor in reversed(path[:-1]):
        if len(combined) >= top_k:
            break
        for cls, p in ancestor.class_distribution.items():
            if cls not in combined:
                combined[cls] = p * borrow_factor

    ranked = sorted(combined.items(), key=lambda kv: kv[1], reverse=True)
    return ranked[:top_k]
