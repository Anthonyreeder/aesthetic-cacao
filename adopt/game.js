// BDS Anthony — Adopt Game v2
// GAMES, SB_URL, SB_KEY are set by inline <script> in HTML

var XP_TABLE=[0,50,130,240,380,550,750,1000,1300,1650,2050,2500,3050,3700,4450,5300,6300,7450,8800,10400,12300];
var RARITY_LEVELS=[[1,'common','Common','#888'],[5,'uncommon','Uncommon','#44cc44'],[10,'rare','Rare','#4488ff'],[15,'epic','Epic','#aa44ff'],[20,'legendary','Legendary','#ffaa00']];
var CD_FEED=15*60000,CD_REST=45*60000,JOB_CD=10*60000,MAX_BATTLES=10;
var FEED_MSGS=["is feeling full!","loved that snack!","gobbled it up!","wants more already!"];
var REST_MSGS=["is recharging nicely.","needed that nap.","feels refreshed!","is full of energy now!"];
var JOB_WIN=["Nailed it! \uD83D\uDCB0","Easy money!","Like a pro!","Crushed it!","Ka-ching!","Smooth operator!"];
var JOB_FAIL=["Not this time...","So close!","Total fail \uD83D\uDC80","Better luck next time","Fumbled it...","Oof. That hurt."];

var JOBS={
fortnite:[
{emoji:"\uD83E\uDDF9",name:"Sweep Lobby Confetti",desc:"Someone has to clean up after Victory Royale",gold:1,base:95,lvl:1},
{emoji:"\uD83D\uDCE6",name:"Deliver Mats",desc:"Run building materials across the map",gold:2,base:75,lvl:3},
{emoji:"\uD83C\uDFD7\uFE0F",name:"Guard the Fort",desc:"Stand there and look intimidating",gold:4,base:55,lvl:6},
{emoji:"\u26C8\uFE0F",name:"Storm Scout",desc:"Check if the storm is still there (it is)",gold:8,base:35,lvl:10},
{emoji:"\uD83C\uDFAF",name:"Bounty Hunter",desc:"Track a target. Try not to get eliminated",gold:15,base:20,lvl:15}
],
minecraft:[
{emoji:"\uD83E\uDE93",name:"Punch Trees",desc:"Classic first day job. Splinter warning",gold:1,base:95,lvl:1},
{emoji:"\u26CF\uFE0F",name:"Mine Coal",desc:"Into the darkness for some rocks",gold:2,base:75,lvl:3},
{emoji:"\uD83C\uDF3E",name:"Farm Wheat",desc:"Don't jump on the crops!",gold:4,base:55,lvl:6},
{emoji:"\uD83D\uDD6F\uFE0F",name:"Cave Explorer",desc:"Bring torches. Lots of torches",gold:8,base:35,lvl:10},
{emoji:"\uD83D\uDC09",name:"Dragon Raid",desc:"Visit the End. What could go wrong?",gold:15,base:20,lvl:15}
],
roblox:[
{emoji:"\uD83E\uDE99",name:"Collect Coins",desc:"Run around the obby grabbing coins",gold:1,base:95,lvl:1},
{emoji:"\uD83C\uDF55",name:"Pizza Delivery",desc:"Work at the pizza place. Don't eat the order",gold:2,base:75,lvl:3},
{emoji:"\uD83C\uDFE6",name:"Guard the Bank",desc:"Jailbreak security duty. Nap responsibly",gold:4,base:55,lvl:6},
{emoji:"\uD83C\uDFC6",name:"Obby Champion",desc:"Complete the impossible tower",gold:8,base:35,lvl:10},
{emoji:"\uD83D\uDC7E",name:"Final Boss",desc:"Take on the ultimate challenge",gold:15,base:20,lvl:15}
]};

var LOOT_TIERS=[
{id:"basic",cost:1,emoji:"\uD83D\uDCE6",rates:{common:70,uncommon:20,rare:8,epic:2,legendary:0}},
{id:"silver",cost:3,emoji:"\uD83E\uDE99",rates:{common:35,uncommon:30,rare:22,epic:10,legendary:3}},
{id:"gold",cost:8,emoji:"\u2728",rates:{common:10,uncommon:20,rare:35,epic:25,legendary:10}},
{id:"diamond",cost:20,emoji:"\uD83D\uDC8E",rates:{common:0,uncommon:10,rare:25,epic:40,legendary:25}}
];
var LOOT_BOX_NAMES={
fortnite:["Supply Drop","Rare Supply","Epic Supply","Mythic Supply"],
minecraft:["Wooden Chest","Iron Chest","Gold Chest","Diamond Chest"],
roblox:["Basic Crate","Silver Crate","Gold Crate","Rainbow Crate"]
};
var LOOT_ITEMS={
fortnite:{
common:[{n:"Rusty Pistol",e:"\uD83D\uDD2B"},{n:"Grey AR",e:"\uD83D\uDD2B"},{n:"Bandage Wrap",e:"\uD83E\uDE79"}],
uncommon:[{n:"Green Pump",e:"\uD83D\uDCA2"},{n:"Green SMG",e:"\uD83D\uDCA8"},{n:"Shield Pot",e:"\uD83D\uDEE1\uFE0F"}],
rare:[{n:"Blue SCAR",e:"\uD83D\uDCA5"},{n:"Blue Tac",e:"\uD83D\uDD35"},{n:"Rift-to-Go",e:"\uD83C\uDF00"}],
epic:[{n:"Purple RPG",e:"\uD83D\uDE80"},{n:"Heavy Sniper",e:"\uD83C\uDFAF"},{n:"Shockwave",e:"\uD83D\uDCA0"}],
legendary:[{n:"Gold SCAR",e:"\u2B50"},{n:"Mythic Drum Gun",e:"\uD83C\uDF1F"},{n:"Infinity Blade",e:"\u2694\uFE0F"}]
},
minecraft:{
common:[{n:"Wooden Sword",e:"\uD83E\uDEB5"},{n:"Stone Pick",e:"\u26CF\uFE0F"},{n:"Leather Tunic",e:"\uD83D\uDC55"}],
uncommon:[{n:"Iron Sword",e:"\u2694\uFE0F"},{n:"Iron Armor",e:"\uD83D\uDEE1\uFE0F"},{n:"Bow",e:"\uD83C\uDFF9"}],
rare:[{n:"Diamond Sword",e:"\uD83D\uDC8E"},{n:"Diamond Armor",e:"\uD83D\uDC8E"},{n:"Crossbow",e:"\uD83C\uDFF9"}],
epic:[{n:"Enchanted Blade",e:"\u2728"},{n:"Elytra Wings",e:"\uD83E\uDEBD"},{n:"Trident",e:"\uD83D\uDD31"}],
legendary:[{n:"Netherite Sword",e:"\uD83C\uDF1F"},{n:"Netherite Armor",e:"\u2B50"},{n:"Totem of Undying",e:"\uD83D\uDDFF"}]
},
roblox:{
common:[{n:"Basic Blaster",e:"\uD83D\uDD2B"},{n:"Wooden Bat",e:"\uD83C\uDFCF"},{n:"Noob Shield",e:"\uD83D\uDEE1\uFE0F"}],
uncommon:[{n:"Laser Gun",e:"\uD83D\uDCA2"},{n:"Katana",e:"\u2694\uFE0F"},{n:"Speed Coil",e:"\uD83C\uDF00"}],
rare:[{n:"Gravity Coil",e:"\uD83D\uDD35"},{n:"Linked Sword",e:"\uD83D\uDCA5"},{n:"Hyperlaser",e:"\uD83D\uDD35"}],
epic:[{n:"Dark Heart",e:"\uD83D\uDDA4"},{n:"Ghost Blade",e:"\uD83D\uDC7B"},{n:"Rainbow Carpet",e:"\uD83C\uDF08"}],
legendary:[{n:"Dominus Blade",e:"\u2B50"},{n:"Korblox Sword",e:"\uD83C\uDF1F"},{n:"Illumina",e:"\u2694\uFE0F"}]
}};
var LOOT_POWER={common:[1,3],uncommon:[4,7],rare:[8,12],epic:[13,18],legendary:[19,25]};
var RARITY_ORDER=["common","uncommon","rare","epic","legendary"];
var RARITY_COLORS={common:"#888",uncommon:"#44cc44",rare:"#4488ff",epic:"#aa44ff",legendary:"#ffaa00"};
var FAKE_NAMES=["xXShadowXx","ProGamer99","NightWolf","DragonSlyr","NoobKing","StormRider","DarkNinja","CoolKid420","MegaBoss","TurboFox","GhostFace","LazerBeam","IceCold","BigChungus","EpicFail","YoloSwag","BotSlayer","PixelKing","ToxicAvenger","SkullCrusher","SilentStrike","BlazeMaster","FrostByte","VenomViper","ThunderBolt"];

// ── State ──────────────────────────────────────────────────
var KEY="bds_pet_v1",pet=null,sb=null,_sbSession=null,_pendingLoot=null,_opponents=[];
try{sb=window.supabase.createClient(SB_URL,SB_KEY);}catch(e){console.warn("Supabase unavailable, offline mode");}

// ── Core ───────────────────────────────────────────────────
function load(){
try{pet=JSON.parse(localStorage.getItem(KEY));}catch(e){pet=null;}
if(pet){
if(pet.str===undefined)pet.str=1;
if(pet.def===undefined)pet.def=1;
if(pet.hp===undefined)pet.hp=10;
if(pet.gold===undefined)pet.gold=1;
if(!pet.weapon)pet.weapon=null;
if(!pet.wins)pet.wins=0;
if(!pet.losses)pet.losses=0;
if(!pet.bat_today)pet.bat_today=0;
if(!pet.bat_date)pet.bat_date="";
if(!pet.last_job)pet.last_job=0;
if(!pet.last_train_stat)pet.last_train_stat="str";
}}
function save(){localStorage.setItem(KEY,JSON.stringify(pet));}
function show(id){document.querySelectorAll(".screen").forEach(function(s){s.classList.remove("active");});document.getElementById(id).classList.add("active");}
function getRarity(lv){var r=RARITY_LEVELS[0];for(var i=0;i<RARITY_LEVELS.length;i++)if(lv>=RARITY_LEVELS[i][0])r=RARITY_LEVELS[i];return r;}
function xpForNext(lv){return lv>=XP_TABLE.length-1?99999:XP_TABLE[lv]-XP_TABLE[lv-1];}
function xpInLevel(lv,xp){return lv<=1?xp:xp-XP_TABLE[lv-1];}
function levelFromXp(xp){for(var i=1;i<XP_TABLE.length;i++)if(xp<XP_TABLE[i])return i;return XP_TABLE.length;}

function getTrainCD(statLv){
if(statLv<=10)return 5*60000;
if(statLv<=15)return 15*60000;
if(statLv<=25)return 30*60000;
return 60*60000;
}
function getJobChance(base){return Math.min(95,base+Math.floor((pet?pet.level:1)*1.5));}
function resetBattlesIfNewDay(){var d=new Date().toDateString();if(pet&&pet.bat_date!==d){pet.bat_today=0;pet.bat_date=d;save();}}

function getMood(){
if(pet.hunger<15)return["\uD83D\uDE29","Starving!","#ff4444"];
if(pet.happiness<20)return["\uD83D\uDE22","Sad...","#ff6b6b"];
if(pet.energy<15)return["\uD83D\uDE34","Exhausted","#8888ff"];
if(pet.hunger<35)return["\uD83D\uDE15","Hungry","#ffaa44"];
if(pet.happiness>80&&pet.hunger>60&&pet.energy>60)return["\uD83E\uDD29","Ecstatic!","#ffcc00"];
if(pet.happiness>60)return["\uD83D\uDE0A","Happy","#66ee66"];
return["\uD83D\uDE10","Okay","#7a788e"];
}

function calcOffline(){
if(!pet||!pet.lastVisit)return null;
var now=Date.now(),hrs=(now-pet.lastVisit)/3600000;
if(hrs<0.01)return null;
var r={hours:hrs,oH:pet.hunger,oE:pet.energy,oP:pet.happiness};
pet.hunger=Math.max(0,Math.round(pet.hunger-hrs*8));
pet.energy=Math.min(100,Math.round(pet.energy+hrs*4));
pet.happiness=Math.max(0,Math.round(pet.happiness-hrs*(pet.hunger<25?5:1.5)));
r.nH=pet.hunger;r.nE=pet.energy;r.nP=pet.happiness;
pet.lastVisit=now;save();return r;
}

function showAway(r){
if(!r||r.hours<0.05){document.getElementById("away-box").innerHTML="";return;}
var h=r.hours,ts=h>=1?Math.floor(h)+"h "+Math.round((h%1)*60)+"m":Math.round(h*60)+"m";
function d(o,n){var v=Math.round(n-o);return v>=0?"+"+v:""+v;}
function c(o,n){return n>=o?"pos":"neg";}
document.getElementById("away-box").innerHTML='<div class="away-report"><h3>While you were away ('+ts+')</h3>'+
'<div class="away-line"><span>\uD83C\uDF56 Hunger</span><span class="change '+c(r.oH,r.nH)+'">'+d(r.oH,r.nH)+'% \u2192 '+r.nH+'%</span></div>'+
'<div class="away-line"><span>\u26A1 Energy</span><span class="change '+c(r.oE,r.nE)+'">'+d(r.oE,r.nE)+'% \u2192 '+r.nE+'%</span></div>'+
'<div class="away-line"><span>\uD83D\uDC96 Happy</span><span class="change '+c(r.oP,r.nP)+'">'+d(r.oP,r.nP)+'% \u2192 '+r.nP+'%</span></div></div>';
setTimeout(function(){document.getElementById("away-box").innerHTML="";},8000);
}

// ── UI ─────────────────────────────────────────────────────
function updateUI(){
if(!pet)return;
document.getElementById("pet-emoji").textContent=pet.emoji;
document.getElementById("pet-name").textContent=pet.name;
document.getElementById("pet-level").textContent="Level "+pet.level;
var rar=getRarity(pet.level);
document.getElementById("pet-rarity").textContent=rar[2];
document.getElementById("pet-rarity").style.cssText="background:"+rar[3]+"22;color:"+rar[3];
document.getElementById("pet-card").className="pet-card rarity-"+rar[1];
var mood=getMood();
document.getElementById("pet-mood").textContent=mood[0]+" "+mood[1];
document.getElementById("pet-mood").style.color=mood[2];
var needed=xpForNext(pet.level),inLvl=xpInLevel(pet.level,pet.xp),pct=Math.min(100,needed>0?(inLvl/needed)*100:100);
document.getElementById("xp-fill").style.width=pct+"%";
document.getElementById("xp-text").textContent=inLvl+"/"+needed+" XP";
document.getElementById("xp-next").textContent="Level "+(pet.level+1);
function sb(id,val,vid){var el=document.getElementById(id);el.style.width=val+"%";el.style.background=val>60?"#44cc44":val>30?"#ddaa00":"#ff4444";document.getElementById(vid).textContent=Math.round(val)+"%";}
sb("bar-hunger",pet.hunger,"val-hunger");sb("bar-energy",pet.energy,"val-energy");sb("bar-happy",pet.happiness,"val-happy");
var ms=Date.now()-(pet.created||Date.now()),dd=Math.floor(ms/86400000),hh=Math.floor((ms%86400000)/3600000);
document.getElementById("pet-age").textContent=dd>0?dd+"d "+hh+"h":hh>0?hh+"h":"just now";
// Gold & weapon
var ga=document.querySelectorAll(".gold-amt");for(var g=0;g<ga.length;g++)ga[g].textContent=pet.gold||0;
var wd=document.getElementById("weapon-display");
if(pet.weapon)wd.innerHTML=pet.weapon.emoji+" "+pet.weapon.name+' <span style="color:'+RARITY_COLORS[pet.weapon.rarity]+'">('+pet.weapon.power+' ATK)</span>';
else wd.textContent="\u2694\uFE0F No weapon";
var ws=document.getElementById("current-weapon");
if(pet.weapon)ws.innerHTML='<span style="font-size:1.5rem">'+pet.weapon.emoji+'</span><div style="flex:1"><div style="font-weight:700">'+pet.weapon.name+'</div><div style="font-size:.72rem;color:var(--muted)">\u2694\uFE0F '+pet.weapon.power+' ATK</div></div><span class="ws-rarity" style="background:'+RARITY_COLORS[pet.weapon.rarity]+'22;color:'+RARITY_COLORS[pet.weapon.rarity]+'">'+pet.weapon.rarity+'</span>';
else ws.innerHTML='<span class="ws-empty">No weapon equipped \u2014 open a loot box!</span>';
}

function updateCD(){
if(!pet)return;var now=Date.now();
function sc(a,cd,bi,ci){var rem=Math.max(0,(pet["last_"+a]||0)+cd-now),b=document.getElementById(bi),c=document.getElementById(ci);
b.classList.remove("ready","on-cooldown","no-energy");
if(rem>0){b.classList.add("on-cooldown");var m=Math.floor(rem/60000),s=Math.floor((rem%60000)/1000);c.textContent=m+":"+(s<10?"0":"")+s;c.classList.remove("ready-text");}
else{b.classList.add("ready");c.textContent="Ready!";c.classList.add("ready-text");}}
sc("feed",CD_FEED,"btn-feed","cd-feed");sc("rest",CD_REST,"btn-rest","cd-rest");
}

function toast(msg){var t=document.getElementById("toast");t.textContent=msg;t.classList.add("show");setTimeout(function(){t.classList.remove("show");},2500);}

function confetti(){
var c=document.getElementById("lvl-confetti");c.innerHTML="";
var cols=["#ff5c87","#7c5cff","#00d2b4","#ffcc00","#ff6b6b","#50c8ff","#60dd60","#ffa040","#aa44ff","#ffaa00"];
for(var i=0;i<50;i++){var p=document.createElement("div");p.className="c";p.style.left=Math.random()*100+"%";p.style.top="-10px";p.style.background=cols[i%cols.length];p.style.animationDelay=Math.random()*0.8+"s";p.style.width=(5+Math.random()*8)+"px";p.style.height=p.style.width;c.appendChild(p);}
setTimeout(function(){c.innerHTML="";},3000);
}

function showLevelUp(lv,oldR,newR){
document.getElementById("lvl-text").textContent="LEVEL "+lv+"!";
document.getElementById("lvl-sub").textContent=pet.name+" grew stronger!";
document.getElementById("lvl-rarity").innerHTML=oldR[1]!==newR[1]?'Evolved to <span style="color:'+newR[3]+'">'+newR[2]+"</span>!":"";
document.getElementById("levelup").classList.add("show");confetti();
if(typeof gtag!=="undefined")gtag("event","pet_levelup",{level:lv,rarity:newR[1],game:pet.game});
setTimeout(function(){document.getElementById("levelup").classList.remove("show");},2800);
}

// ── Tab System ─────────────────────────────────────────────
window._switchTab=function(tab){
document.querySelectorAll(".tab-btn").forEach(function(b){b.classList.remove("active");});
document.querySelectorAll(".tab-panel").forEach(function(p){p.classList.remove("active");});
var btn=document.querySelector('[data-tab="'+tab+'"]');if(btn)btn.classList.add("active");
var panel=document.getElementById("panel-"+tab);if(panel)panel.classList.add("active");
if(tab==="battle")refreshOpponents();
if(tab==="jobs")updateJobs();
if(tab==="loot")updateLoot();
if(tab==="train")updateTrainUI();
};

// ── Actions (Feed / Rest) ──────────────────────────────────
window._doAction=function(action){
if(!pet)return;var now=Date.now(),cds={feed:CD_FEED,rest:CD_REST};
if(now-(pet["last_"+action]||0)<cds[action])return;
var oldLv=pet.level,oldR=getRarity(oldLv),msgs,res="";
if(action==="feed"){pet.hunger=Math.min(100,pet.hunger+25);pet.happiness=Math.min(100,pet.happiness+5);msgs=FEED_MSGS;}
else{pet.energy=Math.min(100,pet.energy+40);pet.happiness=Math.min(100,pet.happiness+10);msgs=REST_MSGS;}
pet["last_"+action]=now;pet.lastVisit=now;save();updateUI();updateCD();
toast(res+pet.name+" "+msgs[Math.floor(Math.random()*msgs.length)]);
if(typeof gtag!=="undefined")gtag("event","pet_action",{action:action,game:pet.game,level:pet.level});
if(pet.level>oldLv)setTimeout(function(){showLevelUp(pet.level,oldR,getRarity(pet.level));},400);
cloudSync();checkSavePrompt();
};

// ── Training ───────────────────────────────────────────────
function updateTrainUI(){
if(!pet)return;
var stats=[{key:"str",name:"Strength",icon:"\uD83D\uDCAA",color:"#ff6b6b",max:50},{key:"def",name:"Defence",icon:"\uD83D\uDEE1\uFE0F",color:"#4488ff",max:50},{key:"hp",name:"Health",icon:"\u2764\uFE0F",color:"#44cc44",max:100}];
var cont=document.getElementById("train-cards");
var now=Date.now();
var lastSK=pet.last_train_stat||"str";
var cdDur=getTrainCD(pet[lastSK]||1);
var rem=Math.max(0,(pet.last_train||0)+cdDur-now);
cont.innerHTML="";
stats.forEach(function(s){
var val=pet[s.key]||1;
var pct=Math.min(100,(val/s.max)*100);
var div=document.createElement("div");div.className="train-card";
var btnH;
if(rem>0){var m=Math.floor(rem/60000),sec=Math.floor((rem%60000)/1000);btnH='<span class="train-cd">'+m+":"+(sec<10?"0":"")+sec+"</span>";}
else if(pet.energy<10){btnH='<span class="train-cd" style="color:#ff6b6b">Low energy</span>';}
else{btnH='<button class="train-btn" onclick="window._doTrain(\''+s.key+"')\">Train +1</button>";}
div.innerHTML='<div class="tc-icon">'+s.icon+'</div><div class="tc-info"><div class="tc-name">'+s.name+'</div><div class="tc-level">Level '+val+'</div><div class="tc-bar"><div class="tc-fill" style="width:'+pct+"%;background:"+s.color+'"></div></div></div>'+btnH;
cont.appendChild(div);
});
}

window._doTrain=function(stat){
if(!pet)return;var now=Date.now();
var lastSK=pet.last_train_stat||"str";
var cdDur=getTrainCD(pet[lastSK]||1);
if(now-(pet.last_train||0)<cdDur)return;
if(pet.energy<10){toast("Need more energy! Rest first.");return;}
pet[stat]+=1;pet.last_train=now;pet.last_train_stat=stat;
pet.energy=Math.max(0,pet.energy-10);pet.hunger=Math.max(0,pet.hunger-5);
pet.lastVisit=now;save();updateUI();updateTrainUI();
var names={str:"Strength",def:"Defence",hp:"Health"};
toast(pet.name+"'s "+names[stat]+" is now "+pet[stat]+"! \uD83D\uDCAA");
if(typeof gtag!=="undefined")gtag("event","pet_train_stat",{stat:stat,value:pet[stat],game:pet.game});
cloudSync();
};

// ── Jobs ───────────────────────────────────────────────────
function updateJobs(){
if(!pet)return;
var jobs=JOBS[pet.game]||JOBS.fortnite;
var now=Date.now(),rem=Math.max(0,(pet.last_job||0)+JOB_CD-now);
var cdEl=document.getElementById("job-cd-global");
if(rem>0){var m=Math.floor(rem/60000),s=Math.floor((rem%60000)/1000);cdEl.textContent="Next job in "+m+":"+(s<10?"0":"")+s;}
else cdEl.textContent="";
var cont=document.getElementById("jobs-list");cont.innerHTML="";
jobs.forEach(function(job,idx){
var locked=pet.level<job.lvl,onCd=rem>0&&!locked;
var chance=getJobChance(job.base);
var div=document.createElement("div");
div.className="job-card"+(locked?" locked":"")+(onCd?" on-cd":"");
div.id="job-"+idx;
div.innerHTML='<div class="job-top"><span class="job-emoji">'+job.emoji+'</span><div class="job-info"><div class="job-name">'+job.name+'</div><div class="job-desc">'+job.desc+'</div></div><div class="job-reward"><div class="job-gold">\uD83D\uDCB0 '+job.gold+'</div><div class="job-chance">'+(locked?"Lv "+job.lvl+" req":chance+"% chance")+'</div></div></div><div class="job-anim"><div class="ja-emoji"></div><div class="ja-text"></div></div>';
if(!locked&&!onCd)div.onclick=function(){window._doJob(idx);};
cont.appendChild(div);
});
}

window._doJob=function(idx){
if(!pet)return;var now=Date.now();
if(now-(pet.last_job||0)<JOB_CD)return;
var jobs=JOBS[pet.game]||JOBS.fortnite;var job=jobs[idx];
if(!job||pet.level<job.lvl)return;
var chance=getJobChance(job.base);
var success=Math.random()*100<chance;
pet.last_job=now;pet.lastVisit=now;
var card=document.getElementById("job-"+idx);if(!card)return;
var anim=card.querySelector(".job-anim");
var emojiEl=anim.querySelector(".ja-emoji"),textEl=anim.querySelector(".ja-text");
anim.className="job-anim show";emojiEl.textContent=job.emoji;textEl.textContent="Working...";
setTimeout(function(){
if(success){
pet.gold+=job.gold;emojiEl.textContent="\uD83D\uDCB0";
textEl.textContent="+"+job.gold+" gold! "+JOB_WIN[Math.floor(Math.random()*JOB_WIN.length)];
anim.classList.remove("fail");
}else{
emojiEl.textContent="\u274C";
textEl.textContent=JOB_FAIL[Math.floor(Math.random()*JOB_FAIL.length)];
anim.classList.add("fail");
}
save();updateUI();
if(typeof gtag!=="undefined")gtag("event","pet_job",{job:job.name,success:success,gold:success?job.gold:0,game:pet.game});
cloudSync();
setTimeout(function(){anim.classList.remove("show","fail");updateJobs();},1800);
},1500);
};

// ── Loot Boxes ─────────────────────────────────────────────
function updateLoot(){
if(!pet)return;
var cont=document.getElementById("loot-grid");cont.innerHTML="";
var names=LOOT_BOX_NAMES[pet.game]||LOOT_BOX_NAMES.fortnite;
LOOT_TIERS.forEach(function(tier,idx){
var locked=pet.gold<tier.cost;
var div=document.createElement("div");
div.className="loot-box lb-"+tier.id+(locked?" locked":"");
div.innerHTML='<div class="lb-emoji">'+tier.emoji+'</div><div class="lb-name">'+names[idx]+'</div><div class="lb-cost">\uD83D\uDCB0 '+tier.cost+' Gold</div><div class="lb-hint">'+(locked?"Need more gold":"Tap to open!")+"</div>";
if(!locked)div.onclick=function(){window._openLoot(idx);};
cont.appendChild(div);
});
}

window._openLoot=function(tierIdx){
if(!pet)return;var tier=LOOT_TIERS[tierIdx];
if(pet.gold<tier.cost){toast("Not enough gold!");return;}
pet.gold-=tier.cost;
var rates={};for(var k in tier.rates)rates[k]=tier.rates[k];
var lb=Math.min(20,pet.level);
rates.legendary=Math.min(50,rates.legendary+lb*0.5);
rates.epic=Math.min(40,rates.epic+lb*0.3);
rates.common=Math.max(0,rates.common-lb);
var total=0;for(var k in rates)total+=rates[k];
var r=Math.random()*total,cum=0,rarity="common";
for(var i=0;i<RARITY_ORDER.length;i++){cum+=rates[RARITY_ORDER[i]];if(r<=cum){rarity=RARITY_ORDER[i];break;}}
var pool=(LOOT_ITEMS[pet.game]||LOOT_ITEMS.fortnite)[rarity];
var item=pool[Math.floor(Math.random()*pool.length)];
var pw=LOOT_POWER[rarity],atk=pw[0]+Math.floor(Math.random()*(pw[1]-pw[0]+1));
_pendingLoot={name:item.n,emoji:item.e,rarity:rarity,power:atk};
var ol=document.getElementById("loot-overlay");
ol.querySelector(".lr-emoji").textContent=item.e;
ol.querySelector(".lr-name").textContent=item.n;
ol.querySelector(".lr-rarity").textContent=rarity.toUpperCase();
ol.querySelector(".lr-rarity").style.color=RARITY_COLORS[rarity];
ol.querySelector(".lr-power").textContent="\u2694\uFE0F "+atk+" ATK";
ol.querySelector(".loot-reveal").style.borderColor=RARITY_COLORS[rarity];
ol.classList.add("show");
save();updateUI();updateLoot();
if(typeof gtag!=="undefined")gtag("event","loot_opened",{tier:tier.id,rarity:rarity,item:item.n,game:pet.game});
cloudSync();
};

window._equipLoot=function(){
if(!_pendingLoot||!pet)return;
var old=pet.weapon;pet.weapon=_pendingLoot;_pendingLoot=null;
document.getElementById("loot-overlay").classList.remove("show");
save();updateUI();updateLoot();
toast("Equipped "+pet.weapon.name+"! \u2694\uFE0F");
if(old)toast("Replaced "+old.name);
cloudSync();
};

window._discardLoot=function(){
_pendingLoot=null;
document.getElementById("loot-overlay").classList.remove("show");
toast("Item discarded");
};

// ── Battle System ──────────────────────────────────────────
function generateOpponents(){
_opponents=[];var g=GAMES[pet.game];
for(var i=0;i<3;i++){
var lvl=Math.max(1,pet.level+Math.floor(Math.random()*7)-3);
var ch=g.chars[Math.floor(Math.random()*g.chars.length)];
var st=1+Math.floor(lvl*0.8+Math.random()*3);
var df=1+Math.floor(lvl*0.6+Math.random()*3);
var hp=10+lvl*3+Math.floor(Math.random()*5);
var ri=Math.min(4,Math.floor(Math.random()*(1+lvl/5)));
var pw=LOOT_POWER[RARITY_ORDER[ri]];
var wpnPow=Math.random()<(0.3+lvl*0.03)?pw[0]+Math.floor(Math.random()*(pw[1]-pw[0]+1)):0;
_opponents.push({emoji:ch[0],name:FAKE_NAMES[Math.floor(Math.random()*FAKE_NAMES.length)]+"#"+Math.floor(1000+Math.random()*9000),level:lvl,str:st,def:df,maxHp:hp,wpnPow:wpnPow});
}
return _opponents;
}

function refreshOpponents(){
if(!pet)return;
resetBattlesIfNewDay();
var cont=document.getElementById("opp-list"),hdr=document.getElementById("battle-header");
if(!cont||!hdr)return;
hdr.querySelector(".bh-left").textContent="Battles: "+(MAX_BATTLES-pet.bat_today)+"/"+MAX_BATTLES+" remaining";
hdr.querySelector(".bh-wins").textContent=pet.wins||0;
hdr.querySelector(".bh-losses").textContent=pet.losses||0;
if(pet.bat_today>=MAX_BATTLES){cont.innerHTML='<div class="no-battles">No battles left today! Come back tomorrow \uD83C\uDF05</div>';return;}
if(_opponents.length===0)generateOpponents();
cont.innerHTML="";
_opponents.forEach(function(opp,i){
var div=document.createElement("div");div.className="opp-card";
div.innerHTML='<span class="opp-emoji">'+opp.emoji+'</span><div class="opp-info"><div class="opp-name">'+opp.name+'</div><div class="opp-level">Level '+opp.level+'</div></div><div class="opp-hp">\u2764\uFE0F '+opp.maxHp+" HP</div>";
div.onclick=function(){startBattle(i);};
cont.appendChild(div);
});
}

function startBattle(oppIdx){
if(!pet||pet.bat_today>=MAX_BATTLES)return;
var opp=_opponents[oppIdx];if(!opp)return;
var myMax=pet.hp*3+10,myHp=myMax,oppMax=opp.maxHp,oppHp=oppMax;
var myAtk=pet.str+(pet.weapon?pet.weapon.power:0),oppAtk=opp.str+opp.wpnPow;
var myDef=pet.def,oppDef=opp.def;
var ol=document.getElementById("battle-overlay");
ol.querySelector(".bf-you .bf-emoji").textContent=pet.emoji;
ol.querySelector(".bf-you .bf-name").textContent=pet.name;
ol.querySelector(".bf-opp .bf-emoji").textContent=opp.emoji;
ol.querySelector(".bf-opp .bf-name").textContent=opp.name;
ol.querySelector(".bf-you .bf-hp-text").textContent=myHp+"/"+myMax;
ol.querySelector(".bf-opp .bf-hp-text").textContent=oppHp+"/"+oppMax;
ol.querySelector(".bf-you .bf-hp-fill").style.width="100%";
ol.querySelector(".bf-opp .bf-hp-fill").style.width="100%";
ol.querySelector(".bf-you .bf-hp-fill").style.background="#44cc44";
ol.querySelector(".bf-opp .bf-hp-fill").style.background="#44cc44";
ol.querySelector("#ba-result").style.display="none";
ol.querySelector("#ba-rewards").textContent="";
ol.querySelector("#ba-close").style.display="none";
var log=ol.querySelector("#ba-log");log.innerHTML="";
ol.classList.add("show");
function updHP(side,cur,max){
var pct=Math.max(0,(cur/max)*100);
ol.querySelector(side+" .bf-hp-fill").style.width=pct+"%";
ol.querySelector(side+" .bf-hp-text").textContent=cur+"/"+max;
ol.querySelector(side+" .bf-hp-fill").style.background=pct>50?"#44cc44":pct>25?"#ddaa00":"#ff4444";
}
function doTurn(){
if(myHp<=0||oppHp<=0){endBattle(myHp>0,opp,ol);return;}
var dmg=Math.max(1,myAtk-Math.floor(oppDef/2)+Math.floor(Math.random()*4));
oppHp=Math.max(0,oppHp-dmg);
log.innerHTML+='<div class="dmg-them">'+pet.name+" hits for "+dmg+" damage!</div>";
updHP(".bf-opp",oppHp,oppMax);log.scrollTop=log.scrollHeight;
if(oppHp<=0){setTimeout(function(){endBattle(true,opp,ol);},600);return;}
setTimeout(function(){
var dmg2=Math.max(1,oppAtk-Math.floor(myDef/2)+Math.floor(Math.random()*4));
myHp=Math.max(0,myHp-dmg2);
log.innerHTML+='<div class="dmg-you">'+opp.name+" hits for "+dmg2+" damage!</div>";
updHP(".bf-you",myHp,myMax);log.scrollTop=log.scrollHeight;
if(myHp<=0){setTimeout(function(){endBattle(false,opp,ol);},600);return;}
setTimeout(doTurn,800);
},500);
}
setTimeout(doTurn,800);
}

function endBattle(won,opp,ol){
pet.bat_today++;
if(won){
pet.wins=(pet.wins||0)+1;
var xpR=10+opp.level*2,goldR=1+Math.floor(opp.level/3);
pet.xp+=xpR;pet.gold+=goldR;
var oldLv=pet.level;pet.level=levelFromXp(pet.xp);
ol.querySelector("#ba-result").textContent="VICTORY!";
ol.querySelector("#ba-result").className="ba-result win";
ol.querySelector("#ba-rewards").textContent="+"+xpR+" XP, +"+goldR+" gold";
if(pet.level>oldLv)setTimeout(function(){showLevelUp(pet.level,getRarity(oldLv),getRarity(pet.level));},500);
}else{
pet.losses=(pet.losses||0)+1;
ol.querySelector("#ba-result").textContent="DEFEATED";
ol.querySelector("#ba-result").className="ba-result lose";
ol.querySelector("#ba-rewards").textContent="Better luck next time!";
}
ol.querySelector("#ba-result").style.display="block";
ol.querySelector("#ba-close").style.display="inline-block";
generateOpponents();save();updateUI();
if(typeof gtag!=="undefined")gtag("event","pet_battle",{won:won,opp_level:opp.level,game:pet.game});
cloudSync();
}

window._closeBattle=function(){
document.getElementById("battle-overlay").classList.remove("show");
refreshOpponents();
};

// ── Supabase Auth + Cloud Sync ─────────────────────────────
function cloudSync(){
if(!sb||!_sbSession||!pet)return;
sb.from("pets").upsert({
user_id:_sbSession.user.id,game:pet.game,emoji:pet.emoji,name:pet.name,
level:pet.level,xp:pet.xp,hunger:Math.round(pet.hunger),energy:Math.round(pet.energy),
happiness:Math.round(pet.happiness),last_feed:pet.last_feed||0,last_train:pet.last_train||0,
last_rest:pet.last_rest||0,last_visit:new Date().toISOString(),
strength:pet.str||1,defence:pet.def||1,health:pet.hp||10,
gold:pet.gold||0,weapon:pet.weapon?JSON.stringify(pet.weapon):null,
wins:pet.wins||0,losses:pet.losses||0
},{onConflict:"user_id"}).then(function(){});
}

function loadCloudPet(){
if(!sb||!_sbSession)return Promise.resolve(false);
return sb.from("pets").select("*").eq("user_id",_sbSession.user.id).maybeSingle().then(function(res){
if(!res.data)return false;var d=res.data;
pet={game:d.game,emoji:d.emoji,name:d.name,level:d.level,xp:d.xp,hunger:d.hunger,energy:d.energy,
happiness:d.happiness,last_feed:d.last_feed,last_train:d.last_train,last_rest:d.last_rest,
created:new Date(d.created_at).getTime(),lastVisit:new Date(d.last_visit).getTime(),
str:d.strength||1,def:d.defence||1,hp:d.health||10,gold:d.gold||0,
weapon:d.weapon?JSON.parse(d.weapon):null,wins:d.wins||0,losses:d.losses||0,
bat_today:0,bat_date:"",last_job:0,last_train_stat:"str"};
save();return true;
}).catch(function(){return false;});
}

function showAccountBar(){
if(!_sbSession)return;
sb.from("profiles").select("display_name").eq("id",_sbSession.user.id).maybeSingle().then(function(res){
var name=(res.data&&res.data.display_name)||_sbSession.user.email;
document.getElementById("account-name").textContent=name;
document.getElementById("account-bar").classList.add("show");
});
}
function hideAccountBar(){document.getElementById("account-bar").classList.remove("show");}

function checkSavePrompt(){
if(_sbSession||!pet)return;
var v=parseInt(localStorage.getItem("bds_visits")||"0");
if((pet.level>=3||v>=3)&&!sessionStorage.getItem("save_dismissed")){
document.getElementById("save-pet-name").textContent=pet.name;
document.getElementById("save-banner").classList.add("show");
}
}

window._dismissSave=function(){sessionStorage.setItem("save_dismissed","1");document.getElementById("save-banner").classList.remove("show");};
window._openAuth=function(mode){
document.getElementById("save-banner").classList.remove("show");
document.getElementById("auth-register").style.display=mode==="register"?"block":"none";
document.getElementById("auth-login").style.display=mode==="login"?"block":"none";
document.getElementById("reg-error").style.display="none";
document.getElementById("login-error").style.display="none";
if(mode==="register"&&pet)document.getElementById("auth-reg-sub").textContent="Create a free account so you never lose "+pet.name;
document.getElementById("auth-overlay").classList.add("show");
};
window._closeAuth=function(){document.getElementById("auth-overlay").classList.remove("show");};
function showAuthError(id,msg){var el=document.getElementById(id);el.textContent=msg;el.style.display="block";}

window._doRegister=function(){
if(!sb)return;
var name=document.getElementById("reg-name").value.trim();
var email=document.getElementById("reg-email").value.trim();
var pass=document.getElementById("reg-pass").value;
var age=parseInt(document.getElementById("reg-age").value)||null;
if(!name){showAuthError("reg-error","Please enter a display name");return;}
if(!email){showAuthError("reg-error","Please enter your email");return;}
if(pass.length<6){showAuthError("reg-error","Password must be 6+ characters");return;}
var btn=document.getElementById("reg-btn");btn.disabled=true;btn.textContent="Creating...";
sb.auth.signUp({email:email,password:pass}).then(function(res){
btn.disabled=false;btn.textContent="Create Account";
if(res.error){showAuthError("reg-error",res.error.message);return;}
_sbSession=res.data.session;
if(!_sbSession&&res.data.user)_sbSession={user:res.data.user};
if(!_sbSession){showAuthError("reg-error","Check your email to confirm, then log in.");return;}
sb.from("profiles").insert({id:_sbSession.user.id,display_name:name,age:age}).then(function(){});
cloudSync();window._closeAuth();showAccountBar();
toast("Account created! "+pet.name+" is saved \u2601\uFE0F");
if(typeof gtag!=="undefined")gtag("event","user_registered",{game:pet?pet.game:"none"});
});
};

window._doLogin=function(){
if(!sb)return;
var email=document.getElementById("login-email").value.trim();
var pass=document.getElementById("login-pass").value;
if(!email||!pass){showAuthError("login-error","Enter email and password");return;}
var btn=document.getElementById("login-btn");btn.disabled=true;btn.textContent="Logging in...";
sb.auth.signInWithPassword({email:email,password:pass}).then(function(res){
btn.disabled=false;btn.textContent="Log In";
if(res.error){showAuthError("login-error",res.error.message);return;}
_sbSession=res.data.session;
loadCloudPet().then(function(loaded){
if(loaded){var r=calcOffline();show("screen-pet");updateUI();updateCD();if(r)showAway(r);}
window._closeAuth();showAccountBar();toast("Welcome back!");
if(typeof gtag!=="undefined")gtag("event","user_login",{game:pet?pet.game:"none"});
});
});
};

window._doLogout=function(){
if(!sb)return;
sb.auth.signOut().then(function(){_sbSession=null;hideAccountBar();toast("Logged out");});
};

// ── Adopt / Release ────────────────────────────────────────
window._startAdopt=function(game){
var g=GAMES[game],pick=g.chars[Math.floor(Math.random()*g.chars.length)];
show("screen-hatch");
if(typeof gtag!=="undefined")gtag("event","pet_adopt_start",{game:game});
setTimeout(function(){document.getElementById("hatch-egg").style.animation="none";document.getElementById("hatch-egg").textContent="\u2728";document.getElementById("hatch-text").textContent="Here they come...";},2000);
setTimeout(function(){
pet={game:game,emoji:pick[0],name:pick[1],level:1,xp:0,hunger:50,energy:100,happiness:70,
str:1,def:1,hp:10,gold:1,weapon:null,wins:0,losses:0,bat_today:0,bat_date:"",
last_feed:0,last_train:0,last_rest:0,last_job:0,last_train_stat:"str",
created:Date.now(),lastVisit:Date.now()};
save();show("screen-pet");updateUI();updateCD();toast("Welcome, "+pet.name+"!");confetti();
if(typeof gtag!=="undefined")gtag("event","pet_adopted",{game:game,character:pick[1]});
},3500);
};

window._releasePet=function(){
if(!confirm("Release "+pet.name+"? This cannot be undone."))return;
if(_sbSession){sb.from("pets").delete().eq("user_id",_sbSession.user.id).then(function(){});}
localStorage.removeItem(KEY);pet=null;show("screen-pick");
};

// ── Init ───────────────────────────────────────────────────
(function init(){
var visits=parseInt(localStorage.getItem("bds_visits")||"0")+1;
localStorage.setItem("bds_visits",String(visits));
load();
function startUI(){
if(pet){var r=calcOffline();show("screen-pet");updateUI();updateCD();if(r)showAway(r);checkSavePrompt();}
else{var p=new URLSearchParams(window.location.search),g=p.get("game");if(g&&GAMES[g])window._startAdopt(g);else show("screen-pick");}
setInterval(function(){updateCD();if(document.querySelector('[data-tab="train"]').classList.contains("active"))updateTrainUI();if(document.querySelector('[data-tab="jobs"]').classList.contains("active"))updateJobs();},1000);
}
if(sb){
sb.auth.getSession().then(function(res){
if(res.data&&res.data.session){_sbSession=res.data.session;loadCloudPet().then(function(loaded){if(loaded)load();startUI();showAccountBar();});}
else{startUI();}
}).catch(function(){startUI();});
}else{startUI();}
})();
