def all_thing_is_obj(object: any) -> int:
	objType = type(object)
	if objType == str:
		print(f'{object} is in the kitchen : {objType}')
	elif objType == tuple:
		print(f'Tuple : {objType}')
	elif objType == dict:
		print(f'Dict : {objType}')
	elif objType == list:
		print(f'List : {objType}')
	elif objType == set:
		print(f'Set : {objType}')
	elif not object:
		return 42
	else:
		print("type not found")
	return 42