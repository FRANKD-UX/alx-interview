#!/usr/bin/node

const request = require('request');

// Get the movie ID from command line arguments
const movieId = process.argv[2];

// Check if movie ID is provided
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Star Wars API base URL
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Function to make HTTP request and return a promise
function makeRequest(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`HTTP ${response.statusCode}: ${response.statusMessage}`));
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

// Function to fetch character name from character URL
async function getCharacterName(characterUrl) {
  try {
    const character = await makeRequest(characterUrl);
    return character.name;
  } catch (error) {
    console.error(`Error fetching character: ${error.message}`);
    return null;
  }
}

// Main function to fetch and display characters
async function displayCharacters() {
  try {
    // Fetch movie data
    const movie = await makeRequest(apiUrl);
    
    // Get character URLs from the movie data
    const characterUrls = movie.characters;
    
    // Fetch all character names in order
    for (const characterUrl of characterUrls) {
      const characterName = await getCharacterName(characterUrl);
      if (characterName) {
        console.log(characterName);
      }
    }
  } catch (error) {
    console.error(`Error: ${error.message}`);
    process.exit(1);
  }
}

// Execute the main function
displayCharacters();
