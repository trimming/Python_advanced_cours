# def make_dict(name, things):
#     my_dict[name] = things
#
#
# my_dict = {}
# make_dict('Ben', ('boat', 'eat', 'watch'))
# make_dict('John', ('axe', 'eat', 'watch'))
# make_dict('Sten', ('matches', 'eat', 'bag'))
# union_set = set()
# inter_set = set()
# for key,value in my_dict.items():
#     my_dict[key] = set(value)
#     union_set = union_set | set(value)
# for i in union_set:
#
#
# print(union_set)
# print(inter_set)

friends = {
    'Максим': ('топор', 'вода', 'еда', 'палатка'),
    'Шамиль': ('топор', 'вода', 'закуска', 'карты'),
    'Сергей': ('топор', 'водка', 'еда', 'карты')
}


all_things = set()
for friend_item in friends.values():
    all_things.update(set(friend_item))

have_all_friends = all_things.copy()
for friend_item in friends.values():
    have_all_friends.intersection_update(friend_item)
print('Вещи, которые есть у всех:')
print(*have_all_friends)
print()

only_one_friend = {}
for friend in friends:
    friend_backpack = set(friends[friend])
    for other_friend in friends:
        if friend != other_friend:
            friend_backpack.difference_update(friends[other_friend])
    if friend_backpack:
        only_one_friend[friend] = friend_backpack
print('Есть только у одного:', *[f'{name}: {", ".join(back)}' for name, back in only_one_friend.items()], sep='\n')
print()

all_except_one_friend = {}
for friend in friends:
    friend_backpack = friends[friend]
    friends_backpacks = all_things.copy()
    for other_friend in friends:
        if friend != other_friend:
            friends_backpacks.intersection_update(friends[other_friend])
    friends_backpacks.difference_update(friend_backpack)
    if friends_backpacks:
        all_except_one_friend[friend] = friends_backpacks
print('Есть у всех, кроме одного:', *[f'{name} не взял: {", ".join(back)}' for name, back in all_except_one_friend.items()], sep='\n')