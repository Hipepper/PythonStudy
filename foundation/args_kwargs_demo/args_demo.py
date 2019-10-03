def info(name,age,*args):     #*args会把多传入的参数变成一个元祖形式
    print(name, age,args)

info("derek","22","CN","Python")     #derek 22 ('CN', 'Python')