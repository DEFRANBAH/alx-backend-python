def insert(*args, **kwargs):
    print("{}-{}".format(args, kwargs))

insert("best",)
insert("best", 89)
insert(best="school")
insert("school", 89, name="best", number=89)
insert()


