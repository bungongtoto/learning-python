#!/usr/bin/env python3
import tensorflow as tf 
hello_str ="Hello World"
hello_int = 1
hello_bool = True
hello_tuple = (21,34)
hello_list = ["hello", "this", "is", "a", "list"]


hello_list = list() #this is used to initialize a empty list

hello_list.append("hello")
hello_list.append("this")
hello_list.append("is")
hello_list.append("a")
hello_list.append("list")


hello_dic = {
    "fist_name": "BUNGONG",
    "last_name": "NDZI",
    "eye_color": "brown",
}

print(hello_list[4])

hello_list[4] += "!"

print(hello_list[4])

print(str(hello_tuple))

print(f"{hello_dic['fist_name']} {hello_dic['last_name']} has {hello_dic['eye_color']} eyes")


