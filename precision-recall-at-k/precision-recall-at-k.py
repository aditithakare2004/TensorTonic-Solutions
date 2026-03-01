def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here

    # top-k recommendations
    top_k = recommended[:k]
    
    # convert relevant to set for fast lookup
    relevant_set = set(relevant)
    
    # count hits
    hits = sum(1 for item in top_k if item in relevant_set)
    
    # compute metrics
    precision = hits / k if k > 0 else 0.0
    recall = hits / len(relevant_set) if len(relevant_set) > 0 else 0.0
    
    return [float(precision), float(recall)]