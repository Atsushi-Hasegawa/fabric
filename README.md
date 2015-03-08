#### 概要
python,fabricのインストール方法
- python2.7のインストール
```
cd /usr/local/src
sudo wget --no-check-certificate http://www.python.org/ftp/python/2.7.7/Python-2.7.7.tgz
sudo tar zxvf ./Python-2.7.7.tgz
cd ./Python-2.7.7
sudo ./configure --prefix=/usr/local/python-2.7 --enable-shared
sudo make
sudo make install
```
- パスを通す
```
sudo ln -s /usr/local/python-2.7/bin/python /usr/local/bin/python
sudo ln -s /usr/local/python-2.7/lib/libpython2.7.so.1.0 /lib64/
```
- easy_install2.7をインストール
```
wget --no-check-certificate http://pypi.python.org/packages/source/d/distribute/distribute-0.6.35.tar.gz
tar xf distribute-0.6.35.tar.gz
cd distribute-0.6.35
sudo /usr/local/python2.7/bin/python2.7 setup.py install
sudo ln -sf /usr/local/python-2.7/bin/easy_install-2.7 /usr/bin/easy_install-2.7
easy_install-2.7 --help
```
- fabricのインストール
```
sudo easy_install-2.7 fabric
sudo ln -sf /usr/local/python-2.7/bin/fab /usr/bin
```
fabricでのデプロイ方法
#### 手順

```
fab -f <デプロイスクリプト> <コマンド> -H <ホスト>
```
