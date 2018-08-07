from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import numpy as np


def plot_roc(model, x_columns, y_true):
    """Returns a ROC plot

    Forked from Matt Drury.
    """

    y_pred = model.predict_proba(x_columns)

    fpr, tpr, threshold = roc_curve(y_true, y_pred[:, 1])
    area_under_curve = auc(fpr, tpr)

    # method I: plt
    fig, ax = plt.subplots()
    model_name = str(type(model)).split('.')[-1].strip(">\'")
    plt.title(f'{model_name} ROC')
    ax.plot(fpr, tpr, 'k', label='AUC = %0.3f' % area_under_curve)

    ax.legend(loc='lower right')
    ax.plot([0, 1], [0, 1], 'r--')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.show()


def plot_jitter(y_true, predictions, probability):
    fig, ax = plt.subplots(figsize=(12, 12))
    x = probability[:, 1]
    jitter = np.random.normal(loc=0, scale=0.05, size=len(y_true))
    y = y_true + jitter
    colors = ['red' if cls == 0 else 'blue' for cls in predictions]
    ax.scatter(x, y, color=colors, s=2, alpha=0.5)
