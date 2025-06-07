const uploadForm = document.getElementById('uploadForm');
const logArea = document.getElementById('logArea');
const submitBtn = document.getElementById('submitBtn');
const submitText = document.getElementById('submitText');
const submitSpinner = document.getElementById('submitSpinner');

uploadForm.addEventListener('submit', function (event) {
  event.preventDefault();

  logArea.value = '';
  submitText.textContent = 'Loading...';
  submitSpinner.style.display = 'inline-block';
  submitBtn.disabled = true;

  const youtubeLink = document.getElementById('youtubeLink').value;
  const language = document.getElementById('language').value;
  const additionalInfo = document.getElementById('additionalInfo').value;

  const data = {
    link: youtubeLink,
    language: language,
    additional_infos: additionalInfo
  };

  fetch('http://127.0.0.1:5002/api', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    },
    body: JSON.stringify(data)
  })
    .then(response => response.json())
    .then(data => {
      logArea.value = data.summary || 'No summary received.';
      submitText.textContent = 'Submit';
      submitSpinner.style.display = 'none';
      submitBtn.disabled = false;
    })
    .catch(error => {
      console.error('Error fetching data:', error);
      logArea.value = 'Error fetching data.';
      submitText.textContent = 'Submit';
      submitSpinner.style.display = 'none';
      submitBtn.disabled = false;
    });
});
