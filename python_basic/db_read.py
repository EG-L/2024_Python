import basic_17

# basic_17.db.insert()

# cur = basic_17.db.selectList()

# for row in cur:
#     print(row)

# basic_17.db.memberDelete(input("아이디 입력 :"))

# cur = basic_17.db.selectList()

# for row in cur:
#     print(row)

data = ('hong','박문수','남자','울산','010-1234-1234')

basic_17.db.memberUpdate(data)

cur = basic_17.db.selectList()

for row in cur:
    print(row)