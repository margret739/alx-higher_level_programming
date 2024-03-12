#!/usr/bin/node
let num = 89;
let process = parseInt(num,10);

if (process.argv === undefined) {
	console.log('My number: ' + process);
}
else {
	console.log(process.argv);
}
