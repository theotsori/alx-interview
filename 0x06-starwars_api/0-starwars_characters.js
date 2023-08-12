#!/usr/bin/env node

const request = require('request');

function getMovieCharacters(movieId) {
  return new Promise((resolve, reject) => {
    const url = `https://swapi.dev/api/films/${movieId}/`;
    
    request(url, (error, response, body) => {
      if (error) {
        reject(`Error fetching data: ${error}`);
      } else {
        const filmData = JSON.parse(body);
        const characterUrls = filmData.characters;
        const characterNames = [];

        const fetchCharacter = (url) => {
          request(url, (charError, charResponse, charBody) => {
            if (charError) {
              reject(`Error fetching character data: ${charError}`);
            } else {
              const characterData = JSON.parse(charBody);
              characterNames.push(characterData.name);

              if (characterNames.length === characterUrls.length) {
                resolve(characterNames);
              } else if (characterNames.length < characterUrls.length) {
                fetchCharacter(characterUrls[characterNames.length]);
              }
            }
          });
        };

        if (characterUrls.length > 0) {
          fetchCharacter(characterUrls[0]);
        } else {
          resolve(characterNames);
        }
      }
    });
  });
}

async function main() {
  if (process.argv.length !== 3) {
    console.log('Usage: node 0-starwars_characters.js <Movie ID>');
    process.exit(1);
  }

  const movieId = process.argv[2];

  try {
    const characterNames = await getMovieCharacters(movieId);

    for (const name of characterNames) {
      console.log(name);
    }
  } catch (error) {
    console.log(`Error: ${error}`);
  }
}

main();
