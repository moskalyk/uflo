from environment_binaural import BandSpace

if __name__ == '__main__':

	experiment_name = input('What should we call this session? > ')
	print("Beginning the Experiment: " + experiment_name)

	b = BandSpace(3, experiment_name)

	try:
		# band_sequence = [1,2,3,4]
		# band_sequence = [0, 1, 2, 3]
		# band_sequence = [0,1,2,3]
		band_sequence = [4]

		for i in range(len(band_sequence)):
			print('Playing next band with index ' + str(i))
			b.new_band(band_sequence[i]) 

		print('Composing')
		b.compose()

	except KeyboardInterrupt:
		print('Removing sound')
		b.compose()
		b.clear_band_space()
	except RuntimeError:
		print('Something went wrong in data collection.')
		# b.clear_band_space()