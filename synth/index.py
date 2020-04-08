import argparse
import os
import subprocess
from multiprocessing import Process

help = 'possible options: composed, singleplayer, multiplayer'
device = 'possible options: bci, offline'

parser = argparse.ArgumentParser(description='~uflo: binaural neural toolkit')
parser.add_argument('--mode', help=help)
parser.add_argument('--device', help=device)
args = parser.parse_args()

if args.mode == None:
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print('Please include flow type.')
	print()
	print('i.e. ' + help)
	print()
	print('example: $ python3 index.py --mode binaural')
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print()
	print('~uflo with love.')
	exit()

b = None

if __name__ == '__main__':

	from environment import BandSpace

	experiment_name = None

	# check if bci device is connected
	if args.device == 'bci':
		print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
		experiment_name = input('What should we call this session? > ')
		print("Beginning the Experiment: " + experiment_name)
		print("In Mode: " + args.mode)

		print('Looking for socket stream connected')
		b.connect_bci()
	
	# TODO: start audio server in background process, this doesn't kill on exit :(
	# os.system('sudo sclang ../sounds/source.scd &')

	# intantiate bandspace
	b = BandSpace(experiment_name)

	try:
		
		# play bands on mode type
		if args.mode == 'composed':
			band_sequence = [1,2,3,4]

			for i in range(len(band_sequence)):
				print('Playing next band with index ' + str(i))
				b.new_band(band_sequence[i]) 


		if args.mode == 'binaural':

			b.binaural() 

		if args.mode == 'multiplayer':
			print('TODO')

		print('Composing')
		b.compose()

	except KeyboardInterrupt:
		print('Removing sound')
		# b.compose()
		b.clear_band_space()
	except RuntimeError as e:
		print(e)
		print('Something went wrong in data collection.')
		b.clear_band_space()