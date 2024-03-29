sciencers={
   '爱婴':{
       'firstname':'艾因',
       'lastname':"斯坦"
   },
   '玛丽居里':{
       'firstname':'玛丽',
       'lastname':'居里'
   } 
}

print(sciencers)

for sci,sciinfo in sciencers.items():
    print(sci)
    print(sciinfo['firstname'])


# 对索引信息进行获取的话，要用到 items 函数
user_0 = {'username': 'efermi',
          'first': 'enrico',
          'last': 'fermi',
          }

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
