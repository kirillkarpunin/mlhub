const datasetDataField = document.getElementById('dataset-data-field');
const datasetFieldError = document.getElementById('dataset-field-error');

const datasetDataInput = document.getElementById('dataset-data-input');
datasetDataInput.addEventListener('input', () => {
    datasetDataField.classList.remove('error');
    datasetFieldError.style.display = 'none';
});

const datasetForm = document.getElementById('dataset-form');
datasetForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const formData = new FormData(datasetForm);
    const data = Object.fromEntries(formData.entries());

    const type = data['dataset-type'];

    let isValid = false
    switch (type) {
        case 'csv':
            isValid = csvValidation(data['dataset-data'])
            break;
    }

    if (!isValid) {
        datasetDataField.classList.add('error');
        datasetFieldError.style.display = 'inline-block';
        return
    }

    fetch('#', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(response => window.location.href = response.headers.get('redirect'));
});

function csvValidation(text) {
    const lines = text.split('\n');

    if (lines.length < 2) {
        return false;
    }

    const columnCount = lines[0].split(',').length;

    // Проверяем каждую строку
    for (let i = 0; i < lines.length; i++) {
        const line = lines[i];

        if (line.trim() === '') {
            return false;
        }

        const fields = line.split(',');

        if (fields.length !== columnCount) {
            return false;
        }
    }

    return true;
}