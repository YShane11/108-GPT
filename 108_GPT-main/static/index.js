const sideLinks = document.querySelectorAll('.sidebar .side-menu li a:not(.logout)');

sideLinks.forEach(item => {
    const li = item.parentElement;
    item.addEventListener('click', () => {
        sideLinks.forEach(i => {
            i.parentElement.classList.remove('active');
        })
        li.classList.add('active');
    })
});

const menuBar = document.querySelector('.content nav .bx.bx-menu');
const sideBar = document.querySelector('.sidebar');

menuBar.addEventListener('click', () => {
    sideBar.classList.toggle('close');
});

const searchBtn = document.querySelector('.content nav form .form-input button');
const searchBtnIcon = document.querySelector('.content nav form .form-input button .bx');
const searchForm = document.querySelector('.content nav form');



window.addEventListener('resize', () => {
    if (window.innerWidth < 768) {
        sideBar.classList.add('close');
    } else {
        sideBar.classList.remove('close');
    }
    if (window.innerWidth > 576) {
        searchBtnIcon.classList.replace('bx-x', 'bx-search');
        searchForm.classList.remove('show');
    }
});



const themeToggle = document.getElementById("theme-toggle");

themeToggle.addEventListener("change", function() {
// ?取复?框的?前??（?中或未?中）
const theme = themeToggle.checked ? "dark" : "light";

fetch('/update_theme', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({ theme: theme }),
});
});

const toggler = document.getElementById('theme-toggle');

toggler.addEventListener('change', function () {
    if (this.checked) {
        document.body.classList.add('dark');
    } else {
        document.body.classList.remove('dark');
    }
});

document.addEventListener("DOMContentLoaded", function() {
    const themeParagraph = document.getElementById("theme_set1");
    if (themeParagraph) {
      const themeValue = themeParagraph.textContent;
      if (themeValue==='dark') {
        document.body.classList.add('dark');
        const themeToggle = document.getElementById("theme-toggle");

        const currentChecked = themeToggle.checked;

        themeToggle.checked = !currentChecked;

    } else {
        document.body.classList.remove('dark');
    }
    }
  });
