from evaluation.model import Model


def forwardSelection(trainingSettings):
    all_features = ["bow", "kuhn_munkres", "length_diff", "q_features", "ref_hedg_bow", "SVO_ppdb", "word2vec"]
    best_features = []

    for i in range(5):
        # print(best_features)
        max_accuracy_temp = 0
        feature_to_add = ""
        for feature in all_features:
            best_features.append(feature)  # Add the feature to test to the list
            print("TESTING: ", best_features)

            # Train the model with the given features
            model = Model(
                "train_and_test",
                features=best_features,
                classifier="SVM",
                settings=trainingSettings
            )

            if(model.results > max_accuracy_temp):
                max_accuracy_temp = model.results
                feature_to_add = feature

            best_features.remove(feature)

        best_features.append(feature_to_add)
        all_features.remove(feature_to_add)

        print("BEST FEATURES: ", best_features)
        print("Accuracy: ", max_accuracy_temp)


def backwardSelection(trainingSettings):
    best_features = ["bow", "kuhn_munkres", "length_diff", "q_features", "ref_hedg_bow", "SVO_ppdb", "word2vec"]

    while len(best_features) > 5:
        max_accuracy_temp = 0
        feature_to_remove = ""

        testing_features = best_features.copy()

        for feature_being_removed in best_features:
            testing_features.remove(feature_being_removed)
            model = Model(
                "train_and_test",
                features=best_features,
                classifier="SVM",
                settings=trainingSettings
            )
            if(model.results > max_accuracy_temp):
                max_accuracy_temp = model.results
                feature_to_remove = feature_being_removed

            testing_features.append(feature_being_removed)

        best_features.remove(feature_to_remove)
        print(best_features)
        print(max_accuracy_temp)

    print(Model(
        "train_and_test",
        features=best_features,
        classifier="Naive Bayes",
        settings=trainingSettings
    ).results)