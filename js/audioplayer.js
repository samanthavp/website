$(window).on("load",function(){
  // variables
  const dt = 1;
  const audio  = document.getElementById("audio");
  const pp     = document.getElementById("play-pause");
  const slider = document.getElementById("player-slider");
  const seekl  = document.getElementById("seek-left");
  const seekr  = document.getElementById("seek-right");
  const time   = document.getElementById("time-current");
  const player = document.getElementById("player");
  var focus = false;
  // print timestamp (audio player)
  const hms = function(dd){
    const hh = Math.floor(dd / 60 / 60);
    const mm = Math.floor(dd / 60) - (hh * 60);
    const ss = Math.floor(dd % 60);
    return(String(hh)+":"+(mm<10?"0":"")+String(mm)+":"+(ss<10?"0":"")+String(ss))
  }
  // slider update function
  const sliderUpdate = function(value){
    const p = 100*(value-slider.min)/(slider.max-slider.min);
    slider.style.background = "linear-gradient(to right,"+
      "#ffffff99 0%, #ffffff99 "+p+"%, #ffffff33 "+p+"%, #ffffff33 100%)";
    time.textContent = hms(audio.currentTime);
  };
  // proxy to make sure slider is always updated
  const sprox = new Proxy(slider,{ // TODO: does beforeinput fix?
    set: function(target,key,value){
      if (key==="value"){
        sliderUpdate(value);
      }
      target[key] = value;
      return true;
    }
  });
  // while audio plays...
  const whileplay = function(){
    sprox.value = dt * audio.currentTime;
    raf = requestAnimationFrame(whileplay);
  };
  // play-pause button
  pp.addEventListener("click",function(e){
    if (pp.classList.contains("play")){
      audio.play();
      requestAnimationFrame(whileplay);
      pp.classList.remove("play");
      pp.classList.add("pause");
    } else {
      audio.pause();
      cancelAnimationFrame(raf);
      pp.classList.remove("pause");
      pp.classList.add("play");
    }
    // avoid spacebar issues
    pp.blur();
    // TODO: kill scroll too...
  });
  // listeners
  const seekfun = function(t){
    audio.currentTime = t;
    sprox.value = dt * t;
  };
  seekl.addEventListener("click",function(){
    seekfun(audio.currentTime - 15);
  });
  seekr.addEventListener("click",function(){
    seekfun(audio.currentTime + 15);
  });
  slider.addEventListener("change",function(){
    seekfun(slider.value/dt);
  });
  // click to focus
  $("body").click(function(e){
    if (e.target.id=="player" || $(e.target).parents("#player").length) {
      focus = true;
    } else {
      focus = false;
    }
  });
  // key presses
  $(document).keydown(function(e){
    if (!focus){ return null; }
    if (e.which == 32){ pp.click();    } // spacebar
    if (e.which == 33){ seekl.click(); } // page up
    if (e.which == 34){ seekr.click(); } // page down
    if (e.which == 35){ seekfun(slider.max); } // end
    if (e.which == 36){ seekfun(slider.min); } // home
    if (e.which == 37){ seekfun(audio.currentTime - 1); } // arrow left
    if (e.which == 39){ seekfun(audio.currentTime + 1); } // arrow right
  });
  // set static audio stuff
  const metaloaded = function(){
    document.getElementById("time-total").textContent = hms(audio.duration);
    slider.max = dt*audio.duration;
  };
  metaloaded();
  audio.addEventListener("onloadedmetadata",metaloaded);
});