def info(name, *args, **kwargs):  # **kwargs 会把多传入的参数变成一个dict形式
    print(name, args)  # derek (22, 'CN', 'Python')
    print(kwargs)  # {'sex': 'Male', 'province': 'HeBei'}


info("derek", 22, "CN", "Python", sex="Male", province="HeBei")
