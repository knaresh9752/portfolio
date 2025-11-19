const display = document.getElementById("display");

    function addToDisplay(value) {
      display.value += value;
    }

    function clearScreen() {
      display.value = "";
    }

    function calculate() {
      try {
        display.value = eval(display.value);
      } catch (error) {
        display.value = "Error";
      }
    }