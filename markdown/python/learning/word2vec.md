## word2vec

- [word2vec: danielfrg/word2vec](https://github.com/danielfrg/word2vec)
- [word2veckeras: niitsuma/word2vec-keras-in-gensim](https://github.com/niitsuma/word2vec-keras-in-gensim)
- [theano-word2vec: newe101/word2vec](https://github.com/enewe101/word2vec)

##  spacy.io

- [https://spacy.io](https://github.com/spacy-io/spaCy)
- [sens2vec](https://github.com/spacy-io/sense2vec)


## gensim

- [gensim](http://radimrehurek.com/gensim/)


## Doc2Vec

- [Word2Vecの進化形Doc2Vecで文章と文章の類似度を算出する](http://qiita.com/okappy/items/32a7ba7eddf8203c9fa1)


~~~bash
$ pip install scipy
Collecting scipy
  Using cached scipy-0.18.0-cp27-cp27mu-manylinux1_x86_64.whl
Installing collected packages: scipy
Successfully installed scipy-0.18.0
~~~

~~~bash
$ pip install gensim
Collecting gensim
  Downloading gensim-0.13.2.tar.gz (6.4MB)
    100% |████████████████████████████████| 6.4MB 217kB/s
Collecting numpy>=1.3 (from gensim)
  Downloading numpy-1.11.1-cp27-cp27mu-manylinux1_x86_64.whl (15.3MB)
    100% |████████████████████████████████| 15.3MB 95kB/s
Requirement already satisfied (use --upgrade to upgrade): scipy>=0.7.0 in /home/vagrant/.anyenv/envs/pyenv/versions/dogs/lib/python2.7/site-packages (from gensim)
Requirement already satisfied (use --upgrade to upgrade): six>=1.5.0 in /home/vagrant/.anyenv/envs/pyenv/versions/dogs/lib/python2.7/site-packages (from gensim)
Collecting smart_open>=1.2.1 (from gensim)
  Downloading smart_open-1.3.4.tar.gz
Requirement already satisfied (use --upgrade to upgrade): boto>=2.32 in /home/vagrant/.anyenv/envs/pyenv/versions/dogs/lib/python2.7/site-packages (from smart_open>=1.2.1->gensim)
Collecting bz2file (from smart_open>=1.2.1->gensim)
  Downloading bz2file-0.98.tar.gz
Requirement already satisfied (use --upgrade to upgrade): requests in /home/vagrant/.anyenv/envs/pyenv/versions/dogs/lib/python2.7/site-packages (from smart_open>=1.2.1->gensim)
Building wheels for collected packages: gensim, smart-open, bz2file
  Running setup.py bdist_wheel for gensim ... done
  Stored in directory: /home/vagrant/.cache/pip/wheels/d7/0b/d9/c75b182a3a7910371a45cf7664083f4360510c9f0666c83c8f
  Running setup.py bdist_wheel for smart-open ... done
  Stored in directory: /home/vagrant/.cache/pip/wheels/86/b9/7e/8de494f4ac64b38d02c473709380ea87bb67a6e5d5c397b4a9
  Running setup.py bdist_wheel for bz2file ... done
  Stored in directory: /home/vagrant/.cache/pip/wheels/31/9c/20/996d65ca104cbca940b1b053299b68459391c01c774d073126
Successfully built gensim smart-open bz2file
Installing collected packages: numpy, bz2file, smart-open, gensim
Successfully installed bz2file-0.98 gensim-0.13.2 numpy-1.11.1 smart-open-1.3.4
~~~
