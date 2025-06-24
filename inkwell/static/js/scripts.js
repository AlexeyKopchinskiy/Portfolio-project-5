document.addEventListener("DOMContentLoaded", function () {
    const toggleGroup = document.getElementById("billing-toggle");
    if (!toggleGroup) return; // gracefully exit if not found

    const buttons = toggleGroup.querySelectorAll("button");
    const prices = document.querySelectorAll(".price");

    buttons.forEach(button => {
        button.addEventListener("click", () => {
            // Toggle active class
            buttons.forEach(btn => btn.classList.remove("active"));
            button.classList.add("active");

            // Switch prices
            const billing = button.dataset.billing; // 'monthly' or 'yearly'
            prices.forEach(span => {
                span.textContent = span.dataset[billing];
            });

            // Update /month label
            const label = billing === "monthly" ? "/month" : "/year";
            document.querySelectorAll(".fs-6.text-muted").forEach(el => {
                el.textContent = label;
            });
        });
    });
});