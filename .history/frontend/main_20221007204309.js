const objects = document.getElementsByClassName("field");
const clue = document.getElementById("clue");
const next_clue = document.getElementById("next_clue");

function placeNextClue(def) {
  console.log(def);
  $(document).ready(() => {
    $("#clue").text(def);
  });
}

fetch("http://127.0.0.1:5000/subject/words")
  .then(function (response) {
    return response.json();
  })
  .then((response) => {
    pairs = [];
    current = null;
    Array.from(objects).forEach((field, index) => {
      l = response.objects;
      word_def = response.topics[Math.floor(Math.random() * (l - 0 + 1)) + 0];
      pairs[index] = { word: word_def.word, def: word_def.definition };
      field.innerText = word_def.word;
    });
    current = pairs[0];
    clue.innerText = current.def;

    $(document).ready(() => {
      $("#next_clue").click((e) => {
        console.log("clicked");
        current = pairs[Math.floor(Math.random() * (25 - 0 + 1)) + 0];
        placeNextClue(current.def);
      });
    });

    $(document).ready(() => {
      $(".field").click((e) => {
        e.target.innerText == current.word
          ? $(e.target).addClass("correct")
          : $(e.target).addClass("incorrect");
      });
    });
  });
