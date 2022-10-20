const objects = document.getElementsByClassName("object");
const clue_container = document.getElementById("clue");
const next_clue = document.getElementById("next_clue");

$(document).ready(function () {
  const socket = io.connect("http://127.0.0.1:5000", {
    cors: {
      origin: "*",
      methods: ["GET", "POST"],
      // transports: ["websocket", "polling"],
    },
  });
  $("#next_clue").click((e) => {
    console.log("clicked");
    socket.emit("next", {
      // who: $(this).attr("id"),
      // data: $(this).val(),
      msg: "the next clue button has been clicked, send another clue!",
    });
  });
  // Listening for event named `after connect`
  socket.on("after connect", function (msg) {
    console.log("After connect", msg);
  });
  socket.on("update", function (msg) {
    alert(msg);
  });
});

function changeCursor(state) {
  $(document).ready(() => {
    $(".object").css({ cursor: state });
  });
}

function placeNextClue(clue) {
  $(document).ready(() => {
    $("#clue").text(clue);
  });
  changeCursor("pointer");
}

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
      field.innerText = object_clue.object;
    });
    current = pairs[0];
    clue_container.innerText = current.clue;

    $(document).ready(() => {
      // checkWinning()
      $("#next_clue").click((e) => {
        current = pairs[Math.floor(Math.random() * (25 - 0 + 1)) + 0];
        placeNextClue(current.clue);
      });
    });

    $(document).ready(() => {
      $(".object").click((e) => {
        e.target.innerText == current.object
          ? $(e.target).addClass("correct")
          : $(e.target).addClass("incorrect");
        changeCursor("not-allowed");
      });
    });
  });