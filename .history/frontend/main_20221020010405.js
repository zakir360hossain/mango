const objects = document.getElementsByClassName("object");
const clue_container = document.getElementById("clue");
const next_clue = document.getElementById("next_clue");

function changeNoneCorrectCursor(state) {
  $(document).ready(() => {
    Array.from(objects).forEach((element) => {
      if (!$(element).hasClass("correct")) {
        $(element).css({ cursor: state });
      }
    });
  });
}

function placeNextClue(clue) {
  console.log(clue);
  $(document).ready(() => {
    $("#clue").text(clue);
  });
  changeNoneCorrectCursor("pointer");
}

fetch("http://127.0.0.1:5000/category/words")
  .then(function (response) {
    return response.json();
  })
  .then((response) => {
    pairs = [];
    current = null;
    Array.from(objects).forEach((field, index) => {
      console.log(response.objects);
      l = response.objects.length;
      object_clue =
        response.objects[Math.floor(Math.random() * (l - 0 + 1)) + 0];
      pairs[index] = { object: object_clue.object, clue: object_clue.clue };
      field.innerText = object_clue.object;
    });
    current = pairs[0];
    clue_container.innerText = current.clue;

    $(document).ready(() => {
      // checkWinning()
      $("#next_clue").click((e) => {
        console.log("clicked");
        current = pairs[Math.floor(Math.random() * (25 - 0 + 1)) + 0];
        placeNextClue(current.clue);
      });
    });

    $(document).ready(() => {
      $(".object").click((e) => {
        if (e.target.innerText === current.object) {
          $(e.target).addClass("correct");
          $(e.target).css({ cursor: "not-allowed" });
        } else {
          const animTime = 1000;
          $(e.target)
            .addClass("pulse", animTime)
            .removeClass("pulse", animTime);
        }
        changeNoneCorrectCursor("not-allowed");
      });
    });
  });
