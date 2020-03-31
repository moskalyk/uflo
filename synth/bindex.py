from environment_binaural import BandSpace
import argparse

# parser.add_argument('integers', metavar='N', type=int, nargs='+',help='an integer for the accumulator')
parser.add_argument('--composed', help='play binaural')
parser.add_argument('--binaural', help='play binaural')
parser.add_argument('--multiplayer', help='play binaural')

args = parser.parse_args()
print(args.accumulate(args.integers))



if __name__ == '__main__':

	if args.composed:
		print('composed')
	else:
		print('nope')

	if args.binaural:
		print('binaural')

	if args.multiplayer:
		print('multiplayer')

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