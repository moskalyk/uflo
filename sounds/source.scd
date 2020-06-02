
s.boot;

(
	s.waitForBoot({

	().play;
	"".postln;
	"Ready for mindfulness...".postln;

	// the sound synth
	SynthDef(\bin, {|prime = 200, diff = 10, fade = 10, primetime = 20, difftime = 10, level= 0.4, gate = 1|
		var freqtransition = VarLag.kr(prime, primetime, 0, \lin);
		var links = SinOsc.ar(freqtransition);
		var rechts = SinOsc.ar(freqtransition - VarLag.kr(diff, difftime, 0, \lin));
		var env = EnvGen.kr(Env.asr(fade, level, fade), gate, doneAction:2);
		Out.ar(0, [links, rechts] * env);
	}).store;


	SynthDef(\noise, {|out = 0, osc = 1, gain = 0.1|
		// "howdie".postln;
		// { Pan2.ar(BrownNoise.ar, SinOsc.kr(1), 0.3) }.scope(5);
		Out.ar(out, Pan2.ar(BrownNoise.ar, SinOsc.kr(osc), gain * 0.1));
		// SinOsc.ar(rrand(400, 800), 0,  SinOsc.kr(1))
		// Out.ar(out, SinOsc.ar(freq) * gain.dbamp);
	}).store;


	SynthDef(\pulse, {|out = 0, osc = 1, freq = 440.0, gain = 0.0|
		Out.ar(out, SinOsc.ar(freq, 0,  SinOsc.kr(osc)))
	}).store;


	SynthDef(\sine, { |out = 0, freq = 440.0, gain = 0.0|
		Out.ar(out, SinOsc.ar(freq) * gain.dbamp);
	}).store;


	SynthDef(\dust, { |out = 0, gain = 10.0, parts = 10 |
		var data = Dust.ar(parts) * gain.dbamp;
		Out.ar(out, Pan2.ar(data));
	}).store;

	SynthDef(\reverb, { |in = 0, out = 2|
		var data = In.ar(in, 2);
		data = FreeVerb.ar(data, 0.7, 0.8, 0.5);
		Out.ar(out, data);
	}).store;

	SynthDef(\neuro, {|in = 0, freq = 440.0, out = 2|
		var ampOsc;
		ampOsc = SinOsc.kr(0.5, 2pi, 1, 0.5);
			Out.ar(out, SinOsc.ar(freq, 0, ampOsc));
	}).store;

	})
)
