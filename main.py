import html_parser.extract_anchor as Extractor

# Hardcode some test data:
testString = """<body class="background">
<div id="main">
<div id="header-w">
      <div id="header">
    <div class="topmenu">
      
    </div>
                  
              <a href="/">
      <img src="/templates/inspiration-et/images/logo.png" border="0" class="logo">
      </a>
                <div class="slogan"></div>
                                     
  </div>        
</div>
<div id="wrapper">
          <div id="navr">
      <div class="tguser"></div>
    <div id="navl">
    <div id="nav">
        <div id="nav-left">
</div><div id="nav-right"></div></div></div></div>  
  <div id="main-content">
    <div class="clearpad"></div>
  <div id="message">
      
<div id="system-message-container">
</div>
  </div>    
            <div id="leftbar-w">
    <div id="sidebar">
        	<div class="module">
        <div class="inner">
			    <div class="module-body">
	        
<ul class="menu">
<li class="item-101 active deeper parent"><a href="/index.php/home" >Mid Rivers CAP - Home</a><ul><li class="item-108 current active"><a href="/" >Welcome!</a></li><li class="item-102"><a href="/index.php/home/menu" >Missions</a></li><li class="item-103"><a href="/index.php/home/menu-2/month.calendar/2013/09/06/-" >Calendar</a></li><li class="item-104"><a href="/index.php/home/menu-3" >FAQ</a></li><li class="item-125"><a href="/index.php/home/join-civil-air-patrol" >Join Civil Air Patrol</a></li><li class="item-105"><a href="/index.php/home/menu-4" >News</a></li><li class="item-127"><a href="/index.php/home/officers-corners" >Officers Corners</a></li><li class="item-143"><a href="http://www.gocivilairpatrol.com/" >CAP National Web Site</a></li><li class="item-145"><a href="http://www.ncrcap.us/" >CAP North Central Region</a></li><li class="item-144"><a href="http://www.mowgcap.us/" >CAP Missouri Wing</a></li></ul></li><li class="item-124"><a href="/index.php/log-in" >Log In</a></li></ul>
        </div>
        </div>
	</div>
	</div>
<!-- MODIFY social buttons here (add yours from addthis.com) -->
   
<div id="bookmark"><div id="addthis">
<div class="addthis_toolbox addthis_default_style addthis_32x32_style">
<a class="addthis_button_preferred_1"></a>
<a class="addthis_button_preferred_2"></a>
<a class="addthis_button_preferred_3"></a>
<a class="addthis_button_preferred_4"></a>
<a class="addthis_button_compact"></a>
</div>
</body>
"""

if __name__ == "__main__":
   # Simple little test driver for our Anchor Extractor:
   anchorParser = Extractor.HTMLAnchorExtractor();
   # Feed the extractor a simple test string.
   anchorParser.feed(testString);

   # 'attributes' is a list of tuples.
   attributes = anchorParser.GetAnchorAttributes();

