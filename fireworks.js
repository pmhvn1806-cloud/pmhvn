// fireworks.js - một implementation đơn giản
(function(){
  const canvas = document.getElementById('fireworks-canvas');
  const ctx = canvas.getContext('2d');
  let W = canvas.width = innerWidth;
  let H = canvas.height = innerHeight;
  window.addEventListener('resize', ()=> {
    W = canvas.width = innerWidth;
    H = canvas.height = innerHeight;
  });

  // particle helpers
  function rand(min,max){ return Math.random()*(max-min)+min }
  class Particle {
    constructor(x,y, color, speed, angle, life, size){
      this.x=x; this.y=y; this.vx=Math.cos(angle)*speed; this.vy=Math.sin(angle)*speed;
      this.life=life; this.alpha=1; this.size=size; this.color=color;
    }
    update(dt){
      this.vy += 0.02; // gravity
      this.x += this.vx*dt;
      this.y += this.vy*dt;
      this.life -= dt*0.02;
      this.alpha = Math.max(0, this.life);
    }
    draw(ctx){
      ctx.globalAlpha = Math.max(0, this.alpha);
      ctx.beginPath();
      ctx.fillStyle = this.color;
      ctx.arc(this.x, this.y, Math.max(0.5, this.size), 0, Math.PI*2);
      ctx.fill();
      ctx.globalAlpha = 1;
    }
  }

  let particles = [];
  let last = performance.now();

  // Launch fireworks periodically
  function launchFirework(){
    const x = rand(100, W-100);
    const y = rand(50, H/2);
    const hue = Math.floor(rand(0,360));
    const count = Math.floor(rand(20,40));
    for (let i=0;i<count;i++){
      const angle = rand(0, Math.PI*2);
      const speed = rand(1.5, 5.5);
      const life = rand(0.8, 1.6);
      const size = rand(1,3.5);
      const color = `hsl(${hue} ${Math.floor(rand(70,100))}% ${Math.floor(rand(45,65))}%)`;
      particles.push(new Particle(x, y, color, speed, angle, life, size));
    }
  }

  // random initial burst
  for (let i=0;i<6;i++){ setTimeout(launchFirework, i*600) }

  // continual fireworks
  setInterval(launchFirework, 1600 + Math.random()*1200);

  function loop(now){
    const dt = (now - last) * 0.06;
    last = now;
    ctx.clearRect(0,0,W,H);

    // subtle background glow
    ctx.fillStyle = "rgba(10,6,20,0.08)";
    ctx.fillRect(0,0,W,H);

    // update and draw particles
    for (let i = particles.length-1; i>=0; i--){
      const p = particles[i];
      p.update(dt);
      p.draw(ctx);
      if (p.life <= 0 || p.y > H+50) particles.splice(i,1);
    }
    requestAnimationFrame(loop);
  }
  requestAnimationFrame(loop);
})();
