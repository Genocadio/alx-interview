#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieId}/`; // Updated API URL

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const film = JSON.parse(body);
    const characters = film.characters;

    const printCharacterNames = (index) => {
      if (index >= characters.length) {
        return;
      }

      const characterUrl = characters[index];
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Error:', error);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
          printCharacterNames(index + 1);
        }
      });
    };

    printCharacterNames(0);
  }
});
