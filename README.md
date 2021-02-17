# Interactive Weak Supervision: Learning Useful Heuristics for Data Labeling
Code for text data experiments in:
`Benedikt Boecking, Willie Neiswanger, Eric Xing, and Artur Dubrawski. “Interactive Weak Supervision: Learning Useful Heuristics for Data Labeling.” (2020).`

Please check out the `IWS.ipynb` notebook. The notebook will walk you through an example application of IWS from start to finish. You can choose to
perform the experiment yourself, or to simulate an oracle which responds to queries about proposed labeling functions.  



## Dependencies
If you have access to GPUs and want to ensure they can be used, please first check the correct way to install torch on your system here:
https://pytorch.org  

Once you have installed pytorch or if you don't care about using a GPU for now, you can install all requirements as follows:

```
pip install -r requirements/requirements_pip.txt
# or
conda install -c conda-forge -c pytorch --file requirements/requirements_conda.txt
```

## Data

Download the data
```
cd datasets
wget https://ndownloader.figshare.com/files/25732838?private_link=860788136944ad107def -O iws_datasets.tar.gz
tar -xzvf iws_datasets.tar.gz
rm iws_datasets.tar.gz
```

tar -xzvf archive.tar.gz

## License

The code in this repository is shared under the MIT license, available in the LICENSE file.
