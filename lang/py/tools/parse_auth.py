import json
import string


def get_json_from_file(fname):
    with open(fname) as f:
        data = json.load(f)
    return data


# hive create table sql:
# CREATE TABLE IF NOT EXISTS market.staff_member(id int COMMENT 'Integer Column',
# name string COMMENT 'String Column' ,
# member int);

INSERT_SQL = u'INSERT INTO market.staff_member (id,name,member) VALUES ({id},"{name}",{member}); '


def parse_lines(fname):
    with open(fname) as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        words = str(line).split(';')
        if len(words) == 3:
            # print(words[1], words[2][:-2])
            print(INSERT_SQL.format(id=i, name=words[1], member=words[2][:-2]))
