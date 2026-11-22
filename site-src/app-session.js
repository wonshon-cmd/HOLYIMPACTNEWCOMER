/* ---- Tend by name: 로그인 세션 (데모용, 브라우저에만 저장) ---- */
(function(){
  let S=null;try{S=JSON.parse(localStorage.getItem('tend-session')||'null')}catch(e){}
  const publicRoute=()=>/-(phone|notes)$/.test(location.hash.slice(1));
  const toLogin=()=>{location.replace('../?login=1')};
  function guard(){
    if(publicRoute())return true;               // 새가족 QR 화면은 로그인 없이
    if(!S||(!S.super&&S.org!=='njholyimpact')){toLogin();return false}
    if(!S.admin&&!S.super&&location.hash==='#team'){location.hash='w1-leader';return false}
    return true;
  }
  if(!guard())return;
  window.addEventListener('hashchange',guard);
  if(!S)return;

  // 순장은 팀장 대시보드 탭을 숨김
  if(!S.admin&&!S.super){const i=ROUTES.findIndex(r=>r.id==='team');if(i>=0)ROUTES.splice(i,1)}
  // 내가 배정된 주차에서는 내 화면으로
  if(S.id&&LEADERS.some(l=>l.id===S.id)){[1,2,3,4].forEach(w=>{if(db.assign[w]&&db.assign[w].includes(S.id))db.viewer[w]=S.id});save()}

  const css=document.createElement('style');
  css.textContent='.me-badge{display:flex;align-items:center;gap:10px;margin-left:auto;font-size:13px;white-space:nowrap}.me-badge b{font-weight:700}.me-badge span{color:var(--muted)}.me-badge button{border:1px solid var(--line);background:none;border-radius:999px;padding:5px 12px;font-size:12px;cursor:pointer;color:var(--ink)}.me-badge button:hover{border-color:var(--ink)}@media(max-width:720px){.me-badge span{display:none}}';
  document.head.appendChild(css);
  const wrap=document.querySelector('.top .wrap');
  if(wrap){const b=document.createElement('div');b.className='me-badge';
    b.innerHTML=`<b></b><span></span><button type="button">로그아웃</button>`;
    b.querySelector('b').textContent=S.name||'';b.querySelector('span').textContent=S.role||'';
    b.querySelector('button').addEventListener('click',()=>{try{localStorage.removeItem('tend-session')}catch(e){}location.href='../'});
    if(S.super){const c=document.createElement('a');c.href='../console/';c.textContent='전체 관리자';c.style.cssText='font-size:12px;text-decoration:underline';b.insertBefore(c,b.firstChild)}
    wrap.appendChild(b)}
  render();
})();
