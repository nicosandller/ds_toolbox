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

![classification_report](/screenshots/class_eval.png? "Classification report example")
