"""
Script for running notebooks and (optionally) replacing results

Example:

.. code:: bash

    # Run all notebooks
    python src/docs/run-notebooks.py
    #
    # Run specific notebook(s) and don't replace results
    python src/docs/run-notebooks.py --replace=False \
        notebooks/extractor.ipynb
"""


# standard libaries
from glob import glob
from pathlib import Path

# third party libraries
import click
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from tqdm import tqdm

REPO_ROOT = Path(__file__).parents[2]
NB_ROOT = REPO_ROOT / "notebooks"

NB_TIMEOUT = 600


def run_notebook(nb_path: str, replace: bool = True) -> None:
    """
    Runs a Jupyter notebook from a path and (optionally) saves it back to the
    same path

    Args:
        nb_path (str): Path to the notebook
        replace (bool, optional): Replace the notebook. Defaults to True.
    """
    with open(nb_path, "r") as fp:
        nb = nbformat.read(fp, as_version=4)
        ep = ExecutePreprocessor(timeout=NB_TIMEOUT, kernel_name="python3")

        ep.preprocess(nb, {"metadata": {"path": NB_ROOT}})

    if replace:
        with open(nb_path, "wt") as fp:
            nbformat.write(nb, fp)


@click.command()
@click.option("--replace", default=True, help="Replace output with notebook results")
@click.argument("notebooks", nargs=-1, type=click.STRING, default=None)
def main(replace, notebooks):
    """Run Notebook Script"""
    notebooks = notebooks or glob(str(NB_ROOT / "*.ipynb"))

    print("Collected Notebooks:\n-", "\n- ".join(notebooks))

    with tqdm(notebooks) as progress:
        for path in progress:
            # Set filename as progress description
            progress.set_description(path.split("/")[-1])

            # Run notebook and replace with results
            run_notebook(path, replace=replace)


if __name__ == "__main__":
    main()
