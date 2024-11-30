let totalItems = 0;

document.querySelectorAll('.increment').forEach(button => {
    button.addEventListener('click', () => {
        const input = button.previousElementSibling;
        const currentValue = parseInt(input.value)

        if (totalItems < 4) {
            input.value = currentValue + 1;
            totalItems++;
        } else {
            alert("You can only select up to 4 items.")
        }
        
    });
});

document.querySelectorAll('.decrement').forEach(button => {
    button.addEventListener('click', () => {
        const input = button.nextElementSibling;
        const currentValue = parseInt(input.value)

        if (currentValue > 0) {
            input.value = currentValue - 1;
            totalItems--;
        }
    });
});
