import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sica",
    version="0.0.1",
    author="Nicolas Captier",
    author_email="nicolas.captier@curie.fr",
    description="Stabilized ICA algorithm and applications to single-cell data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ncaptier/Stabilized_ICA",
    packages=setuptools.find_packages(),
    install_requires = [
        "anndata == 0.7.5",
        "joblib >= 0.17.0",
        "matplotlib >= 3.2.2",
        "networkx == 2.4",
        "numpy >= 1.18.5",
        "pandas >= 1.0.5",
        "python-picard == 0.4",
        "tqdm == 4.47.0",
        "scikit-learn >= 0.23.1",
        "scipy >= 1.5.0",
        "umap-learn == 0.4.6",        
        ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
