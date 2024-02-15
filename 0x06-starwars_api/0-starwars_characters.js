#!/usr/bin/node

const request = require('request'); //import request module
const movieId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieId}/`; //api url

request(apiUrl, (err, response, body) => {
  if (error) {
    console.error('Error:', err);
  } else {
    const film = JSON.parse(body);
    const characters = film.characters;
    const printNamChar = (index) => {
      if (index >= characters.length) {
        return;
      }

      const characterUrl = characters[index];
      request(characterUrl, (err, response, body) => {
        if (err) {
          console.error('Error:', err);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
          printNamChar(index + 1);
        }
      });
    };
    printNamChar(0);
  }
});
