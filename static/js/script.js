//@ts-check
import { runSignupStepper } from "./stepperForm.js";
import { validateInput } from "./formValidation.js";

// Run functions when the DOM loads
document.addEventListener("DOMContentLoaded", () => {
  handleDeleteButton();
  displayToasts();
  runSlider();

  if (window.location.href.indexOf("signup") > -1) {
    runSignupStepper();
  } else if (
    window.location.href.indexOf("project/create") > -1 ||
    (window.location.href.indexOf("project/") > -1 &&
      window.location.href.indexOf("edit") > -1) ||
    window.location.href.indexOf("job/create") > -1 ||
    (window.location.href.indexOf("job/") > -1 &&
      window.location.href.indexOf("edit") > -1)
  ) {
    handleCreateEditForm();
  } else if (
    (window.location.href.indexOf("user/") > -1 &&
      window.location.href.indexOf("edit") > -1) ||
    (window.location.href.indexOf("user/") > -1 &&
      window.location.href.indexOf("settings") > -1)
  ) {
    handleUserForm();
  }
});

/**
 * Function that displays the toast message on load
 * and then removes it after 3 seconds.
 * @returns {void}
 */
const displayToasts = () => {
  // Check if there are any toast messages
  if (!document.querySelector(".toast")) return;

  // Get all the toast messages
  const toasts = [...document.querySelectorAll(".toast")];

  // Loop through the toast messages and remove
  // them after 3 seconds
  for (const toast of toasts) {
    setTimeout(() => {
      toast.classList.add("opacity-0");
      setTimeout(() => toast.remove(), 300);
    }, 3000);
  }
};

/**
 * Check for delete profile button and add
 * event listener to display modal
 * @returns {void}
 */
const handleDeleteButton = () => {
  if (!document.querySelector(".delete-link")) return;
  const deleteButtons = document.querySelectorAll(".delete-link");
  const deleteModal = document.getElementById("delete-modal");
  const deleteConfirmButton = document.querySelector(".delete-confirm-button");
  const deleteCancelButton = document.querySelector(".delete-cancel-button");
  let currentDeleteForm = null;

  if (deleteButtons.length === 0 || !deleteModal) return;

  for (const deleteButton of deleteButtons) {
    deleteButton.addEventListener("click", (event) => {
      event.preventDefault();
      try {
        if (!(deleteButton.parentElement instanceof HTMLFormElement)) return;
        const formId = deleteButton.parentElement.getAttribute("id");
        if (formId) {
          currentDeleteForm = document.getElementById(formId);
        }

        // @ts-ignore
        deleteModal.showModal();
      } catch (error) {
        console.error(error);
      }
    });
  }

  if (deleteConfirmButton) {
    deleteConfirmButton.addEventListener("click", () => {
      if (currentDeleteForm instanceof HTMLFormElement) {
        currentDeleteForm.submit();
      }
    });
  }

  if (deleteCancelButton && deleteModal) {
    deleteCancelButton.addEventListener("click", (event) => {
      event.preventDefault();
      // @ts-ignore
      deleteModal.close();
    });
  }
};

/**
 * Hanlde creation and edit forms
 * @returns {void}
 */

const handleCreateEditForm = () => {
  const formInputs = [
    ...document.querySelectorAll(
      "input:not([type='checkbox']):not([type='radio']):not([type='file']):not([type='hidden']:not([name='tech_input']), textarea"
    ),
  ];
  const submitButton = document.querySelector("button[type='submit']");

  for (const input of formInputs) {
    input.addEventListener("input", () => {
      if (input instanceof HTMLInputElement) {
        input.dataset.touched = "true";
        if (input.name == "name") {
          validateInput({
            input,
            customMinLength: 3,
            customPattern: "^(?=.*[A-Za-z])[A-Za-z\\d\\s]{3,100}$",
            customValidationMessage:
              "Must be at least 3 characters long and can't contain symbols.",
          });
        } else {
          validateInput({ input });
        }
      }
      checkAllInputs();
    });
  }

  const checkAllInputs = () => {
    // @ts-ignore
    if (formInputs.every((input) => input.checkValidity())) {
      if (submitButton instanceof HTMLButtonElement) {
        submitButton.disabled = false;
        submitButton.ariaDisabled = "false";
        submitButton.classList.remove("opacity-50", "cursor-not-allowed");
      }
    } else {
      if (submitButton instanceof HTMLButtonElement) {
        submitButton.disabled = true;
        submitButton.ariaDisabled = "true";
        submitButton.classList.add("opacity-50", "cursor-not-allowed");
      }
    }
  };
  checkAllInputs();
};

/**
 * Run slider on the home page
 * Adapted from kindacode:
 * https://www.kindacode.com/article/tailwind-css-create-an-image-carousel-slideshow/
 * @returns {void}
 */

const runSlider = () => {
  let slideIndex = 1;
  const slides = document.querySelectorAll(".slide");
  const dots = document.querySelectorAll(".dot");

  const prevButton = document.querySelector(".carousel-prev");
  const nextButton = document.querySelector(".carousel-next");

  if (!prevButton || !nextButton) {
    return;
  } else {
    prevButton.addEventListener("click", () => moveSlide(-1));
    nextButton.addEventListener("click", () => moveSlide(1));
  }

  dots.forEach((dot, index) => {
    dot.parentElement.addEventListener("click", () => currentSlide(index + 1));
  });

  function moveSlide(moveStep) {
    showSlide((slideIndex += moveStep));
  }

  function currentSlide(index) {
    showSlide((slideIndex = index));
  }

  function showSlide(index) {
    if (index > slides.length) {
      slideIndex = 1;
    }
    if (index < 1) {
      slideIndex = slides.length;
    }

    slides.forEach((slide) => slide.classList.add("hidden"));
    dots.forEach((dot) => dot.classList.replace("bg-primary", "bg-secondary"));

    slides[slideIndex - 1].classList.remove("hidden");
    dots[slideIndex - 1].classList.replace("bg-secondary", "bg-primary");
  }

  // Initially show the first slide
  showSlide(slideIndex);
};

/**
 * Handle the user profile edit form
 * @returns {void}
 */
const handleUserForm = () => {
  const userFormInputs = [
    ...document.querySelectorAll(
      "input:not([type='checkbox']):not([type='radio']):not([type='file']):not([type='hidden'], textarea"
    ),
  ];
  const submitButton = document.querySelector("button[type='submit']");

  for (const input of userFormInputs) {
    input.addEventListener("input", () => {
      if (input instanceof HTMLInputElement) {
        input.dataset.touched = "true";
        if (input.name === "first_name" || input.name === "last_name") {
          validateInput({
            input,
            customMaxLength: 40,
            customRequired: true,
          });
        } else if (input.type === "tel") {
          validateInput({
            input,
            customValidationMessage:
              "Phone numbers can only be numbers and be between 10 and 15 characters long.",
          });
        } else if (input.name === "username") {
          validateInput({
            input,
            customMaxLength: 20,
            customValidationMessage:
              "Username must contain 5 characters and it can't contain symbols or spaces.",
          });
        }
        validateInput({ input });
      }
      checkAllInputs();
    });
  }

  const checkAllInputs = () => {
    // @ts-ignore
    if (userFormInputs.every((input) => input.checkValidity())) {
      if (submitButton instanceof HTMLButtonElement) {
        submitButton.disabled = false;
        submitButton.ariaDisabled = "false";
        submitButton.classList.remove("opacity-50", "cursor-not-allowed");
      }
    } else {
      if (submitButton instanceof HTMLButtonElement) {
        submitButton.disabled = true;
        submitButton.ariaDisabled = "true";
        submitButton.classList.add("opacity-50", "cursor-not-allowed");
      }
    }
  };
  checkAllInputs();
};
