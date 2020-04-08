// #!/usr/local/bin/sclang

s.boot;

"hello world!".postln;
(
t = Task({
    loop {
    	().play;
    	"waiting...".postln;
        2.wait;
    }
}).play;
)