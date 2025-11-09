from flask import Flask, request
from markupsafe import Markup


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    teacher_name = "Thầy/Cô kính mến"
    default_message = "Chúc mừng Ngày Nhà giáo Việt Nam 20/11! Lớp 11A6 Kính chúc Thầy/Cô luôn mạnh khỏe, hạnh phúc và thành công trong sự nghiệp trồng người!"
    message = default_message
    if request.method == "POST":
        message = request.form.get("message", default_message)

    html = f"""
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Chúc mừng Ngày Nhà giáo Việt Nam</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{height:100%;font-family:Segoe UI,Roboto,Arial,sans-serif;}}
body{{
  background:linear-gradient(180deg,#fff8f0,#fff0f6);
  color:#222;
  overflow-x:hidden;
}}
#fireworks-canvas{{position:fixed;inset:0;pointer-events:none;z-index:0;}}
.container{{position:relative;z-index:5;max-width:1000px;margin:40px auto;padding:20px;text-align:center;}}
.marquee{{
  display:inline-block;
  font-size:22px;
  font-weight:700;
  padding:8px 20px;
  border-radius:999px;
  background:rgba(255,255,255,0.85);
  box-shadow:0 8px 30px rgba(0,0,0,0.08);
  animation:slide 10s linear infinite;
  white-space:nowrap;
}}
@keyframes slide{{0%{{transform:translateX(0)}}50%{{transform:translateX(-20px)}}100%{{transform:translateX(0)}}}}
.teacher{{margin-top:12px;color:#6b2c91;font-weight:700}}
.card{{
  margin-top:18px;
  display:flex;
  gap:20px;
  align-items:center;
  justify-content:center;
  background:rgba(255,255,255,0.9);
  border-radius:14px;
  padding:18px;
  box-shadow:0 10px 30px rgba(102,51,153,0.08);
}}
@media(max-width:800px){{.card{{flex-direction:column}}}}
.teacher-image{{
  width:360px;
  max-width:100%;
  border-radius:10px;
  box-shadow:0 8px 20px rgba(0,0,0,0.08);
}}
.card-right{{max-width:480px;text-align:left}}
#message{{
  font-size:18px;
  line-height:1.5;
  background:linear-gradient(90deg,#fff,#fff7);
  padding:14px;
  border-radius:10px;
  margin-bottom:12px;
}}
.msg-form textarea{{
  width:100%;
  min-height:80px;
  border-radius:8px;
  padding:10px;
  resize:vertical;
  border:1px solid #e6d6f2;
  font-family:inherit;
}}
.msg-form button{{
  margin-top:8px;
  padding:8px 14px;
  border-radius:8px;
  border:none;
  cursor:pointer;
  background:linear-gradient(90deg,#f29bb7,#a05bd6);
  color:white;
  font-weight:600;
}}
#petal-root{{pointer-events:none;position:fixed;inset:0;z-index:4}}
.petal{{
  position:fixed;
  top:-10vh;
  width:18px;
  height:18px;
  border-radius:50% 50% 50% 10%;
  transform:rotate(0deg);
  background:radial-gradient(circle at 30% 30%,#fff5,#ffb6c1);
  filter:drop-shadow(0 2px 3px rgba(0,0,0,0.08));
  animation:fall linear infinite;
  opacity:0.9;
}}
@keyframes fall{{
  0%{{transform:translateY(-10vh) rotate(0deg);opacity:0}}
  10%{{opacity:1}}
  100%{{transform:translateY(120vh) rotate(720deg);opacity:0.9}}
}}
footer{{margin-top:16px;color:#6b6b6b}}
</style>
</head>
<body>
<canvas id="fireworks-canvas"></canvas>
<div class="container">
  <header>
    <h1 class="marquee">🌸 Chúc mừng Ngày Nhà giáo Việt Nam - 20/11 🌸</h1>
    <h2 class="teacher">Gửi: <span id="teacher-name">{teacher_name}</span></h2>
  </header>

  <main class="card">
    <div class="card-left">
      <img src="https://upload.wikimedia.org/wikipedia/commons/8/85/Vietnamese_teacher_day_20-11.jpg"
           alt="Thầy/Cô" class="teacher-image">
           default_message = "Chúc thầy/cô 8386"
           </div>
              <div class="card-right">
      <p id="message">{message}</p>
      <form method="post" class="msg-form">
      </form>
    </div>
  </main>

  <footer>
    <p>From: <strong>toàn bộ lớp 11A6</strong> — <small>Ngày Nhà giáo Việt Nam 20/11</small></p>
  </footer>
</div>
<div id="petal-root"></div>
<script>
  // hiệu ứng hoa rơi
  const petalRoot=document.getElementById('petal-root');
  const PETAL_COUNT=18;
  for(let i=0;i<PETAL_COUNT;i++){{
    const p=document.createElement('div');
    p.className='petal';
    p.style.left=Math.random()*100+'vw';
    p.style.animationDelay=(Math.random()*5)+'s';
    p.style.opacity=(0.6+Math.random()*0.4);
    petalRoot.appendChild(p);
  }}
</script>
<script>
// pháo hoa đơn giản
(function(){{
  const canvas=document.getElementById('fireworks-canvas');
  const ctx=canvas.getContext('2d');
  let W=canvas.width=innerWidth;
  let H=canvas.height=innerHeight;
  window.addEventListener('resize',()=>{{W=canvas.width=innerWidth;H=canvas.height=innerHeight;}});
  function rand(a,b){{return Math.random()*(b-a)+a;}}
  class P{{constructor(x,y,c,s,a,l,z){{this.x=x;this.y=y;this.vx=Math.cos(a)*s;this.vy=Math.sin(a)*s;this.life=l;this.alpha=1;this.size=z;this.color=c;}}
  update(dt){{this.vy+=0.02;this.x+=this.vx*dt;this.y+=this.vy*dt;this.life-=dt*0.02;this.alpha=Math.max(0,this.life);}}
  draw(){{ctx.globalAlpha=this.alpha;ctx.beginPath();ctx.fillStyle=this.color;ctx.arc(this.x,this.y,this.size,0,Math.PI*2);ctx.fill();ctx.globalAlpha=1;}}}}
  let ps=[];let last=performance.now();
  function boom(){{const x=rand(100,W-100);const y=rand(50,H/2);const h=Math.floor(rand(0,360));
  for(let i=0;i<rand(20,40);i++){{const a=rand(0,Math.PI*2);const s=rand(1.5,5.5);const l=rand(0.8,1.6);const z=rand(1,3.5);const c=`hsl(${{h}} ${{Math.floor(rand(70,100))}}% ${{Math.floor(rand(45,65))}}%)`;ps.push(new P(x,y,c,s,a,l,z));}}}}
  for(let i=0;i<6;i++)setTimeout(boom,i*600);
  setInterval(boom,1600+Math.random()*1200);
  function loop(n){{const dt=(n-last)*0.06;last=n;ctx.clearRect(0,0,W,H);ctx.fillStyle='rgba(10,6,20,0.08)';ctx.fillRect(0,0,W,H);
  for(let i=ps.length-1;i>=0;i--){{const p=ps[i];p.update(dt);p.draw();if(p.life<=0||p.y>H+50)ps.splice(i,1);}}
  requestAnimationFrame(loop);}}
  requestAnimationFrame(loop);
}})();
</script>
</body></html>
"""
    return Markup(html)

if __name__ == "__main__":
    app.run(debug=True)


