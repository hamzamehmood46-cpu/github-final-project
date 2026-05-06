const form = document.getElementById("interest-form");
const interestOutput = document.getElementById("interest-output");
const totalOutput = document.getElementById("total-output");
const resetButton = document.getElementById("reset-btn");

form.addEventListener("submit", function (event) {
  event.preventDefault();

  const principal = Number(document.getElementById("principal").value);
  const rate = Number(document.getElementById("rate").value);
  const time = Number(document.getElementById("time").value);

  if (principal <= 0 || rate <= 0 || time <= 0) {
    interestOutput.textContent = "Simple Interest: Please enter valid positive numbers.";
    totalOutput.textContent = "Total Amount: --";
    return;
  }

  const simpleInterest = (principal * rate * time) / 100;
  const totalAmount = principal + simpleInterest;

  interestOutput.textContent = `Simple Interest: ${simpleInterest.toFixed(2)}`;
  totalOutput.textContent = `Total Amount: ${totalAmount.toFixed(2)}`;
});

resetButton.addEventListener("click", function () {
  interestOutput.textContent = "Simple Interest: 0.00";
  totalOutput.textContent = "Total Amount: 0.00";
});
