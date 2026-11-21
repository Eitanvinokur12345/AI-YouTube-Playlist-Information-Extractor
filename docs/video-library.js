// Video-focused views. Reads the existing database; no agent runtime.
const CORE_TABS = new Set(["overview","videos","hub","packages","taste","skills","tools","models",
  "comingsoon","prompts","improvement","tips","news","connectors","designs","sources","effectiveness",
  "selfimprove","devbuild","search"]);
const VIDEO_STAGES = {analyzed:"Analysis confirmed", queued:"Awaiting analysis", unconfirmed:"Historical analysis unconfirmed"};
function coreButton(label, attr, value) {
  return '<button class="qr-btn" '+attr+'="'+esc(value)+'">'+esc(label)+'</button>';
}
async function renderOverview() {
  const scan = await load("skill_scan.json");
  const stamp = scan && scan.at;
  view.innerHTML = '<section class="card"><h2>Knowledge library</h2>'+
    '<p>Browse findings extracted from playlists, public repositories and community sources.</p>'+
    '<div class="el-actions always">'+coreButton("Browse findings","data-core-tab","hub")+
    coreButton("Skills","data-core-tab","skills")+coreButton("Discoveries","data-core-tab","sources")+'</div></section>'+
    '<section class="card"><h3>Skill checks</h3><p>Source verification and malware signatures are checked separately.</p>'+
    '<p class="sub">'+(stamp ? 'Latest package and record scan: '+esc(fmtDate(stamp)) : 'Awaiting first signature scan')+'</p></section>';
  view.querySelectorAll("[data-core-tab]").forEach(b => { b.onclick = () => show(b.dataset.coreTab); });
}
async function renderVideos() {
  const c = await load("video_catalog.json");
  if (!c) {view.innerHTML=empty("Video catalog unavailable. Run the Refresh video library workflow.");return;}
  const query=q(), stage=state.videoStage||"all", category=state.videoCategory||"all";
  const filtered=c.videos.filter(function(v){
    return (stage==="all" || stage==="queued"&&v.queued || stage==="transcript"&&v.has_transcript || stage===v.stage)&&
      (category==="all"||v.categories.includes(category))&&
      (!query||[v.title,v.channel,v.video_id].concat(v.categories,v.elements.map(function(e){return e.name;})).join(" ").toLowerCase().includes(query));
  });
  const pages=Math.max(1,Math.ceil(filtered.length/40)), page=Math.min(state.videoPage||0,pages-1);
  state.videoPage=page;
  function option(val,label,current){return '<option value="'+esc(val)+'"'+(val===current?' selected':'')+'>'+esc(label)+'</option>';}
  view.innerHTML='<section class="card"><h2>Video library</h2><p class="sub">Search titles, channels, categories and extracted findings with the search box above.</p>'+
    '<label>Content stage <select id="video-stage">'+option("all","All stages",stage)+Object.entries(VIDEO_STAGES).map(function(e){return option(e[0],e[1],stage);}).join("")+option("transcript","Has a real transcript",stage)+'</select></label> '+
    '<label>Category <select id="video-category">'+option("all","All categories",category)+Object.keys(c.summary.categories).sort().map(function(cat){return option(cat,cat,category);}).join("")+'</select></label>'+
    '<p class="sub">'+filtered.length.toLocaleString()+' matching videos · page '+(page+1)+' of '+pages+'. A confirmed video may also be queued for deeper analysis.</p></section>'+
    '<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,340px),1fr));gap:14px">'+filtered.slice(page*40,(page+1)*40).map(function(v){
      return '<article class="card" style="margin:0;min-width:0"><span class="pill">'+esc(VIDEO_STAGES[v.stage])+'</span> <span class="pill">'+
        (v.has_transcript?"Transcript available":esc(v.retrieval+" only"))+'</span><h3><a target="_blank" rel="noopener" href="'+esc(v.url)+'">'+esc(v.title)+'</a></h3>'+
        '<p class="sub">'+esc(v.channel||"Channel not recorded")+(v.published_at?" · "+esc(fmtDate(v.published_at)):"")+'</p><p>'+
        (v.categories.length?v.categories.map(function(cat){return '<span class="pill">'+esc(cat)+'</span>';}).join(" "):'<span class="sub">Categories not yet extracted</span>')+'</p>'+
        (v.elements.length?'<details><summary>'+v.elements.length+' extracted findings</summary>'+v.elements.map(function(e){
          return '<p><a href="#element/'+encodeURIComponent(e.id)+'">'+esc(e.type)+" · "+esc(e.name)+'</a></p>';
        }).join("")+'</details>':"")+'</article>';
    }).join("")+'</div>'+(filtered.length?"":empty("No matching videos."))+
    '<div style="display:flex;justify-content:center;align-items:center;gap:16px;margin:24px 0"><button class="qr-btn" id="video-prev"'+(page===0?' disabled':'')+'>Previous</button><span>'+(page+1)+' / '+pages+'</span><button class="qr-btn" id="video-next"'+(page+1===pages?' disabled':'')+'>Next</button></div>';
  [["video-stage","videoStage"],["video-category","videoCategory"]].forEach(function(pair){
    view.querySelector("#"+pair[0]).onchange=function(e){state[pair[1]]=e.target.value;state.videoPage=0;show("videos");};
  });
  view.querySelector("#video-prev").onclick=function(){state.videoPage=Math.max(0,page-1);show("videos");};
  view.querySelector("#video-next").onclick=function(){state.videoPage=page+1;show("videos");};
}
