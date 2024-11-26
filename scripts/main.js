// Contact form submission
document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    form.addEventListener("submit", (e) => {
        e.preventDefault(); // Prevent form from refreshing the page
        alert("Thank you for your submission!");
        form.reset();
    });
});
