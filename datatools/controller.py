import datetime as dt
# import pandas as pd


class Controller(object):
    """Class object to manage and log data cleaning processes

        After using the controller, syntax to get X and y would be:
        X = controller.features
        y = controller.target

        OR

        Xtrain, Xtest, ytrain, ytest = controller.train_test_split()
    """

    def __init__(self, raw_data, target=None):
        self.raw_data = raw_data
        self._created_date = dt.datetime.today()
        self.log = None
        self.train = None
        self.test = None
        if target is not None:
            self.target = raw_data[target]
            self.features = raw_data.drop(target, axis=1)
            self.create_log()

    def extract_target(self, target_col_name):
        """User identifies which column is the target variable
        """
        self.target = self.raw_data[target_col_name]
        self.features = self.raw_data.drop(target_col_name, axis=1)

        self.log = self.create_log()

    def create_log(self):
        """Dictionary of feature names and last modifications
        """
        columns = self.features.columns
        self.log = {}
        for col in columns:
            self.log[col] = []

    def record(self, f, **kwargs):
        orig_features = self.features.copy()
        orig_columns = orig_features.columns
        mod_features = f(**kwargs)
        mod_columns = mod_features.columns
        orig_and_mod = [col for col in orig_columns if col in mod_columns]
        # check if number of columns has changed
        if len(mod_columns) != len(orig_columns):
            print('columns added')
            # check if columns have been added
            if len(mod_columns) > len(orig_columns):
                for col in mod_columns:
                    if col not in orig_columns:
                        # self.log[col] = []
                        self.log[col] = ["Added by {}".format(f.__name__)]
            # check if columns have been dropped
            else:
                for col in orig_columns:
                    if col not in mod_columns:
                        self.log[col].append("Deleted by {}"
                                             .format(f.__name__))

        # check if columns have been modified
        for col in orig_and_mod:
            if not orig_features[col].equals(mod_features[col]):
                self.log[col].append("Modified by {}".format(f.__name__))
        self.features = mod_features
