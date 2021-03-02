def filter_mgf(input_feature_table,input_mgf):
	# Open a .csv file with the features you want to delete
	with open(input_feature_table, 'r') as features:
		lines = features.read()

	# Create a list with the features to be deleted    
	to_delete = lines.splitlines()


	# Open .mgf file exported from MZmine
	with open(input_mgf, 'r') as f:
		lines2 = f.read()

	# Create a list with data to be compared
	delete_from = lines2.splitlines()


	# Create a list of lists, separeted by blank line in the .mgf file
	size = len(delete_from)
	idx_list = [idx + 1 for idx, val in
				enumerate(delete_from) if val == '']
	res = [delete_from[i: j] for i, j in zip([0] + idx_list, idx_list + ([size] if idx_list[-1] != size else []))] #resulting list

	# Loop to compare both lists and delete the matches
	for i in range(len(res)):
		for n in to_delete:
			try:
				if n == res[i][1][11:]:
					del res[i]
			except IndexError:
				break

	# Save new .mgf file filtered
	with open(input_mgf[:-4]+'_filtered.mgf', 'w') as f:
		for n in range(len(res)):
			for i in range(len(res[n])):
				print(res[n][i], end='\n', file=f)

