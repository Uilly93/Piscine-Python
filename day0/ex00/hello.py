ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}


# modifying ft_list
ft_list[1] = "World!"

# modifying ft_tuple
tmp = list(ft_tuple)
tmp[1] = "France!"
ft_tuple = tuple(tmp)

# modifying ft_set
tmp = list(ft_set)
tmp.append("Paris!")
ft_set.update(tmp)
ft_set.remove("tutu!")

# mofifying ft_dict
ft_dict["Hello"] = "42Paris"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
