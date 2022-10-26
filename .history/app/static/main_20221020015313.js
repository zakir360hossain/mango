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
//creating a timer
function startTimer(duration, display){
  var timer = duration, minutes, seconds;
  setInterval(function () {
    minutes = parseInt(timer/60, 10);
    seconds = parseInt(timer%60, 10);

    minutes = minutes < 10 ? "0" + minutes : minutes;
    seconds = seconds < 10 ? "0" + seconds : seconds;

    display.textContent = minutes + ":" + seconds;

// checks correct answer if the guess is made before time runs out --> will set
//timer to 0 once guess is made + colors the board
    $(".object").click((e) => {

      if (e.target.innerText === current.object) {
        $(e.target).addClass("correct");
        $(e.target).css({ pointerEvents: "none" });
      } else {
        $(e.target).addClass("pulse");
      }
      changeNoneCorrectCursor("none");
      timer = 0

    });
    //if time runs out, cycles to next clue.
    //code taken from previous next button clicked logic
    if(--timer < 0){
      timer = duration;
      // window.location.href= 'http://www.google.com';
      changeNoneCorrectCursor("none");
      current = pairs[Math.floor(Math.random() * (25 - 0 + 1)) + 0];
      placeNextClue(current.clue);
    }

  }, 1000);
}


window.onload = function() {
  var fourtyFiveSeconds = 45,
    display = document.querySelector('#time');
  startTimer(fourtyFiveSeconds, display);
};


fetch("http://127.0.0.1:5000/category/words")
  .then(function (response) {
    return response.json();
  })
  .then((response) => {
    pairs = [];
    current = null;
    Array.from(objects).forEach((field, index) => {
      l = response.objects.length;
      object_clue =
        response.objects[Math.floor(Math.random() * (l - 0 + 1)) + 0];
      pairs[index] = { object: object_clue.object, clue: object_clue.clue };
      field.innerText += object_clue.object;
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
          $(e.target).css({ pointerEvents: "none" });
        } else {
          $(e.target).addClass("pulse");
        }
        changeNoneCorrectCursor("none");

      });
    });
  });
