// Simple log to confirm it's working
console.log("☕ Coffee House: Interface loaded successfully!");

// You can add a "Added to cart" toast or alert later
document.addEventListener('DOMContentLoaded', function() {
    const orderButtons = document.querySelectorAll('.btn-coffee');
    orderButtons.forEach(button => {
        button.addEventListener('click', function() {
            const productName = this.closest('.card-body').querySelector('.card-title').innerText;
            alert(`Coming soon: ${productName} added to your order!`);
        });
    });
});
