#!/usr/bin/python3

language = 'python programming'
print(language, type(language))

question = 'how are you?'
print(question,type(question))

#where_abouts = 'what's up?'  #syntax error
where_abouts = 'what\'s up?'

#NOte: placing \ before any operator with result in treating operator as ordinary character

other_string = 'What\'s going in yours\' in-laws\' house'
print(other_string)

other_string = "What's going in yours' in-laws' house"
print(other_string)

other_string = '''What's going in yours' daughters "wedding*"'''
print(other_string)

db_command = '''select * from mytable where name like "bhargav*" '''
print(db_command)

db_command = '''select * from mytable where name like 'bhargav*' '''
print(db_command)

db_command = '''select * from mytable where name like 'bhargav*'; '''
print(db_command)


#multi line strings


print(
    "Today is awesome day \
    to learn python"
      )

print(
    'Today is awesome day \
    to learn python'
      )

print(
    "Today is awesome day" 
    "to learn python"
      )

print(
    {
    "Today is awesome day" 
    "to learn python"
    }
)

print(
    '''Today is awesome day \
    to learn python'''
      )

print(
    '''Today is awesome day 
    to learn python'''
      )

print(
    """Today is awesome day 
    to learn python"""
      )


print(
    '''
    A- APPLE
    C- CAT
    '''
)

sql_cmd = '''
    select * 
    from table t1
    LEFT join table t2 on t1.id = t2.id
    '''
print(sql_cmd)