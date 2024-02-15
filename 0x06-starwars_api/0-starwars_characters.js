#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (err, response, body) => {
  if (err) {
    throw err;
  } else {
    const film = JSON.parse(body);
    const characters = film.characters;
    const printNames = (index) => {
      if (index >= characters.length) {
        return;
      }

      const characterUrl = characters[index];
      request(characterUrl, (err, response, body) => {
        if (err) {
          throw err;
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
          printNames(index + 1);
        }
      });
    };
    printNames(0);
  }
});
