function submitForm(event) {
    event.preventDefault();
    var input = document.getElementById('input').value.replace(/[^a-z0-9]/gi, '').replace(/\s/g, '').toUpperCase();
    fetch(`https://12v.github.io/boundary-mapper/postcodes/${input}.txt`)
        .then(response => {
            if (!response.ok) {
                throw new Error(response.status);
            }

            return response.text()
        })
        .then(data => {
            document.getElementById('result').innerHTML = 'Following the 2023 boundary review, your constituency is:<br><br><span class="result-text"> ' + data + '</span>';
        })
        .catch(error => {
            if (error.message == '404') {
                document.getElementById('result').textContent = 'Your postcode was not found, please check your postcode and try again.';
            } else {
                document.getElementById('result').textContent = 'An error occurred: ' + error.message;
            }
        });
}