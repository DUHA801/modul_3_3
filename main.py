def print_params(a = 1.34, b = 'строка', c = 'True'):
    print(a ,b , c)
print_params(b='25')
print_params(c=[1, 2, 3])
values_list =(1 , 'привет', 45.78)
values_dict = {'a':1.34 , 'b' : 'строка', 'c'  : 'True'}

def print_params(*value_list, **value_dict):
    print(*value_list, **value_dict)
values_list = (1, 'привет', 45.78)
values_dict = {'a': 1.34, 'b': 'строка', 'c': 'True'}
values_list_2 = [54.32,'Строка']
print_params(*values_list_2, 42)