"use strict";

document.addEventListener("DOMContentLoaded", () => {
    const slideshows = document.querySelectorAll("[data-slideshow]");

    slideshows.forEach((slideshow) => {
        const slides = Array.from(
            slideshow.querySelectorAll("[data-slide]")
        );

        const previousButton = slideshow.querySelector(
            "[data-previous-slide]"
        );

        const nextButton = slideshow.querySelector(
            "[data-next-slide]"
        );

        const toggleButton = slideshow.querySelector(
            "[data-toggle-slideshow]"
        );

        const counter = slideshow.querySelector(
            "[data-current-slide]"
        );

        if (
            slides.length === 0 ||
            !previousButton ||
            !nextButton ||
            !toggleButton
        ) {
            return;
        }

        let currentIndex = 0;
        let intervalId = null;

        const showSlide = (newIndex) => {
            currentIndex = (
                newIndex + slides.length
            ) % slides.length;

            slides.forEach((slide, index) => {
                const isActive = index === currentIndex;

                slide.classList.toggle("is-active", isActive);
                slide.setAttribute(
                    "aria-hidden",
                    String(!isActive)
                );
            });

            if (counter) {
                counter.textContent = String(currentIndex + 1);
            }
        };

        const nextSlide = () => {
            showSlide(currentIndex + 1);
        };

        const previousSlide = () => {
            showSlide(currentIndex - 1);
        };

        const stopSlideshow = () => {
            if (intervalId !== null) {
                window.clearInterval(intervalId);
                intervalId = null;
            }

            toggleButton.textContent = "Diashow starten";
            toggleButton.setAttribute("aria-pressed", "false");
        };

        const startSlideshow = () => {
            stopSlideshow();

            intervalId = window.setInterval(
                nextSlide,
                5000
            );

            toggleButton.textContent = "Diashow anhalten";
            toggleButton.setAttribute("aria-pressed", "true");
        };

        previousButton.addEventListener("click", () => {
            previousSlide();

            if (intervalId !== null) {
                startSlideshow();
            }
        });

        nextButton.addEventListener("click", () => {
            nextSlide();

            if (intervalId !== null) {
                startSlideshow();
            }
        });

        toggleButton.addEventListener("click", () => {
            if (intervalId === null) {
                startSlideshow();
            } else {
                stopSlideshow();
            }
        });

        document.addEventListener(
            "visibilitychange",
            () => {
                if (document.hidden && intervalId !== null) {
                    stopSlideshow();
                }
            }
        );

        showSlide(0);
    });
});
