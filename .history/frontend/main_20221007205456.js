const objects = document.getElementsByClassName("field");
const clue_container = document.getElementById("clue");
const next_clue = document.getElementById("next_clue");

function placeNextClue(def) {
  console.log(def);
  $(document).ready(() => {
    $("#clue").text(def);
  });
}

fetch("http://127.0.0.1:5000/category/words")
  .then(function (response) {
    return response.json();
  })
  .then((response) => {
    pairs = [];
    current = null;
    Array.from(objects).forEach((field, index) => {
        console.log(response.)
      l = response.objects.length;
      object_clue =
        response.objects[Math.floor(Math.random() * (l - 0 + 1)) + 0];
      pairs[index] = { object: object_clue.object, clue: object_clue.clue };
      field.innerText = object_clue.object;
    });
    current = pairs[0];
    clue_container.innerText = current.clue;

    $(document).ready(() => {
      $("#next_clue").click((e) => {
        console.log("clicked");
        current = pairs[Math.floor(Math.random() * (25 - 0 + 1)) + 0];
        placeNextClue(current.clue);
      });
    });

    $(document).ready(() => {
      $(".field").click((e) => {
        e.target.innerText == current.object
          ? $(e.target).addClass("correct")
          : $(e.target).addClass("incorrect");
      });
    });
  });
