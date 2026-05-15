function RunSentimentAnalysis() {
  const textToAnalyze = document.getElementById("textToAnalyze").value;
  const resultElement = document.getElementById("system_response");

  const request = new XMLHttpRequest();
  request.onreadystatechange = function () {
    if (request.readyState === 4) {
      resultElement.innerHTML = request.responseText;
    }
  };

  request.open(
    "GET",
    `/emotionDetector?textToAnalyze=${encodeURIComponent(textToAnalyze)}`,
    true
  );
  request.send();
}
