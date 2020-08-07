# branch_never_exists local de var ama githubda yok bakalım ekleyecek mi ? master to master push.
# "Commit 2.1"

# branch_never_exists de değişiklik yapıp pushlarken branche master veriyorum.
# "Commit 2.2" Everything up-to-date dedi.

# branch_never_exists de değişiklik duruyor ve bu satır ekleniyor. branche branch_never_exists veriyorum.
# "Commit 2.3" olarak gelmeli
# Githubda Yeni bir branch oluşturdu mastera atamadım. Commit 2.3.1

# Sadece test_script.py dosyasını mastera mergeliyorum ve master'ı pushluyorum.
# > git checkout master
# > git checkout branch_never_exists test_script.py
<<<<<<< HEAD
# "Commit 2.4" ile master'a eklenmeli (eklendi tik)

# yukarıdaki yöntemle test_script.py ı tekrar branch_never_exists le merglelüyorum.
# Bu sefer bu değişiklikleri bu branchten master a pushluyorum.
# > git push origin branch_never_exists:master
# Commit 2.5 ile mastera eklenmeli
=======
# "Commit 2.4" ile master'a eklenmeli
>>>>>>> 9b6f2f2c26d42911878dd78468dfc498bfcb8957

# Commit 2.5 teki çekilde eklenmiyormuş önce pull etmek gerkiyormuş. branch_never_exists2 ye git pull origin master ile
# pull ettim.
# C:\Users\oodabasi\Desktop\git denemeler\test_repo>git pull origin master
# From https://github.com/odabasionur/test_repo
#  * branch            master     -> FETCH_HEAD
# Auto-merging test_script.py
# CONFLICT (content): Merge conflict in test_script.py
# Automatic merge failed; fix conflicts and then commit the result.
# Yukarıda yorum olmayan satırlardaki gibi bazı şeyler ekledi git. Hata mı bug mı anlamadım.
# şimdi tekrar > git push origin branch_never_exists2:master deniyorum.
# Commit 2.6 ile mastera eklenmeli
