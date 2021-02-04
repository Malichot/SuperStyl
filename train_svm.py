import jagen_will.svm
import pandas
import joblib


if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('train_path', action='store', help="Path to train file", type=str)
    parser.add_argument('test_path', action='store', help="Path to test file", type=str)
    parser.add_argument('--dim_reduc', action='store', choices=['pca', 'som'], help="optional dimensionality reduction of input data", default=None)
    parser.add_argument('--norms', action='store_true', help="perform normalisations?", default=False)
    parser.add_argument('--kernel', action='store',
                        help="type of kernel to use (default LinearSVC; possible alternatives, linear, polynomial, rbf, sigmoid)",
                        default="LinearSVC", choices=['LinearSVC', 'linear', 'polynomial', 'rbf', 'sigmoid'], type=str)
    parser.add_argument('--final', action='store_true', help="final analysis on unknown dataset (no evaluation)?", default=False)
    args = parser.parse_args()

    # path = "data/feats_tests_train.csv"
    # train_path = "data/feats_tests_realForTest.csv"
    # test_path = "data/feats_tests_valid_realForTest.csv"
    print(".......... loading data ........")
    train = pandas.read_csv(args.train_path, index_col=0)
    test = pandas.read_csv(args.test_path, index_col=0)

    svm = jagen_will.svm.train_svm(train, test, dim_reduc=args.dim_reduc, norms=args.norms,
                                   kernel=args.kernel, final_pred=args.final)

    joblib.dump(svm, 'mySVM.joblib')
