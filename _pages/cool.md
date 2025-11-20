---
layout: archive
title: "Welcome to the COOL Page!"
permalink: /cool/
author_profile: true
---

{% include base_path %}

<style>
/* 2000s Overembellished Website Theme */
body, html {
  background: url('{{ base_path }}/images/plink.gif') repeat !important;
  background-size: 150px 150px !important;
  background-attachment: fixed !important;
  font-family: "Comic Sans MS", cursive, fantasy !important;
  overflow-x: hidden !important;
  min-height: 100vh !important;
  cursor: url('{{ base_path }}/images/NyanCat.gif'), auto !important;
}

body {
  background: url('{{ base_path }}/images/plink.gif') repeat !important;
  background-size: 150px 150px !important;
  background-attachment: fixed !important;
  cursor: url('{{ base_path }}/images/NyanCat.gif'), auto !important;
}

@keyframes gradientShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

/* Rainbow text animation */
@keyframes rainbow {
  0% { color: #ff0000; }
  16.66% { color: #ff8000; }
  33.33% { color: #ffff00; }
  50% { color: #00ff00; }
  66.66% { color: #0080ff; }
  83.33% { color: #8000ff; }
  100% { color: #ff0000; }
}

/* Blink animation */
@keyframes blink {
  0%, 50% { opacity: 1; }
  51%, 100% { opacity: 0; }
}

/* Slide animation */
@keyframes slide {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(100vw); }
}

/* Sparkle animation */
@keyframes sparkle {
  0%, 100% { transform: scale(1) rotate(0deg); opacity: 1; }
  50% { transform: scale(1.5) rotate(180deg); opacity: 0.7; }
}

/* Container styling */
.cool-container {
  background: rgba(255, 255, 255, 0.9) !important;
  border: 5px solid #ff00ff !important;
  border-radius: 20px !important;
  box-shadow: 0 0 20px #00ffff, inset 0 0 20px rgba(255, 0, 255, 0.3) !important;
  margin: 20px !important;
  padding: 30px !important;
  position: relative !important;
  overflow: hidden !important;
}

.cool-container::before {
  content: "✨ WELCOME TO THE COOL ZONE ✨";
  position: absolute;
  top: -5px;
  left: 0;
  right: 0;
  background: linear-gradient(90deg, #ff0080, #8000ff, #0080ff);
  color: white;
  text-align: center;
  padding: 5px;
  font-weight: bold;
  animation: rainbow 2s linear infinite;
}

h1, h2, h3 {
  animation: rainbow 3s linear infinite !important;
  text-shadow: 2px 2px 4px #000000 !important;
  font-family: "Impact", "Arial Black", cursive !important;
  text-align: center !important;
}

.blink-text {
animation: blink 3s infinite !important;
    font-weight: bold !important;
    color: #ff0000 !important;
}

.slide-text {
    display: inline-block;
    animation: slide 10s linear infinite !important;
    font-weight: bold !important;
    color: #ff00ff !important;
    white-space: nowrap !important;
}

@keyframes slide {
    0% { transform: translateX(0%); }
    100% { transform: translateX(-100%); }
}

.sparkle {
    display: inline-block;
    animation: sparkle 5.5s ease-in-out infinite !important;
    color: #0000ff !important;
  text-shadow: 0 0 10px #ffff00 !important;
}

/* Fake GIF placeholder styling */
.fake-gif {
  width: 100px;
  height: 100px;
  background: linear-gradient(45deg, #ff0080, #8000ff);
  border: 3px solid #00ffff;
  border-radius: 10px;
  display: inline-block;
  margin: 10px;
  animation: sparkle 2s ease-in-out infinite;
  position: relative;
  overflow: hidden;
}

.fake-gif::after {
  content: "GIF";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  font-weight: bold;
  text-shadow: 2px 2px 4px #000;
}

/* Visitor counter styling */
.visitor-counter {
  background: #000000 !important;
  color: #00ff00 !important;
  padding: 10px !important;
  border: 2px solid #00ff00 !important;
  font-family: "Courier New", monospace !important;
  text-align: center !important;
  margin: 20px auto !important;
  width: fit-content !important;
}

/* Under construction styling */
.under-construction {
  background: repeating-linear-gradient(
    45deg,
    #ffff00,
    #ffff00 10px,
    #000000 10px,
    #000000 20px
  ) !important;
  color: #ff0000 !important;
  padding: 15px !important;
  text-align: center !important;
  font-weight: bold !important;
  /* animation: blink 0.5s infinite !important; */
  border: 3px solid #ff0000 !important;
  margin: 20px 0 !important;
}

/* Override sidebar for cool theme - match main container */
.sidebar {
  background: rgba(255, 255, 255, 0.9) !important;
  border-left: 5px solid #ff00ff !important;
  border-right: 5px solid #ff00ff !important;
  box-shadow: 0 0 20px #00ffff, inset 0 0 20px rgba(255, 0, 255, 0.3) !important;
  text-align: center !important;
  margin: 20px !important;
}

.author__avatar {
  text-align: center !important;
  margin: 20px auto !important;
}

.author__avatar img {
  border: 5px solid #ffff00 !important;
  box-shadow: 0 0 15px #ff0080 !important;
}

.author__content {
  text-align: center !important;
  padding: 10px !important;
}

.author__name {
  text-align: center !important;
}

.author__bio {
  text-align: center !important;
}

/* Show social links with cool theme styling */
.author__urls {
  display: block !important;
  text-align: center !important;
}

.author__urls-wrapper {
  display: block !important;
}

/* Scrolling text container */
.scroll-container {
  background: #000000;
  color: #00ff00;
  padding: 10px;
  margin: 20px 0;
  overflow: hidden;
  border: 2px solid #00ff00;
}

/* Web ring styling */
.web-ring {
  background: #000080 !important;
  color: #ffff00 !important;
  padding: 15px !important;
  text-align: center !important;
  border: 3px solid #ffff00 !important;
  margin: 20px 0 !important;
}

.web-ring a {
  color: #00ffff !important;
  text-decoration: underline !important;
  /* animation: blink 2s infinite !important; */
}

/* Cool links styling - exclude navigation */
.cool-container a, .web-ring a {
  color: #ff00ff !important;
  text-decoration: underline !important;
  animation: rainbow 4s linear infinite !important;
}

.cool-container a:hover, .web-ring a:hover {
  background: #ffff00 !important;
  color: #ff0000 !important;
  padding: 2px 4px !important;
  border-radius: 5px !important;
}

/* Hide footer on cool page */
.page__footer {
  display: none !important;
}

/* NyanCat cursor for all elements */
*, *:hover, *:focus, *:active {
  cursor: url('{{ base_path }}/images/NyanCat.gif'), auto !important;
}

/* Ensure NyanCat cursor on all interactive elements */
a, button, input, textarea, select, .btn, [role="button"], [onclick] {
  cursor: url('{{ base_path }}/images/NyanCat.gif'), auto !important;
}

a:hover, button:hover, input:hover, textarea:hover, select:hover, .btn:hover, [role="button"]:hover, [onclick]:hover {
  cursor: url('{{ base_path }}/images/NyanCat.gif'), auto !important;
}



/* Particle styles */
.particle {
  position: fixed;
  pointer-events: none;
  z-index: 9999;
  border-radius: 50%;
  animation: particleFloat 2s ease-out forwards;
}

@keyframes particleFloat {
  0% {
    transform: translate(0, 0) scale(1) rotate(0deg);
    opacity: 1;
  }
  100% {
    transform: translate(var(--random-x, 0), var(--random-y, 0)) scale(0) rotate(360deg);
    opacity: 0;
  }
}
</style>

<div class="cool-container">

🌟 CONGRATULATIONS YOU MADE IT TO THE COOL PAGE! 🌟

<div class="under-construction">
<span style="background-color: #ffff00; color: #ff0000; padding: 2px 5px;">🚧 ⚠️ UNDER CONSTRUCTION ⚠️ 🚧<br>
Best Viewed in Netscape Navigator 4.0+</span>
</div>

<div class="visitor-counter">
👁️ VISITOR COUNT: 1337 👁️<br>
You are visitor number <span class="blink-text">42</span>!
</div>

<div class="scroll-container" style="padding: 5px; margin: 15px 0;">
<div style="background: linear-gradient(180deg, #000000, #1a1a1a); border: 2px solid #00ff00; border-radius: 3px; padding: 5px 10px; box-shadow: 0 0 10px #00ff00;">
    <div style="display: flex; align-items: center; justify-content: space-between; gap: 10px;">
        <span style="color: #00ff00; font-family: 'Courier New', monospace; font-size: 11px; white-space: nowrap;">🎵 WINAMP:</span>
        <div style="flex: 1; overflow: hidden; background: #000; border: 1px inset #333; padding: 2px 5px;">
            <div class="slide-text" style="color: #00ffff; font-family: 'Courier New', monospace; font-size: 20px;">♫ Darude - Sandstorm ♫ *** [128 kbps MP3] *** Next: Eiffel 65 - Blue (Da Ba Dee) *** </div>
        </div>
        <span style="color: #888; font-family: 'Courier New', monospace; font-size: 10px; white-space: nowrap;">⏮️ ⏯️ ⏹️ ⏭️ ▓▓▓▓▓▓▓▓░░</span>
    </div>
</div>
</div>

📧 Get In Touch 📧 <br>

Want to collaborate on some <span class="sparkle">AWESOME</span> research? Send me an electronic mail message! But first, please sign my <span class="blink-text">GUESTBOOK</span>!

<div class="web-ring">
🌐 WEB RING 🌐<br>
← <a href="#">Previous Cool Site</a> | 
<a href="#">Random Cool Site</a> | 
<a href="#">Next Cool Site</a> →<br>
</div>



<script type="text/javascript">
// <![CDATA[
var colour="random"; // in addition to "random" can be set to any valid colour eg "#f0f" or "red"
var sparkles=50;

/****************************
*  Tinkerbell Magic Sparkle *
*(c)2005-13 mf2fm web-design*
*  http://www.mf2fm.com/rv  *
* DON'T EDIT BELOW THIS BOX *
****************************/
var x=ox=400;
var y=oy=300;
var swide=800;
var shigh=600;
var sleft=sdown=0;
var tiny=new Array();
var star=new Array();
var starv=new Array();
var starx=new Array();
var stary=new Array();
var tinyx=new Array();
var tinyy=new Array();
var tinyv=new Array();

window.onload=function() { if (document.getElementById) {
  var i, rats, rlef, rdow;
  for (var i=0; i<sparkles; i++) {
    var rats=createDiv(3, 3);
    rats.style.visibility="hidden";
    rats.style.zIndex="999";
    document.body.appendChild(tiny[i]=rats);
    starv[i]=0;
    tinyv[i]=0;
    var rats=createDiv(5, 5);
    rats.style.backgroundColor="transparent";
    rats.style.visibility="hidden";
    rats.style.zIndex="999";
    var rlef=createDiv(1, 5);
    var rdow=createDiv(5, 1);
    rats.appendChild(rlef);
    rats.appendChild(rdow);
    rlef.style.top="2px";
    rlef.style.left="0px";
    rdow.style.top="0px";
    rdow.style.left="2px";
    document.body.appendChild(star[i]=rats);
  }
  set_width();
  sparkle();
}}

function sparkle() {
  var c;
  if (Math.abs(x-ox)>1 || Math.abs(y-oy)>1) {
    ox=x;
    oy=y;
    for (c=0; c<sparkles; c++) if (!starv[c]) {
      star[c].style.left=(starx[c]=x)+"px";
      star[c].style.top=(stary[c]=y+1)+"px";
      star[c].style.clip="rect(0px, 5px, 5px, 0px)";
      star[c].childNodes[0].style.backgroundColor=star[c].childNodes[1].style.backgroundColor=(colour=="random")?newColour():colour;
      star[c].style.visibility="visible";
      starv[c]=50;
      break;
    }
  }
  for (c=0; c<sparkles; c++) {
    if (starv[c]) update_star(c);
    if (tinyv[c]) update_tiny(c);
  }
  setTimeout("sparkle()", 40);
}

function update_star(i) {
  if (--starv[i]==25) star[i].style.clip="rect(1px, 4px, 4px, 1px)";
  if (starv[i]) {
    stary[i]+=1+Math.random()*3;
    starx[i]+=(i%5-2)/5;
    if (stary[i]<shigh+sdown) {
      star[i].style.top=stary[i]+"px";
      star[i].style.left=starx[i]+"px";
    }
    else {
      star[i].style.visibility="hidden";
      starv[i]=0;
      return;
    }
  }
  else {
    tinyv[i]=50;
    tiny[i].style.top=(tinyy[i]=stary[i])+"px";
    tiny[i].style.left=(tinyx[i]=starx[i])+"px";
    tiny[i].style.width="2px";
    tiny[i].style.height="2px";
    tiny[i].style.backgroundColor=star[i].childNodes[0].style.backgroundColor;
    star[i].style.visibility="hidden";
    tiny[i].style.visibility="visible"
  }
}

function update_tiny(i) {
  if (--tinyv[i]==25) {
    tiny[i].style.width="1px";
    tiny[i].style.height="1px";
  }
  if (tinyv[i]) {
    tinyy[i]+=1+Math.random()*3;
    tinyx[i]+=(i%5-2)/5;
    if (tinyy[i]<shigh+sdown) {
      tiny[i].style.top=tinyy[i]+"px";
      tiny[i].style.left=tinyx[i]+"px";
    }
    else {
      tiny[i].style.visibility="hidden";
      tinyv[i]=0;
      return;
    }
  }
  else tiny[i].style.visibility="hidden";
}

document.onmousemove=mouse;
function mouse(e) {
  if (e) {
    y=e.pageY;
    x=e.pageX;
  }
  else {
    set_scroll();
    y=event.y+sdown;
    x=event.x+sleft;
  }
}

window.onscroll=set_scroll;
function set_scroll() {
  if (typeof(self.pageYOffset)=='number') {
    sdown=self.pageYOffset;
    sleft=self.pageXOffset;
  }
  else if (document.body && (document.body.scrollTop || document.body.scrollLeft)) {
    sdown=document.body.scrollTop;
    sleft=document.body.scrollLeft;
  }
  else if (document.documentElement && (document.documentElement.scrollTop || document.documentElement.scrollLeft)) {
    sleft=document.documentElement.scrollLeft;
    sdown=document.documentElement.scrollTop;
  }
  else {
    sdown=0;
    sleft=0;
  }
}

window.onresize=set_width;
function set_width() {
  var sw_min=999999;
  var sh_min=999999;
  if (document.documentElement && document.documentElement.clientWidth) {
    if (document.documentElement.clientWidth>0) sw_min=document.documentElement.clientWidth;
    if (document.documentElement.clientHeight>0) sh_min=document.documentElement.clientHeight;
  }
  if (typeof(self.innerWidth)=='number' && self.innerWidth) {
    if (self.innerWidth>0 && self.innerWidth<sw_min) sw_min=self.innerWidth;
    if (self.innerHeight>0 && self.innerHeight<sh_min) sh_min=self.innerHeight;
  }
  if (document.body.clientWidth) {
    if (document.body.clientWidth>0 && document.body.clientWidth<sw_min) sw_min=document.body.clientWidth;
    if (document.body.clientHeight>0 && document.body.clientHeight<sh_min) sh_min=document.body.clientHeight;
  }
  if (sw_min==999999 || sh_min==999999) {
    sw_min=800;
    sh_min=600;
  }
  swide=sw_min;
  shigh=sh_min;
}

function createDiv(height, width) {
  var div=document.createElement("div");
  div.style.position="absolute";
  div.style.height=height+"px";
  div.style.width=width+"px";
  div.style.overflow="hidden";
  return (div);
}

function newColour() {
  var c=new Array();
  c[0]=255;
  c[1]=Math.floor(Math.random()*256);
  c[2]=Math.floor(Math.random()*(256-c[1]/2));
  c.sort(function(){return (0.5 - Math.random());});
  return ("rgb("+c[0]+", "+c[1]+", "+c[2]+")");
}
// ]]>
</script>