

dic1 = { 'id1':{
        'name' : 'sora',
        'age': 12,
        'subjest':['math','english','science']
        },
        'id2':{
        'name' : 'nora',
        'age': 13,
        'subjest':['math','english','science']
        },
        'id1':{
        'name' : 'sora',
        'age': 12,
        'subjest':['math','english','science']
        },
        'id3':{
        'name' : 'rina',
        'age': 14,
        'subjest':['math','english','science']
        }}

result = {}

for key,value in dic1.items():
    if result.values() != value:
        result[key] = value


print('with out dupliicates')
print(result)