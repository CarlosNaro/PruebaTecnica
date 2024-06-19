setTimeout(function () {
    const elements = document.querySelectorAll('#error-message');
    elements.forEach(element => {
        element.remove();
    });

}, 3000);
