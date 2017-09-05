cd  /home/lhm/gtest/liudayeblogs
hexo clean
hexo g
python /home/lhm/gtest/liudayeblogs/python/Main.py
rm public/vip/ -Rf
cp -ri source/vip/  public/vip/
hexo s
