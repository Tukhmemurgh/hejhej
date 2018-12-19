var canvas = document.querySelector('canvas');
var c = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
console.log(window.innerWidth + ":" + window.innerHeight);
function mandelbrot(x, y, a, b){
  var Re = x;
  var Im = y;
  var n = 0;
  var Re_temp;
  var Im_temp;
  while(n <= 100 && (Re*Re + Im*Im < 4)){
    Re_temp = Re*Re - Im*Im + a;
    Im = 2*Re*Im + b;
    Re = Re_temp;
    n++
  }
  return n;
}

function outsidepixel(x, y, n){
  if(n >= 100){
    n = 0
  }
  var color = 'rgb('+ Math.floor(255*n/100) +', ' + Math.floor(100*n/100) + ', 0)';
  c.beginPath();
  c.rect(x, y, 1, 1);
  c.rect(x, window.innerHeight-y, 1, 1);
  c.fillStyle = color;
  c.fill();
  c.closePath();
}

for(var x = 0; x <= window.innerWidth; x+=1){
  for(var y = 0; y <= window.innerHeight/2; y+=1){
    //console.log(mandelbrot(0, 0, 3*x/window.innerWidth-2, 2*y/window.innerHeight-1));
    outsidepixel(x, y, mandelbrot(0, 0, 3*x/window.innerWidth-2, 2*y/window.innerHeight-1));
  }
}
