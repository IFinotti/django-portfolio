const scrollReveal = ScrollReveal({
  origin: "top",
  distance: "30px",
  duration: 300, //ms
  reset: false,
  easing: "ease-in-out",
});

scrollReveal.reveal(
  `.grid, .text-content, .sections-title, .title, .img-art, 
.text-description, .title-project`,
  {
    interval: 100,
  },
);
