# What's this
Visualize SQL relationship for SQLAlchemy ORM.

You can get dot file for graphviz.
```bash
viz_alchemy -i example\test_db.py
```

# Installation
You can install from pip.

```bash
pip install viz_alchemy
```

or

```bash
python setup.py install
```

# Usage
```
usage: viz_alchemy [-h] -i INPUT [-o OUTPUT] [-n NAME] [-f FORMAT]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input script path
  -o OUTPUT, --output OUTPUT
                        Output file
  -n NAME, --name NAME  class name at the input file
  -f FORMAT, --format FORMAT
```

Now format is not working.

# ToDO
- Add unit test
- Code refactoring for more update
- Directly convert dot to image using graphviz.