(function () {
  var correctPassword = "curvesAndTheLine131"; // Change this
  var timeoutMinutes = 15; // Change this to the desired timeout duration
  var currentTime = new Date().getTime();
  var storedPassword = sessionStorage.getItem("auth_pass");
  var storedTime = sessionStorage.getItem("auth_time");

  function askForPassword() {
    var userInput = prompt("Enter the password:", ""); // Prompts user
    if (userInput === correctPassword) {
      sessionStorage.setItem("auth_pass", userInput);
      sessionStorage.setItem("auth_time", new Date().getTime()); // Save timestamp
    } else {
      document.body.innerHTML = "<h2>Access Denied</h2>";
    }
  }

  // Check if password is correct AND if the session hasn't expired
  if (
    storedPassword !== correctPassword ||
    !storedTime ||
    currentTime - storedTime > timeoutMinutes * 60 * 1000
  ) {
    askForPassword();
  } else {
    sessionStorage.setItem("auth_time", currentTime); // Reset timeout on activity
  }
})();
