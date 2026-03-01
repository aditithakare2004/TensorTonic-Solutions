import numpy as np

def roc_curve(y_true, y_score):
    """
    Compute ROC curve from binary labels and scores.
    """
    # Write code here

    y_true = np.asarray(y_true)
    y_score = np.asarray(y_score)

    # sort by descending score
    order = np.argsort(-y_score)
    y_true = y_true[order]
    y_score = y_score[order]

    P = np.sum(y_true == 1)
    N = np.sum(y_true == 0)

    # cumulative sums
    tp = np.cumsum(y_true == 1)
    fp = np.cumsum(y_true == 0)

    # 🔥 keep only where score changes
    distinct = np.where(np.diff(y_score))[0]
    idx = np.r_[distinct, len(y_score) - 1]

    tp = tp[idx]
    fp = fp[idx]
    thresholds = y_score[idx]

    # rates
    tpr = tp / P if P > 0 else np.zeros_like(tp, dtype=float)
    fpr = fp / N if N > 0 else np.zeros_like(fp, dtype=float)

    # add starting point
    tpr = np.r_[0.0, tpr]
    fpr = np.r_[0.0, fpr]
    thresholds = np.r_[np.inf, thresholds]

    return fpr, tpr, thresholds