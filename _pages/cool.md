---
layout: archive
title: "Welcome to My COOL Page!"
permalink: /cool/
author_profile: true
---

{% include base_path %}

<style>
/* 2000s Overembellished Website Theme */
body {
  background: linear-gradient(45deg, #ff00ff, #00ffff, #ffff00, #ff0080) !important;
  background-size: 400% 400% !important;
  animation: gradientShift 3s ease infinite !important;
  cursor: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAYAAAA71pVKAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAAdgAAAHYBTnsmCAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAFYSURBVCiRpZM9SwNBEIafgxBsLWwsrW0srK0srBQsLBQsLBQsLBQs'), auto !important;
  font-family: "Comic Sans MS", cursive, fantasy !important;
  overflow-x: hidden !important;
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
  animation: blink 1s infinite !important;
  font-weight: bold !important;
  color: #ff0000 !important;
}

.slide-text {
  display: inline-block;
  animation: slide 8s linear infinite !important;
  font-weight: bold !important;
  color: #ff00ff !important;
  white-space: nowrap !important;
}

.sparkle {
  display: inline-block;
  animation: sparkle 1.5s ease-in-out infinite !important;
  color: #ffff00 !important;
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
  animation: blink 0.5s infinite !important;
  border: 3px solid #ff0000 !important;
  margin: 20px 0 !important;
}

/* Override sidebar for cool theme */
.sidebar {
  background: rgba(255, 0, 255, 0.8) !important;
  border: 3px solid #00ffff !important;
  border-radius: 15px !important;
  box-shadow: 0 0 15px #ff00ff !important;
}

.author__avatar img {
  border: 5px solid #ffff00 !important;
  box-shadow: 0 0 15px #ff0080 !important;
  animation: sparkle 3s ease-in-out infinite !important;
}

/* Navigation styling */
.masthead {
  background: linear-gradient(90deg, #ff0080, #8000ff, #0080ff, #00ff80) !important;
  border-bottom: 5px solid #ffff00 !important;
}

.masthead__menu-item {
  color: #ffffff !important;
  text-shadow: 2px 2px 4px #000000 !important;
  font-weight: bold !important;
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
  animation: blink 2s infinite !important;
}

/* Cool links styling */
a {
  color: #ff00ff !important;
  text-decoration: underline !important;
  animation: rainbow 4s linear infinite !important;
}

a:hover {
  background: #ffff00 !important;
  color: #ff0000 !important;
  padding: 2px 4px !important;
  border-radius: 5px !important;
}
</style>

<div class="cool-container">

# 🌟 WELCOME TO MY TOTALLY RADICAL COOL PAGE! 🌟

<div class="under-construction">
🚧 ⚠️ UNDER CONSTRUCTION ⚠️ 🚧<br>
Best Viewed in Netscape Navigator 4.0+
</div>

<div class="visitor-counter">
👁️ VISITOR COUNT: 1337 👁️<br>
You are visitor number <span class="blink-text">42</span>!
</div>

<div class="scroll-container">
<div class="slide-text">*** Welcome to the most AWESOME page on the interwebs! ***</div>
</div>

## <span class="sparkle">✨</span> About This COOL Page <span class="sparkle">✨</span>

Hey there, <span class="blink-text">cyber-surfer</span>! Welcome to my totally <span class="sparkle">RADICAL</span> corner of the world wide web! This page is a tribute to the golden age of the internet when websites had <span class="blink-text">PERSONALITY</span> and weren't afraid to be <span class="rainbow-text">COLORFUL</span>!

<div class="fake-gif"></div>
<div class="fake-gif"></div>
<div class="fake-gif"></div>

### 🎮 Cool Features of This Page 🎮

- <span class="blink-text">Blinking text</span> because why not?!
- <span class="slide-text">Sliding text that goes WHOOOOSH!</span>
- Rainbow colors that change faster than a chameleon!
- Fake GIFs that sparkle like diamonds! <span class="sparkle">💎</span>
- A custom cursor (if your browser supports it)!
- Background that shifts like a lava lamp!

### 🌈 My Academic Work (But Make It Y2K) 🌈

Even though this page is totally <span class="blink-text">RADICAL</span>, I'm still a serious researcher! Check out my work in:

- <span class="sparkle">Neural Oscillations</span> (they oscillate like this text!)
- <span class="blink-text">Motion Perception</span> (everything's moving here!)
- <span class="sparkle">EEG Analysis</span> (brain waves as colorful as this page!)
- <span class="slide-text">Temporal Processing</span>

<div class="scroll-container">
<div class="slide-text">🧠 SCIENCE IS COOL! NEURONS ARE RADICAL! PSYCHOLOGY ROCKS! 🧠</div>
</div>

### 📧 Get In Touch (Web 1.0 Style) 📧

Want to collaborate on some <span class="sparkle">AWESOME</span> research? Send me an electronic mail message! But first, please sign my <span class="blink-text">GUESTBOOK</span>!

<div class="web-ring">
🌐 WEB RING 🌐<br>
← <a href="#">Previous Cool Site</a> | 
<a href="#">Random Cool Site</a> | 
<a href="#">Next Cool Site</a> →<br>
<small>Member of the Academic Researchers Who Love Y2K Aesthetics Ring</small>
</div>

### 🎵 Currently Playing 🎵
🎶 <span class="slide-text">Darude - Sandstorm (on repeat)</span> 🎶

---

<div class="scroll-container">
<div class="slide-text">*** Thanks for visiting! Don't forget to bookmark this page and tell all your friends! ***</div>
</div>

<center>
<span class="blink-text">Made with ❤️ and way too much caffeine</span><br>
<small>© 2000-something | Optimized for 800x600 resolution</small><br>
<span class="sparkle">✨ You've been visited by the Y2K fairy! ✨</span>
</center>

</div>

<script>
// Add some JavaScript for extra 2000s flair
document.addEventListener('DOMContentLoaded', function() {
    // Create floating sparkles
    function createSparkle() {
        const sparkle = document.createElement('div');
        sparkle.innerHTML = '✨';
        sparkle.style.position = 'fixed';
        sparkle.style.left = Math.random() * window.innerWidth + 'px';
        sparkle.style.top = '-20px';
        sparkle.style.fontSize = '20px';
        sparkle.style.pointerEvents = 'none';
        sparkle.style.zIndex = '9999';
        sparkle.style.animation = 'sparkle 3s ease-out forwards';
        
        document.body.appendChild(sparkle);
        
        setTimeout(() => {
            sparkle.remove();
        }, 3000);
    }
    
    // Create sparkles every 2 seconds
    setInterval(createSparkle, 2000);
    
    // Add CSS for sparkle animation
    const style = document.createElement('style');
    style.textContent = `
        @keyframes sparkle {
            to {
                transform: translateY(${window.innerHeight + 50}px) rotate(360deg);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);
});
</script>