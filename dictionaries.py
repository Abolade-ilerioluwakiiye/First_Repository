favorite_languages={
	'jen':['java'],
	'sarah':['ruby'],
	'ileri':['python']
}

for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite language is:")
	for language in languages:
		print(f"\t{language.title()}.")

Ilerioluwakiiye={
	'first_name':['Ilerioluwa'],
	'last_name':['Abolade'],
	'age':[17]
}

for title, subject in Ilerioluwakiiye.items():
	print(f" Ilerioluwakiiye's {title.title()} is:")
	for subjects in subject:
		print(f"\t{subjects}")
