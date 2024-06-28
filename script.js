const form = document.querySelector('form');
const queryInput = document.querySelector('#query');
const responseDiv = document.querySelector('#response');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const query = queryInput.value.trim();
    if (query) {
        try {
            const response = await fetch('/query', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ query }),
            });
            const data = await response.json();
            responseDiv.innerText = data.answer;
        } catch (error) {
            console.error(error);
            responseDiv.innerText = 'Error: ' + error.message;
        }
    }
});