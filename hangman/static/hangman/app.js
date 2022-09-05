
document.addEventListener('DOMContentLoaded', () => {
  let triesCounter = 0
  let isSolved = false;
  let gmDuration = 0;
  var intervalID;

  function startTimer(duration, display) {
    var timer = duration, minutes, seconds;
    console.log(timer);
    intervalID = setInterval(function () {
      minutes = parseInt(timer / 60, 10);
      seconds = parseInt(timer % 60, 10);

      minutes = minutes < 10 ? "0" + minutes : minutes;
      seconds = seconds < 10 ? "0" + seconds : seconds;

      display.textContent = minutes + ":" + seconds;

      if (--timer < 0) {
        gmDuration = timer;
        stopTimer(timer);
        gameEnd();

      }
    }, 1000);
  }

  function stopTimer(timer) {
    clearInterval(intervalID);
    console.log("stop timer", timer);
  }

  window.onload = function () {
    var twoMinutes = 10//60 * 2,
      display = document.querySelector('#time');
    startTimer(twoMinutes, display);
  };

  document.addEventListener('keypress', logKey);

    function logKey(e) {
      var still = 0;
      triesCounter++;
      document.querySelectorAll('.letter').forEach(letter => {
        if (e.key.toUpperCase() === letter.innerHTML) {
          letter.style.color = 'red';
          document.querySelectorAll('.gmLetter').forEach(gl => {
            if (e.key.toUpperCase() === gl.innerHTML.toUpperCase()) {
              gl.style.color = 'red';
            }
            if (gl.style.color != 'red') {
              still++;
            }
          })
        }
      });
      if (still === 0) {
        alert('solved!');
        isSolved = true;
      }
      if (triesCounter >= r.length) {
        alert('Game Over!!');
      }
    }

    document.querySelectorAll('.gmLetter').forEach(l => {
      l.style.color = 'lightblue';
    });


  function gameEnd() { 
    const url = "savegame/";
    const data = {
      "player_name": playerName,
      "game_duration": gmDuration,
      "tries_counter": triesCounter,
      "is_solved": isSolved
    }
    fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    })
      .then(response => response.text())
      .then(text => {
        console.log(text);
        document.querySelector('#content').innerHTML = text;
      });
  }
});