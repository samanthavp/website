$(window).on("load",function(){
  // variables
  const dt = 1;
  const audio  = document.getElementById("audio");
  const pp     = document.getElementById("play-pause");
  const slider = document.getElementById("player-slider");
  const time   = document.getElementById("time-current");
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
  const sprox = new Proxy(slider,{
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
  pp.addEventListener("click",function(){
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
  });
  // skip buttons
  document.getElementById("seek-left").addEventListener("click",function(){
    audio.currentTime -= 15;
    sprox.value = dt * audio.currentTime;
  });
  document.getElementById("seek-right").addEventListener("click",function(){
    audio.currentTime += 15;
    sprox.value = dt * audio.currentTime;
  });
  // slider listener
  slider.addEventListener("change",function(){
    audio.currentTime = slider.value / dt;
    sliderUpdate(slider.value);
  });
  // set static audio stuff
  document.getElementById("time-total").textContent = hms(audio.duration); // TODO
  slider.max = dt*audio.duration; // TODO
});