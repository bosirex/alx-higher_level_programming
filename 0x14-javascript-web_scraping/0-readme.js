#!/usr/bin/node

const file = require('file');

file.readFile(process.argv[2], 'utf8', function (error, data) {
  if (error) {
    console.log(error);
  } else {
    process.stdout.write(data);
  }
});
