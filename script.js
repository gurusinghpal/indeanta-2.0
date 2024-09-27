document.getElementById('inputForm').addEventListener('submit', function(e) {
    // Prevent the default form submission
    e.preventDefault();

    // Get user input values
    const amount = document.getElementById('amount').value;
    const quantity = document.getElementById('quantity').value;
    const dateTime = document.getElementById('dateTime').value;

    // Convert dateTime to more readable format (optional)
    const readableDate = new Date(dateTime).toLocaleString();

    // Prepare and display the result
    const resultHTML = `
        <p><strong>Amount:</strong> ${amount}</p>
        <p><strong>Quantity:</strong> ${quantity}</p>
        <p><strong>Date and Time:</strong> ${readableDate}</p>
    `;

    document.getElementById('result').innerHTML = resultHTML;
});
