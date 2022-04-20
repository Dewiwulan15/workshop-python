#starting conda: menggunakan Anaconda prompt

#Managing conda
"""
(base) C:\Users\HP>conda --version
conda 4.12.0

(base) C:\Users\HP>conda update conda
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\HP\anaconda3

  added / updated specs:
    - conda


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    conda-package-handling-1.8.1|   py39h8cc25b3_0         729 KB
    ------------------------------------------------------------
                                           Total:         729 KB

The following packages will be UPDATED:

  conda-package-han~                   1.7.3-py39h8cc25b3_1 --> 1.8.1-py39h8cc25b3_0


Proceed ([y]/n)? y


Downloading and Extracting Packages
conda-package-handli | 729 KB    | #################################################### | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
"""

#Managing environments
"""
(base) C:\Users\HP>conda create --name snowflakes biopython
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\HP\anaconda3\envs\snowflakes

  added / updated specs:
    - biopython


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    biopython-1.78             |   py39h2bbff1b_0         2.1 MB
    ca-certificates-2022.3.29  |       haa95532_0         122 KB
    certifi-2021.10.8          |   py39haa95532_2         152 KB
    numpy-1.21.5               |   py39h7a0a035_1          25 KB
    numpy-base-1.21.5          |   py39hca35cd5_1         4.4 MB
    openssl-1.1.1n             |       h2bbff1b_0         4.8 MB
    python-3.9.12              |       h6244533_0        17.1 MB
    setuptools-61.2.0          |   py39haa95532_0         1.0 MB
    six-1.16.0                 |     pyhd3eb1b0_1          18 KB
    sqlite-3.38.2              |       h2bbff1b_0         807 KB
    tzdata-2022a               |       hda174b7_0         109 KB
    wheel-0.37.1               |     pyhd3eb1b0_0          33 KB
    ------------------------------------------------------------
                                           Total:        30.7 MB

The following NEW packages will be INSTALLED:

  biopython          pkgs/main/win-64::biopython-1.78-py39h2bbff1b_0
  blas               pkgs/main/win-64::blas-1.0-mkl
  ca-certificates    pkgs/main/win-64::ca-certificates-2022.3.29-haa95532_0
  certifi            pkgs/main/win-64::certifi-2021.10.8-py39haa95532_2
  intel-openmp       pkgs/main/win-64::intel-openmp-2021.4.0-haa95532_3556
  mkl                pkgs/main/win-64::mkl-2021.4.0-haa95532_640
  mkl-service        pkgs/main/win-64::mkl-service-2.4.0-py39h2bbff1b_0
  mkl_fft            pkgs/main/win-64::mkl_fft-1.3.1-py39h277e83a_0
  mkl_random         pkgs/main/win-64::mkl_random-1.2.2-py39hf11a4ad_0
  numpy              pkgs/main/win-64::numpy-1.21.5-py39h7a0a035_1
  numpy-base         pkgs/main/win-64::numpy-base-1.21.5-py39hca35cd5_1
  openssl            pkgs/main/win-64::openssl-1.1.1n-h2bbff1b_0
  pip                pkgs/main/win-64::pip-21.2.4-py39haa95532_0
  python             pkgs/main/win-64::python-3.9.12-h6244533_0
  setuptools         pkgs/main/win-64::setuptools-61.2.0-py39haa95532_0
  six                pkgs/main/noarch::six-1.16.0-pyhd3eb1b0_1
  sqlite             pkgs/main/win-64::sqlite-3.38.2-h2bbff1b_0
  tzdata             pkgs/main/noarch::tzdata-2022a-hda174b7_0
  vc                 pkgs/main/win-64::vc-14.2-h21ff451_1
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.27.29016-h5e58377_2
  wheel              pkgs/main/noarch::wheel-0.37.1-pyhd3eb1b0_0
  wincertstore       pkgs/main/win-64::wincertstore-0.2-py39haa95532_2


Proceed ([y]/n)? y


Downloading and Extracting Packages
openssl-1.1.1n       | 4.8 MB    | #################################################### | 100%
numpy-base-1.21.5    | 4.4 MB    | #################################################### | 100%
sqlite-3.38.2        | 807 KB    | #################################################### | 100%
wheel-0.37.1         | 33 KB     | #################################################### | 100%
ca-certificates-2022 | 122 KB    | #################################################### | 100%
setuptools-61.2.0    | 1.0 MB    | #################################################### | 100%
numpy-1.21.5         | 25 KB     | #################################################### | 100%
python-3.9.12        | 17.1 MB   | #################################################### | 100%
tzdata-2022a         | 109 KB    | #################################################### | 100%
certifi-2021.10.8    | 152 KB    | #################################################### | 100%
biopython-1.78       | 2.1 MB    | #################################################### | 100%
six-1.16.0           | 18 KB     | #################################################### | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate snowflakes
#
# To deactivate an active environment, use
#
#     $ conda deactivate


(base) C:\Users\HP>conda info --envs
# conda environments:
#
base                  *  C:\Users\HP\anaconda3
snowflakes               C:\Users\HP\anaconda3\envs\snowflakes
"""

#Managing Python
"""
(base) C:\Users\HP>conda create --name snakes python=3.9
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\HP\anaconda3\envs\snakes

  added / updated specs:
    - python=3.9


The following NEW packages will be INSTALLED:

  ca-certificates    pkgs/main/win-64::ca-certificates-2022.3.29-haa95532_0
  certifi            pkgs/main/win-64::certifi-2021.10.8-py39haa95532_2
  openssl            pkgs/main/win-64::openssl-1.1.1n-h2bbff1b_0
  pip                pkgs/main/win-64::pip-21.2.4-py39haa95532_0
  python             pkgs/main/win-64::python-3.9.12-h6244533_0
  setuptools         pkgs/main/win-64::setuptools-61.2.0-py39haa95532_0
  sqlite             pkgs/main/win-64::sqlite-3.38.2-h2bbff1b_0
  tzdata             pkgs/main/noarch::tzdata-2022a-hda174b7_0
  vc                 pkgs/main/win-64::vc-14.2-h21ff451_1
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.27.29016-h5e58377_2
  wheel              pkgs/main/noarch::wheel-0.37.1-pyhd3eb1b0_0
  wincertstore       pkgs/main/win-64::wincertstore-0.2-py39haa95532_2


Proceed ([y]/n)? y

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate snakes
#
# To deactivate an active environment, use
#
#     $ conda deactivate


(base) C:\Users\HP>conda info --envs
# conda environments:
#
base                  *  C:\Users\HP\anaconda3
snakes                   C:\Users\HP\anaconda3\envs\snakes
snowflakes               C:\Users\HP\anaconda3\envs\snowflakes


(base) C:\Users\HP>python --version
Python 3.9.7
"""

#Managing packages
"""
                  0.9.7            py39h2eaa2aa_1
ruamel_yaml               0.15.100         py39h2bbff1b_0
sastrawi                  1.0.1                    pypi_0    pypi
scatterd                  1.1.1                    pypi_0    pypi
scikit-image              0.18.3           py39hf11a4ad_0
scikit-learn              0.24.2           py39hf11a4ad_1
scikit-learn-intelex      2021.3.0         py39haa95532_0
scipy                     1.7.1            py39hbe87c03_2
seaborn                   0.11.2             pyhd3eb1b0_0
send2trash                1.8.0              pyhd3eb1b0_1
setuptools                58.0.4           py39haa95532_0
simplegeneric             0.8.1            py39haa95532_2
singledispatch            3.7.0           pyhd3eb1b0_1001
sip                       4.19.13          py39hd77b12b_0
six                       1.16.0             pyhd3eb1b0_0
sklearn                   0.0                      pypi_0    pypi
snappy                    1.1.8                h33f27b4_0
sniffio                   1.2.0            py39haa95532_1
snowballstemmer           2.1.0              pyhd3eb1b0_0
sortedcollections         2.1.0              pyhd3eb1b0_0
sortedcontainers          2.4.0              pyhd3eb1b0_0
soupsieve                 2.2.1              pyhd3eb1b0_0
sphinx                    4.2.0              pyhd3eb1b0_1
sphinxcontrib             1.0              py39haa95532_1
sphinxcontrib-applehelp   1.0.2              pyhd3eb1b0_0
sphinxcontrib-devhelp     1.0.2              pyhd3eb1b0_0
sphinxcontrib-htmlhelp    2.0.0              pyhd3eb1b0_0
sphinxcontrib-jsmath      1.0.1              pyhd3eb1b0_0
sphinxcontrib-qthelp      1.0.3              pyhd3eb1b0_0
sphinxcontrib-serializinghtml 1.1.5              pyhd3eb1b0_0
sphinxcontrib-websupport  1.2.4                      py_0
spyder                    5.1.5            py39haa95532_1
spyder-kernels            2.1.3            py39haa95532_0
sqlalchemy                1.4.22           py39h2bbff1b_0
sqlite                    3.36.0               h2bbff1b_0
statsmodels               0.12.2           py39h2bbff1b_0
sympy                     1.9              py39haa95532_0
tbb                       2021.4.0             h59b6b97_0
tbb4py                    2021.4.0         py39h59b6b97_0
tblib                     1.7.0              pyhd3eb1b0_0
terminado                 0.9.4            py39haa95532_0
testpath                  0.5.0              pyhd3eb1b0_0
text-unidecode            1.3                pyhd3eb1b0_0
textdistance              4.2.1              pyhd3eb1b0_0
threadpoolctl             2.2.0              pyh0d69192_0
three-merge               0.1.1              pyhd3eb1b0_0
tifffile                  2021.7.2           pyhd3eb1b0_2
tinycss                   0.4             pyhd3eb1b0_1002
tk                        8.6.11               h2bbff1b_0
toml                      0.10.2             pyhd3eb1b0_0
toolz                     0.11.1             pyhd3eb1b0_0
tornado                   6.1              py39h2bbff1b_0
tqdm                      4.62.3             pyhd3eb1b0_1
traitlets                 5.1.0              pyhd3eb1b0_0
typed-ast                 1.4.3            py39h2bbff1b_1
typing_extensions         3.10.0.2           pyh06a4308_0
tzdata                    2021e                hda174b7_0
ujson                     4.0.2            py39hd77b12b_0
unicodecsv                0.14.1           py39haa95532_0
unidecode                 1.2.0              pyhd3eb1b0_0
urllib3                   1.26.7             pyhd3eb1b0_0
vc                        14.2                 h21ff451_1
vs2015_runtime            14.27.29016          h5e58377_2
watchdog                  2.1.3            py39haa95532_0
wcwidth                   0.2.5              pyhd3eb1b0_0
webencodings              0.5.1            py39haa95532_1
werkzeug                  2.0.2              pyhd3eb1b0_0
wget                      3.2                      pypi_0    pypi
wheel                     0.37.0             pyhd3eb1b0_1
whichcraft                0.6.1              pyhd3eb1b0_0
widgetsnbextension        3.5.1            py39haa95532_0
win_inet_pton             1.1.0            py39haa95532_0
win_unicode_console       0.5              py39haa95532_0
wincertstore              0.2              py39haa95532_2
winpty                    0.4.3                         4
wrapt                     1.12.1           py39h196d8e1_1
xlrd                      2.0.1              pyhd3eb1b0_0
xlsxwriter                3.0.1              pyhd3eb1b0_0
xlwings                   0.24.9           py39haa95532_0
xlwt                      1.3.0            py39haa95532_0
xmltodict                 0.12.0             pyhd3eb1b0_0
xz                        5.2.5                h62dcd97_0
yaml                      0.2.5                he774522_0
yapf                      0.31.0             pyhd3eb1b0_0
zfp                       0.5.5                hd77b12b_6
zict                      2.0.0              pyhd3eb1b0_0
zipp                      3.6.0              pyhd3eb1b0_0
zlib                      1.2.11               h62dcd97_4
zope                      1.0              py39haa95532_1
zope.event                4.5.0            py39haa95532_0
zope.interface            5.4.0            py39h2bbff1b_0
zstd                      1.4.9                h19a0ad4_0
"""