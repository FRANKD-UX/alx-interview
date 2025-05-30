#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID');
  process.exit(1);
}

function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err || res.statusCode !== 200) {
        reject(err || new Error(`Status: ${res.statusCode}`));
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

async function main () {
  try {
    const film = await makeRequest(`https://swapi-api.alx-tools.com/api/films/${movieId}/`);

    for (const url of film.characters) {
      const character = await makeRequest(url);
      console.log(character.name);
    }
  } catch (error) {
    console.error('Error:', error.message);
    process.exit(1);
  }
}

main();
