#!usr/bin/node
let num = 0;
let process.argv[2] = parseInt(num,10);

if (process.argv[2] === undefined) {
	console.log('Not a number');
}
else
{
	console.log(process.argv[2]);
}
