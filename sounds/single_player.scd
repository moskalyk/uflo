s.boot;

// the sound synth
SynthDef(\bin, {|prime = 200, diff = 10, fade = 15, primetime = 20, difftime = 30, level= 0.4, gate = 1|
	var freqtransition = VarLag.kr(prime, primetime, 0, \lin);
	var links = SinOsc.ar(freqtransition);
	var rechts = SinOsc.ar(freqtransition - VarLag.kr(diff, difftime, 0, \lin));
	var env = EnvGen.kr(Env.asr(fade, level, fade), gate, doneAction:2);
	Out.ar(0, [links, rechts] * env);
}).add;
)