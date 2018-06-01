# datatools
Class object that logs functions that are run when processing raw data

## Installation
1. Clone this repo
2. Go to the directory of the cloned repo
3. `pip install .`

## Usage

#### Definition for a function that would modify and add new columns
```
def fill_and_dummy_binary(df, list_of_binary_col):
    for col in list_of_binary_col:
        dummy_name = "{}_was_null".format(col)
        df[dummy_name] = df[col].apply(lambda x: pd.isnull(x))
        df[col] = df[col].fillna(value=0)
    return df
```

#### Create Controller object
```
from datatools.controller import Controller
c = Controller(df, target='TARGET')

c.record(fill_and_dummy_binary, optional_notes="optional notes", df=c.features, list_of_binary_col=bool_cols.columns)
```

#### Sample of log
```
c.log
```
Output:
```
{'AMT_ANNUITY': [],
 'AMT_CREDIT': [],
 'AMT_GOODS_PRICE': [],
 'AMT_INCOME_TOTAL': [],
 'AMT_REQ_CREDIT_BUREAU_DAY': [],
 'AMT_REQ_CREDIT_BUREAU_HOUR': [],
 'AMT_REQ_CREDIT_BUREAU_MON': [],
 'AMT_REQ_CREDIT_BUREAU_QRT': [],
 'AMT_REQ_CREDIT_BUREAU_WEEK': [],
 'AMT_REQ_CREDIT_BUREAU_YEAR': [],
 'APARTMENTS_AVG': ['Modified by fill_and_dummy_binary; optional notes'],
 'APARTMENTS_AVG_was_null': ['Added by fill_and_dummy_binary; optional notes'],
 'APARTMENTS_MEDI': ['Modified by fill_and_dummy_binary; optional notes'],
 'APARTMENTS_MEDI_was_null': ['Added by fill_and_dummy_binary; optional notes'],
 'APARTMENTS_MODE': ['Modified by fill_and_dummy_binary; optional notes'],
 'APARTMENTS_MODE_was_null': ['Added by fill_and_dummy_binary; optional notes'],
 'BASEMENTAREA_AVG': ['Modified by fill_and_dummy_binary; optional notes'],
 ...
```
