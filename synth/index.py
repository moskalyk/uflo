from environment import BandSpace

import argparse

parser = argparse.ArgumentParser(description='binaural neural toolkit')
parser.add_argument('--type', help='possible options: composed, singleplayer, multiplayer')
args = parser.parse_args()

if __name__ == '__main__':

	try:
		
		experiment_name = input('What should we call this session? > ')
		print("Beginning the Experiment: " + experiment_name)
		print("As type: " + args.type)

		if args.type == 'composed':
			band_sequence = [1,2,3,4]
			b = BandSpace(3, experiment_name)

		if args.type == 'binaural':
			band_sequence = [4]
			for i in range(len(band_sequence)):
				print('Playing next band with index ' + str(i))
				b.new_band(band_sequence[i]) 

		if args.type == 'multiplayer':
			print('TODO')


		print('Composing')
		b.compose()

	except KeyboardInterrupt:
		print('Removing sound')
		b.compose()
		b.clear_band_space()
	except RuntimeError:
		print('Something went wrong in data collection.')
		b.clear_band_space()