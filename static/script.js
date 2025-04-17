function submitGuess() {
    const guess = document.getElementById("guessInput").value;

    fetch('/guess', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'guess=' + guess
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("resultMessage").textContent = data.message;
        if (data.correct) {
            setTimeout(() => {
                window.location.reload();
            }, 2500);
        }
    });
}
