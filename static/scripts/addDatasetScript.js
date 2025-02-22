const datasetForm = document.getElementById('dataset-form');
datasetForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const formData = new FormData(datasetForm);
    const data = Object.fromEntries(formData.entries());

    fetch('#', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(response => window.location.href = response.headers.get('redirect'))
});