#!/usr/bin/node

if (process.argv[2] === undefined) {
	console.log('No argument');
}
if (process.argv[2] === 0) {
	console.log('Argument found');
}
else {
	console.log('Arguments found');
}
