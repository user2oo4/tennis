# Tennis

## Overall file structure

1. data: Handling fetching and processing raw data
2. src: 
- player.py: basic Player class for stats
- data.py: data for reading and processing data
- utils.py: to be added (utils function to do operations on objects)
3. models/analytics
- make a new folder inside src to do any kind of folder, experiment
- feel free to make a new more specific class based on player, or any new class (such as head2head)
- however, the class directly inside src should be more generic, and more specific classes can be written within the model folder if needed

```
tennis/
├── src/
│   ├── player.py
│   ├── data.py
│   ├── model_1/
│   │   ├── __init__.py
│   │   └── simple.py
│   └── analytic_1/
│       └── __init__.py
├── data/
│   ├── raw/
│   └── processed/
└── ...
```

## How to start
1. venv and install libraries from requirements.txt
2. run scripts in data/scripts to get raw data
3. make a new folder in src to try out any different experiments with predictions, data analytics or any other sort of models