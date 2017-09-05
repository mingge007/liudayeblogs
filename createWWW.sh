cd  /home/lhm/gtest/liudayeblogs
git pull
python /home/lhm/gtest/liudayeblogs/python/Main.py
/home/lhm/gtest/liudayeblogs/node_modules/hexo/bin/hexo clean
/home/lhm/gtest/liudayeblogs/node_modules/hexo/bin/hexo g
rm public/vip/ -Rf
cp -ri source/vip/  public/vip/
#:wcp -f source/googlee579ed228d9e3be7.html public/googlee579ed228d9e3be7.html
/home/lhm/gtest/liudayeblogs/node_modules/hexo/bin/hexo d
