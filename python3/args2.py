def hard(*args, **kwargs):
    print("{}-{}".format(args, kwargs))

a_dict = {'illenium' : 'crawl_outalove', 'album' : 'ashes'}

hard(a_dict)
hard(*a_dict)
hard(**a_dict)

 
