from sklearn.metrics import (
    confusion_matrix, classification_report, roc_auc_score, log_loss, accuracy_score, roc_curve, auc
)


def build_classification_report(target_test_data, target_predictions, class_labels):
    print("Definition reminder:")
    print("\nAccuracy = (True Pos + True Neg)/(TP + TN + FP + FN)")
    print("Precision = (True Pos) / (True Pos + False Pos)")
    print("Recall = (True Pos) / (True Pos + False Neg)")

    # Calculamos el accuracy
    print("\n Accuracy: {}".format(accuracy_score(target_test_data, target_predictions)))

    # Classification report
    report = classification_report(target_test_data, target_predictions)
    report_as_dict = classification_report(target_test_data, target_predictions, output_dict=True)
    print('\n' + report)

    conf_mat = confusion_matrix(target_test_data, target_predictions, labels=class_labels)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(conf_mat, cmap=plt.cm.Blues)
    fig.colorbar(cax)

    for i in range(conf_mat.shape[0]):
        for j in range(conf_mat.shape[1]):
            plt.text(j, i, conf_mat[i, j], ha="center", va="center", color="r")

    ax.set_xticklabels([''] + class_labels)
    ax.set_yticklabels([''] + class_labels)
    plt.xlabel('Predicted')
    plt.ylabel('Expected')
    plt.show()
    
    return report_as_dict
