cd  /home/lhm/gtest/liudayeblogs
git pull
python /home/lhm/gtest/liudayeblogs/python/Main.py
hexo clean
hexo g
rm public/vip/ -Rf
cp -ri source/vip/  public/vip/
hexo d

