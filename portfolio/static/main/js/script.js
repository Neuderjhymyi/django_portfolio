document.addEventListener('DOMContentLoaded', function() {
  var menuToggle = document.querySelector('.menu-toggle');
  var menuList = document.querySelector('.menu-list');

  menuToggle.addEventListener('click', function() {
    menuToggle.classList.toggle('active');
    menuList.classList.toggle('show');
    menuList.style.display = menuList.style.display === 'block' ? 'none' : 'block';
  });
});

//  var menuToggle = document.querySelector('.menu-toggle');
//  var menuList = document.querySelector('.menu-list');
//
//  menuToggle.addEventListener('click', function() {
//    menuList.classList.toggle('show');
//  });