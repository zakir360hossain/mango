const objects = document.getElementsByClassName("object");
const clue_container = document.getElementById("clue");
const next_clue = document.getElementById("next_clue");

function changeNoneCorrectCursor(state) {
  $(document).ready(() => {
    Array.from(objects).forEach((element) => {
      if (!$(element).hasClass("correct")) {
        $(element).css({ "pointer-events": state });
      }
    });
  });
}

function placeNextClue(clue) {
  console.log(clue);
  $(document).ready(() => {
    $("#clue").text(clue);
  });
  changeNoneCorrectCursor("auto");
}

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
      $(e.target).css({ pointerEvents: "none" });
    } else {
      $(e.target).addClass("pulse");
    }
    changeNoneCorrectCursor("none");
  });
});
