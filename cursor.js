var cursor = document.querySelector('.cursor');
var cursorinner = document.querySelector('.cursor2');
var links = document.querySelectorAll('a, button, .clickable');

document.addEventListener('mousemove', function(e){
  var x = e.clientX;
  var y = e.clientY;
  
  // Movimiento del anillo (con ligero lag para efecto fluido)
  cursor.style.transform = `translate3d(calc(${x}px - 50%), calc(${y}px - 50%), 0)`;
  
  // Movimiento del punto central
  cursorinner.style.left = x + 'px';
  cursorinner.style.top = y + 'px';
});

document.addEventListener('mousedown', function(){
  cursor.classList.add('cursor-click');
  cursorinner.classList.add('cursor-inner-hover');
});

document.addEventListener('mouseup', function(){
  cursor.classList.remove('cursor-click');
  cursorinner.classList.remove('cursor-inner-hover');
});

links.forEach(item => {
  item.addEventListener('mouseover', () => {
    cursor.classList.add('cursor-hover');
    cursorinner.classList.add('cursor-inner-hover');
  });
  item.addEventListener('mouseleave', () => {
    cursor.classList.remove('cursor-hover');
    cursorinner.classList.remove('cursor-inner-hover');
  });
});
