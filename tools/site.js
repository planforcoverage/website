(function(){
  var t=document.querySelector('.nav-toggle'),n=document.getElementById('nav');
  if(!t||!n)return;
  t.addEventListener('click',function(){
    var open=n.classList.toggle('open');
    t.setAttribute('aria-expanded',open?'true':'false');
    t.textContent=open?'Close':'Menu';
  });
})();
