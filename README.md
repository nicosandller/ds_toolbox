# Data science toolbox
Tools for data science exploration.


## installation
To install, run:
```
pip install git+https://github.com/nicosandller/#egg=ds_toolbox
```

## update
To update, run:
```
pip install --upgrade git+https://github.com/nicosandller/ds_toolbox#egg=ds_toolbox
```


## Model Evaluation

These are tools for model evaluation. For classification problems an example would be to use `build_classification_report` as follows:
```
report_V1 = build_classification_report(
                          true_target_data, predicted_target_data,
                          class_labels=["negative", "neutral", "positive"]
)
```
which would output the following report:

<img src="https://github.com/nicosandller/ds_toolbox/blob/master/screenshots/Screen%20Shot%202019-10-17%20at%2017.10.18.png" width="500" height="450">
