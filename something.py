info = [
		{'site': 'github', 'password': 'Blitz123'},
		{'site': 'Youtube', 'password': '123'},
		{'site': 'Discord', 'password': '456'},
]

def get_info(action='view', **kwargs):
	try:
		resp = []
		actions = {
			'viewSites': ",".join([s['site'] for s in info]), 
			'viewPass': ",".join([s['password'] for s in info]),
			'view': "".join([f"Site: {s['site']}  Password: {s['password']}," for s in info]),
		}
		if action:
			if action != 'help':
				a = actions.get(action)
				resp.append(a)	
			elif action == 'help':
				res = {res for res in actions.keys()}
				resp.append(res)
		if kwargs.get('add', False):
			site = kwargs.get('site', " ")
			password = kwargs.get('password', " ")
			load_dict = dict(site=site, password= password)
			if load_dict in info:
				resp.append(f"{load_dict['site']} is already in the info list")
			else:
				info.append(load_dict)
				resp.append(info)
		if kwargs.get('remove', False):
			r_site = kwargs.get('site', " ")
			r_password = kwargs.get('password', " ")
			r_di = dict(site=r_site, password= r_password)
			if r_di in info:
				info.remove(r_di)
				resp.append(f"{r_site} has been removed!  {info}")
			else:
				resp.append(f"Could not find: {r_di['site']} in the list of sites")
		return resp
	except SyntaxError as err:
		return 'hm it looks like something went wrong :(' + err

